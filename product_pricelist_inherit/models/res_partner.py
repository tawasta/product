from odoo import api, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    @api.onchange("property_product_pricelist")
    def onchange_pricelist_update_children(self):
        for record in self:
            pricelist = record.property_product_pricelist

            if pricelist:
                for child in record.child_ids:
                    child.property_product_pricelist = pricelist

    @api.model
    def create(self, vals):
        # Inherit pricelist from parent
        if "property_product_pricelist" not in vals and "parent_id" in vals:
            parent_id = self.browse([vals["parent_id"]])
            vals["property_product_pricelist"] = parent_id.property_product_pricelist.id

        res = super(ResPartner, self).create(vals)

        return res

    def write(self, vals):
        res = super(ResPartner, self).write(vals)

        pricelist = vals.get("property_product_pricelist", False)
        if pricelist:
            for record in self:
                for child in record.child_ids:
                    child.property_product_pricelist = pricelist

        return res
