# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BuildingType(models.Model):
    _name = 'building.type.toratto'
    
    name = fields.Char(string="Nombre", required=True, size=50)