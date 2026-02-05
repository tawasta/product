from odoo import api, fields, models


class ProductProfileFormula(models.Model):
    _name = "product.profile.formula"
    _description = "Profile formula of products"

    product_id = fields.One2many("product.product", "profile_info_id")
    profile_type = fields.Char(required=True, copy=False)
    show_diameter = fields.Boolean(copy=False)
    show_length = fields.Boolean(copy=False)
    show_height = fields.Boolean(copy=False)
    show_width = fields.Boolean(copy=False)
    multiply_first = fields.Char(copy=False)
    multiply_second = fields.Char(copy=False)
    multiply_third = fields.Char(copy=False)
    symbol_first = fields.Char(copy=False)
    symbol_second = fields.Char(copy=False)
    symbol_third = fields.Char(copy=False)

    _sql_constraints = [
        (
            "default_profile_type",
            "unique(profile_type)",
            "Profile Type must be unique across the database!",
        )
    ]

    @api.depends("product_id", "profile_type")
    def _compute_display_name(self):
        for rec in self:
            if rec.product_id:
                rec.display_name = f"{rec.id} | {rec.profile_type}"
            else:
                rec.display_name = f"{rec.profile_type}"
