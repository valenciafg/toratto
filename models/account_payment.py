# -*- coding: utf-8 -*-
from odoo import models, fields, api

class account_payment(models.Model):
    _name = "account.payment"
    _inherit = "account.payment"
    _description = "Payments"

    name = fields.Char(readonly=False, copy=False)  # The name is attributed upon post()
    description = fields.Char('Descripcion', required=True)
    amount = fields.Monetary(string='Monto Programado', required=True, readonly=True, states={'draft': [('readonly', False)]}, tracking=True)
