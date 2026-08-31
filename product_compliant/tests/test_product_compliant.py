from odoo.tests.common import TransactionCase


class TestProductCompliant(TransactionCase):
    def setUp(self):
        super().setUp()

        self.ProductCompliant = self.env["product.compliant"]

        self.general_value = self.ProductCompliant.create(
            {
                "name": "Not Applicable",
                "sequence": 20,
                "description": "Compliance not applicable for this product.",
            }
        )

        self.reach_value = self.ProductCompliant.create(
            {
                "name": "REACH Registered",
                "sequence": 10,
                "selectable_for": "reach",
            }
        )

        self.atex_value = self.ProductCompliant.create(
            {
                "name": "ATEX Certified",
                "sequence": 5,
                "selectable_for": "atex",
            }
        )

    def test_compliance_value_creation(self):
        value = self.ProductCompliant.create(
            {
                "name": "Yes",
                "sequence": 30,
                "selectable_for": "rohs",
                "description": "Product is RoHS compliant.",
            }
        )

        self.assertEqual(value.name, "Yes")
        self.assertEqual(value.sequence, 30)
        self.assertEqual(value.selectable_for, "rohs")
        self.assertEqual(value.description, "Product is RoHS compliant.")

    def test_compliance_value_ordering(self):
        values = self.ProductCompliant.search([])
        self.assertEqual(values[0], self.atex_value)
        self.assertEqual(values[1], self.reach_value)
        self.assertEqual(values[2], self.general_value)

    def test_empty_selectable_for_available_for_all(self):
        for field_name in (
            "atex_compliant",
            "reach_compliant",
            "rohs_compliant",
            "composition_checked_compliant",
            "msds_checked_compliant",
            "work_safety_checked_compliant",
        ):
            domain = self.env["product.template"]._fields[field_name].domain
            self.assertIn(False, domain[0][2])

    def test_selectable_for_restricts_field_domains(self):
        atex_domain = self.env["product.template"]._fields["atex_compliant"].domain
        reach_domain = self.env["product.template"]._fields["reach_compliant"].domain

        atex_values = self.ProductCompliant.search(atex_domain)
        self.assertIn(self.general_value, atex_values)
        self.assertIn(self.atex_value, atex_values)
        self.assertNotIn(self.reach_value, atex_values)

        reach_values = self.ProductCompliant.search(reach_domain)
        self.assertIn(self.general_value, reach_values)
        self.assertIn(self.reach_value, reach_values)
        self.assertNotIn(self.atex_value, reach_values)

    def test_product_compliance_fields(self):
        product = self.env["product.template"].create(
            {
                "name": "Compliant Product",
                "atex_compliant": self.atex_value.id,
                "reach_compliant": self.reach_value.id,
                "rohs_compliant": self.general_value.id,
                "composition_checked_compliant": self.general_value.id,
                "msds_checked_compliant": self.general_value.id,
                "work_safety_checked_compliant": self.general_value.id,
            }
        )

        self.assertEqual(product.atex_compliant, self.atex_value)
        self.assertEqual(product.reach_compliant, self.reach_value)
        self.assertEqual(product.rohs_compliant, self.general_value)
        self.assertEqual(product.composition_checked_compliant, self.general_value)
        self.assertEqual(product.msds_checked_compliant, self.general_value)
        self.assertEqual(product.work_safety_checked_compliant, self.general_value)

    def test_settings_implied_groups(self):
        settings = self.env["res.config.settings"].create(
            {
                "group_product_template_manage_compliance_atex": True,
                "group_product_template_manage_compliance_reach": True,
            }
        )
        settings.execute()

        group_atex = self.env.ref(
            "product_compliant.group_product_template_manage_compliance_atex"
        )
        group_reach = self.env.ref(
            "product_compliant.group_product_template_manage_compliance_reach"
        )
        group_rohs = self.env.ref(
            "product_compliant.group_product_template_manage_compliance_rohs"
        )

        self.assertIn(group_atex, self.env.user.all_group_ids)
        self.assertIn(group_reach, self.env.user.all_group_ids)
        self.assertNotIn(group_rohs, self.env.user.all_group_ids)
