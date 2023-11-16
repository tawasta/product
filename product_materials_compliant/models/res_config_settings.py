from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    group_prod_mat_comp_manage_compliance_chemicals = fields.Boolean(
        string="Manage Chemicals Compliance Info for Product Materials",
        implied_group="product_materials_compliant."
        "group_prod_mat_comp_manage_compliance_chemicals",
    )

    group_prod_mat_comp_manage_compliance_conflict_area_minerals = fields.Boolean(
        string="Manage Conflict Area Minerals Compliance Info for Product Materials",
        implied_group="product_materials_compliant."
        "group_prod_mat_comp_manage_compliance_conflict_area_minerals",
    )

    group_prod_mat_comp_manage_compliance_halogens = fields.Boolean(
        string="Manage Halogen Compliance Info for Product Materials",
        implied_group="product_materials_compliant."
        "group_prod_mat_comp_manage_compliance_halogens",
    )

    group_prod_mat_comp_manage_compliance_pop = fields.Boolean(
        string="Manage POP (Persistent Organic Pollutants) "
        "Compliance Info for Product Materials",
        implied_group="product_materials_compliant."
        "group_prod_mat_comp_manage_compliance_pop",
    )

    group_prod_mat_comp_manage_compliance_reach = fields.Boolean(
        string="Manage REACH Compliance Info for Product Materials",
        implied_group="product_materials_compliant."
        "group_prod_mat_comp_manage_compliance_reach",
    )

    group_prod_mat_comp_manage_compliance_rohs = fields.Boolean(
        string="Manage RoHS Compliance Info for Product Materials",
        implied_group="product_materials_compliant."
        "group_prod_mat_comp_manage_compliance_rohs",
    )

    group_prod_mat_comp_manage_compliance_scip = fields.Boolean(
        string="Manage SCIP (Substances of Concern In Products) "
        "Compliance Info for Product Materials",
        implied_group="product_materials_compliant."
        "group_prod_mat_comp_manage_compliance_scip",
    )
