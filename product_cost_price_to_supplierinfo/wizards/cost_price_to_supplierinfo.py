from odoo import _, api, fields, models


class CostPriceToSupplierinfo(models.TransientModel):

    _name = "product_cost_price_to_supplierinfo.cost_price_wizard"

    def find_latest_supplier(self, product_template):
        po_line_model = self.env["purchase.order.line"]
        latest_line = po_line_model.search(
            args=[("product_id.product_tmpl_id", "=", product_template.id)],
            order="date_planned DESC",
            limit=1,
        )

        if latest_line:
            return latest_line.order_id.partner_id
        else:
            return False

    @api.multi
    def copy_cost_price(self):
        """Create a new purchase request containing the selected PO lines."""

        product_template_model = self.env["product.template"]
        supplierinfo_model = self.env["product.supplierinfo"]

        for product in product_template_model.browse(self.env.context["active_ids"]):

            if not product.standard_price:
                # If no cost price set, move on to next product
                continue

            # Set some common values
            supplierinfo_vals = {
                "product_tmpl_id": product.id,
                "price": product.standard_price,
                "from_cost_price": True,
            }

            if product.seller_ids:
                # If a supplier exists, copy the rest of the values from there.
                # Note: the original supplier does not get deleted at this
                # point
                primary = product.seller_ids[0]
                supplierinfo_vals["name"] = primary.name.id
                supplierinfo_vals["product_name"] = primary.product_name
                supplierinfo_vals["product_code"] = primary.product_code
                supplierinfo_vals["delay"] = primary.delay
                supplierinfo_vals["min_qty"] = primary.min_qty
                supplierinfo_vals["date_start"] = primary.date_start
                supplierinfo_vals["date_end"] = primary.date_end
                supplierinfo_vals["sequence"] = primary.sequence - 1

                msg_body = _(
                    " Cost price %0.2f copied to supplierinfo, "
                    "using existing supplier '%s'"
                ) % (product.standard_price, primary.name.name)
            else:
                # If no supplier exists, try to find the last partner the
                # product was bought from
                latest_supplier = self.find_latest_supplier(product)

                if latest_supplier:
                    supplierinfo_vals["name"] = latest_supplier.id
                    msg_body = _(
                        " Cost price %0.2f copied to supplierinfo, "
                        "using latest Purchase Order supplier '%s'"
                    ) % (product.standard_price, latest_supplier.name)
                else:
                    # If still nothing found, use a placeholder partner that
                    # can be replaced later
                    placeholder_partner = self.env.ref(
                        "product_cost_price_to_supplierinfo"
                        ".supplierinfo_placeholder_partner"
                    )

                    supplierinfo_vals["name"] = placeholder_partner.id
                    msg_body = _(
                        " Cost price %0.2f copied to supplierinfo, "
                        "no Purchase Orders found, "
                        "using placeholder supplier '%s'"
                    ) % (product.standard_price, placeholder_partner.name)

            supplierinfo_model.create(supplierinfo_vals)
            product.message_post(subtype="mt_comment", body=msg_body)

    name = fields.Char("Name")
