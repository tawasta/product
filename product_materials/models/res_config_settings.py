from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    group_product_template_manage_product_materials = fields.Boolean(
        string="Manage Material Info for Products",
        implied_group="product_materials."
        "group_product_template_manage_product_materials",
    )

    group_product_template_manage_product_packaging_materials = fields.Boolean(
        string="Manage Packaging Material Info for Products",
        implied_group="product_materials."
        "group_product_template_manage_product_packaging_materials",
    )

    group_product_template_manage_materials_recycling_percentages = fields.Boolean(
        string="Manage Product & Packaging Materials' Recycling Percentages",
        implied_group="product_materials."
        "group_product_template_manage_materials_recycling_percentages",
    )

    group_product_template_enable_product_materials_on_prints = fields.Boolean(
        string="Enable showing Product Materials on prints",
        implied_group="product_materials."
        "group_product_template_enable_product_materials_on_prints",
    )

    # The new compliances that are managed on product material composition lines

    group_prod_mat_comp_manage_compliance_conflict_area_minerals = fields.Boolean(
        string="Manage Conflict Area Minerals Compliance Info for Product Materials",
        implied_group="product_materials."
        "group_prod_mat_comp_manage_compliance_conflict_area_minerals",
    )

    group_prod_mat_comp_manage_compliance_halogens = fields.Boolean(
        string="Manage Halogen Compliance Info for Product Materials",
        implied_group="product_materials."
        "group_prod_mat_comp_manage_compliance_halogens",
    )

    group_prod_mat_comp_manage_compliance_packaging_materials = fields.Boolean(
        string="Manage Packaging Materials Checked Info for Product Materials",
        implied_group="product_materials."
        "group_prod_mat_comp_manage_compliance_packaging_materials",
    )
