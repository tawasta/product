from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    group_product_product_manage_product_materials = fields.Boolean(
        string="Manage Material Info for Products",
        implied_group="product_materials."
        "group_product_product_manage_product_materials",
    )

    group_product_product_manage_product_packaging_materials = fields.Boolean(
        string="Manage Packaging Material Info for Products",
        implied_group="product_materials."
        "group_product_product_manage_product_packaging_materials",
    )

    group_product_product_manage_material_hierarchy = fields.Boolean(
        string="Use three-level Material Hierarchy",
        implied_group="product_materials."
        "group_product_product_manage_material_hierarchy",
    )

    group_product_product_manage_materials_weights = fields.Boolean(
        string="Manage Product & Packaging Materials' Weights",
        implied_group="product_materials."
        "group_product_product_manage_materials_weights",
    )

    group_product_product_manage_materials_recycling_percentages = fields.Boolean(
        string="Manage Product & Packaging Materials' Recycling Percentages",
        implied_group="product_materials."
        "group_product_product_manage_materials_recycling_percentages",
    )

    group_product_product_manage_materials_waste = fields.Boolean(
        string="Manage Product & Packaging Materials' Waste Components and Endpoints",
        implied_group="product_materials."
        "group_product_product_manage_materials_waste",
    )

    group_product_product_enable_product_materials_on_prints = fields.Boolean(
        string="Enable showing Product Materials on prints",
        implied_group="product_materials."
        "group_product_product_enable_product_materials_on_prints",
    )

    group_product_product_manage_materials_biogenic_and_renewable = fields.Boolean(
        string="Manage Product & Packaging Materials' Biogenic and Renewable Percentages",
        implied_group="product_materials."
        "group_product_product_manage_materials_biogenic_and_renewable_percentages",
    )
