# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Funders(models.Model):
    _name = 'funders.toratto'
    
    name = fields.Char(string="Nombre de Entidad Bancaria", required=True, size=50)
