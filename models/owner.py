# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Owner(models.Model):
    _name = 'owner.toratto'
    
    name = fields.Char(string="Propietario", required=True, size=200)