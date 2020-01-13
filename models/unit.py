# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Unit(models.Model):
    _name = 'unit.toratto'
    _description = 'Unidades'

    code = fields.Char(string="Código", required=True, size=15)
    name = fields.Char(string="Nombre", required=True, size=50)
    unit_type = fields.Char(string="Tipo", required=True, size=100)
    sub_division = fields.Char(string="Subdivisión", required=True, size=150)
    proyect_id = fields.Many2one('project.toratto',
        ondelete='set null', string="Proyecto", index=True)
    st_commercial = fields.Char(string="Estado Comercial", required=True, size=200)
    currency_id = fields.Many2one('res.currency',
        ondelete='set null', string="Moneda", index=True)
    price = fields.Monetary(string="Precio")
    m2_price = fields.Monetary(string="Precio M2")
