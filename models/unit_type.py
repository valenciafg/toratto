# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UnitType(models.Model):
    _name = 'unit.type.toratto'
    
    name = fields.Char(string="Nombre", required=True, size=100)
