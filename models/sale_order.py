# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = "sale.order"

    client_order_ref = fields.Many2one('res.partner',
        ondelete='set null', string="Referencia del Cliente", index=True)

    def action_toratto_quotation_email_send(self):
        print("enviando correo")
        template_id = self.env.ref('toratto.sale_order_email_template').id
        print(template_id)
        template = self.env['mail.template'].browse(template_id)
        print(template)
        template.send_mail(self.id, force_send = True)