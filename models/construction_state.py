# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ConstructionState(models.Model):
    _name = 'construction_state.toratto'
    
    name = fields.Char(string="Estado de construccion", required=True, size=200)