from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    quality_instruction_ids = fields.Many2many(
        "product_quality_instruction.instruction",
        "prod_qual_instr_rel",
        "prod_id",
        "instr_id",
        "Quality Instructions",
    )
