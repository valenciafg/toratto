# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CurrencyType(models.Model):
    _name = 'currency.type.toratto'
    
    code = fields.Char(required=True, size=15)
    name = fields.Char(required=True, size=50)
    symbol = fields.Char(size=5)
    #currency = fields.Selection(required=True, list([('dolar','Dolar'),('sol','Sol')]))
