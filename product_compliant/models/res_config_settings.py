from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    group_product_template_manage_compliance_atex = fields.Boolean(
        string="Manage ATEX Compliance Info for Products",
        implied_group="product_compliant."
        "group_product_template_manage_compliance_atex",
    )

    group_product_template_manage_compliance_reach = fields.Boolean(
        string="Manage REACH Compliance Info for Products",
        implied_group="product_compliant."
        "group_product_template_manage_compliance_reach",
    )

    group_product_template_manage_compliance_rohs = fields.Boolean(
        string="Manage RoHS Compliance Info for Products",
        implied_group="product_compliant."
        "group_product_template_manage_compliance_rohs",
    )

    group_product_template_manage_compliance_composition_checked = fields.Boolean(
        string="Manage Composition Checked Info for Products",
        implied_group="product_compliant."
        "group_product_template_manage_compliance_composition_checked",
    )

    group_product_template_manage_compliance_msds_checked = fields.Boolean(
        string="Manage MSDS (Material Safety Data Sheet) Checked Info for Products",
        implied_group="product_compliant."
        "group_product_template_manage_compliance_msds_checked",
    )

    group_product_template_manage_compliance_work_safety_checked = fields.Boolean(
        string="Manage Work Safety Checked Info for Products",
        implied_group="product_compliant."
        "group_product_template_manage_compliance_work_safety_checked",
    )
