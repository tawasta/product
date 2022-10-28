from odoo import fields, models


class QualityInstruction(models.Model):
    _name = "product_quality_instruction.instruction"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Product Quality Instruction Document"
    _INSTRUCTION_TYPES = [("text", "Text"), ("url", "URL"), ("file", "File")]

    name = fields.Char(required=True)
    type = fields.Selection(_INSTRUCTION_TYPES, required=True)
    instruction_text = fields.Text(string="Instruction")
    instruction_url = fields.Char(string="URL")
    instruction_file = fields.Binary(string="File", attachment=True)
    comments = fields.Text()
    active = fields.Boolean(
        strgin="Active",
        default=True,
        help="Inactive quality instructions are hidden from lists but remain stored.",
    )
    product_template_ids = fields.Many2many(
        "product.template",
        "prod_qual_instr_rel",
        "instr_id",
        "prod_id",
        "Products",
        help="Products that this instruction applies to",
    )
