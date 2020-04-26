# -*- coding: utf-8 -*-
from odoo import models, fields, api
from num2words import num2words

class SaleOrderLine(models.Model):
    _name = "sale.order.line"
    _inherit = "sale.order.line"

    initial_fee = fields.Float(string='C.Inicial (%)', default=10.0)
    amount_of_separation = fields.Monetary(string="Monto de Separacion", default=2500.0)
    discount2 = fields.Monetary(string="Desc")

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id', 'initial_fee', 'amount_of_separation', 'discount2')
    def _compute_amount(self):
        for line in self:
            price = (line.price_unit * (1 - (line.discount + line.initial_fee or 0.0) / 100.0) - line.discount2)
            price = price - line.amount_of_separation
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id)
            line.update({
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })

    @api.depends('price_unit', 'discount')
    def _get_price_reduce(self):
        for line in self:
            line.price_reduce = (line.price_unit * (1.0 - (line.discount + line.initial_fee) / 100.0) - line.discount2)

    sale_order_option2_ids = fields.One2many('sale.order.option2', 'line_id', 'Optional2 Products Lines')

#   @api.model
#   def render_html(self, docids, data=None):
#        report_obj = self.env['report']
#        report = report_obj._get_report_from_name('sale_order.report_agreement_document')
#        docs = self.env[report.model].browse(docids)
#        docargs = {
#            'doc_ids': docids,
#            'doc_model': report.model,
#            'docs': docs,
#            'data': data,
#            'to_word': number_to_letter.to_word,
#        }
#        return report_obj.render('sale_order.report_agreement_document', docargs)

class SaleOrderOption2(models.Model):
    _name = "sale.order.option2"
    _description = "Sale Options2"
    _order = 'sequence, id'


    order_id = fields.Many2one('sale.order', 'Sales Order Reference', ondelete='cascade', index=True)
    line_id = fields.Many2one('sale.order.line', ondelete="set null", copy=False)
    description = fields.Char('account.payment')
    product_id = fields.Many2one('account.payment')
    sequence = fields.Integer('Sequence', help="Gives the sequence order when displaying a list of optional products.")

