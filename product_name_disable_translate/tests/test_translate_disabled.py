from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestTranslateDisabled(TransactionCase):
    def test_field_translate_metadata_template(self):
        """product.template.name must not be translatable."""
        field = self.env["product.template"]._fields["name"]
        self.assertFalse(bool(field.translate))

    def test_field_translate_metadata_product(self):
        """product.product.name (delegated) must not be translatable."""
        field = self.env["product.product"]._fields["name"]
        self.assertFalse(bool(field.translate))

    def test_name_not_translated_across_langs(self):
        """Writing in another lang overwrites the single value (no jsonb store)."""
        self.env["res.lang"]._activate_lang("fr_FR")
        product = self.env["product.product"].create({"name": "English"})
        product.with_context(lang="fr_FR").name = "Francais"
        self.assertEqual(
            product.with_context(lang="en_US").name,
            "Francais",
            "Name should be overwritten, not stored as a separate translation.",
        )

    def test_name_search_still_works(self):
        """Trigram-backed name_search must still find products."""
        product = self.env["product.product"].create({"name": "Test Product XYZ"})
        res = self.env["product.template"].name_search(
            name="Product XY", operator="ilike"
        )
        self.assertIn(product.product_tmpl_id.id, [r[0] for r in res])
