# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_toratto_quotation_email_send(self):
        print("enviando correo")
        template_id = self.env.ref('toratto.sale_order_email_template').id
        print(template_id)
        template = self.env['mail.template'].browse(template_id)
        print(template)
        template.send_mail(self.id, force_send = True)