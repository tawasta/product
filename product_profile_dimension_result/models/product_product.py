from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    profile_info_id = fields.Many2one("product.profile.formula", copy=False)
    profile_info_result = fields.Text(compute=lambda self: self._compute_info_result())

    def write(self, vals):
        info_type = vals.get("profile_info_type", False)
        if info_type:
            profile_info = self.env["product.profile.formula"].search(
                [("profile_type", "=", info_type)]
            )
            if profile_info:
                vals["profile_info_id"] = profile_info.id
        else:
            vals["profile_info_id"] = False
        return super().write(vals)

    def _compute_info_result(self):
        for prod in self:
            profile = prod.profile_info_id
            if profile:
                prod.profile_info_result = (
                    "{symbol_first}{diameter}{symbol_second}"
                    "{length}{multiply_first}{height}{symbol_third}"
                    "{multiply_second}{width}".format(
                        symbol_first=profile.symbol_first or "",
                        diameter=profile.show_diameter
                        and str(prod.diameter) + " "
                        or "",
                        symbol_second=profile.symbol_second or "",
                        length=profile.show_length
                        and str(prod.product_length) + " "
                        or "",
                        multiply_first=profile.multiply_first or "",
                        height=profile.show_height
                        and str(prod.product_height) + " "
                        or "",
                        symbol_third=profile.symbol_third or "",
                        multiply_second=profile.multiply_second or "",
                        width=profile.show_width and prod.product_width or "",
                    )
                )
            else:
                prod.profile_info_result = ""
