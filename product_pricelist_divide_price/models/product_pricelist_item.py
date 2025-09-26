from odoo import _, api, fields, models, tools


class ProductPricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    divide_by = fields.Float(string="Divide by", copy=False)

    def _compute_price(self, product, quantity, uom, date, currency=None):
        price = super()._compute_price(
            product=product, quantity=quantity, uom=uom, date=date, currency=currency
        )

        if self.compute_price == "formula":
            price = price / self.divide_by

        return price

    @api.onchange("compute_price")
    def _onchange_compute_price(self):
        res = super()._onchange_compute_price()
        if self.compute_price != "formula":
            self.update(
                {
                    "divide_by": 0.0,
                }
            )
        return res

    @api.depends(
        "applied_on",
        "categ_id",
        "product_tmpl_id",
        "product_id",
        "compute_price",
        "fixed_price",
        "pricelist_id",
        "percent_price",
        "price_discount",
        "price_surcharge",
    )
    def _compute_name_and_price(self):
        res = super()._compute_name_and_price()
        for item in self:
            if item.compute_price not in ("fixed", "percentage") and item.divide_by:
                item.price = _(
                    "%(percentage)s %% discount, %(price)s surcharge "
                    "and %(divide_by)s division",
                    percentage=item.price_discount,
                    price=item.price_surcharge,
                    divide_by=item.divide_by,
                )
        return res

    @api.depends_context("lang")
    @api.depends(
        "compute_price", "price_discount", "price_surcharge", "base", "price_round"
    )
    def _compute_rule_tip(self):
        res = super()._compute_rule_tip()
        base_selection_vals = {
            elem[0]: elem[1]
            for elem in self._fields["base"]._description_selection(self.env)
        }

        for item in self:
            if item.divide_by:
                item.rule_tip = False
                if item.compute_price != "formula":
                    continue
                base_amount = 100
                discount_factor = (100 - item.price_discount) / 100
                divide_by = item.divide_by
                discounted_price = base_amount / divide_by * discount_factor
                if item.price_round:
                    discounted_price = tools.float_round(
                        discounted_price, precision_rounding=item.price_round
                    )
                surcharge = tools.format_amount(
                    item.env, item.price_surcharge, item.currency_id
                )
                item.rule_tip = _(
                    "%(base)s with a %(discount)s %% discount and %(surcharge)s "
                    "extra fee\n"
                    "Example: %(amount)s / %(divide_by)s * %(discount_charge)s + "
                    "%(price_surcharge)s → %(total_amount)s",
                    base=base_selection_vals[item.base],
                    discount=item.price_discount,
                    surcharge=surcharge,
                    amount=tools.format_amount(item.env, 100, item.currency_id),
                    divide_by=divide_by,
                    discount_charge=discount_factor,
                    price_surcharge=surcharge,
                    total_amount=tools.format_amount(
                        item.env,
                        discounted_price + item.price_surcharge,
                        item.currency_id,
                    ),
                )
        return res
