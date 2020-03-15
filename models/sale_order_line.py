# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _name = "sale.order.line"
    _inherit = "sale.order.line"

    #initial_fee = fields.Float(string='C.Inicial (%)', default=10.0)
    """
    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id', 'initial_fee')
    def _compute_amount(self):
        for line in self:
            price = line.price_unit * (1 - (line.discount + line.initial_fee or 0.0) / 100.0)
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id)
            line.update({
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })

    @api.depends('price_unit', 'discount')
    def _get_price_reduce(self):
        for line in self:
            line.price_reduce = line.price_unit * (1.0 - (line.discount + line.initial_fee) / 100.0)
    """