# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MinimalModel(models.Model):
    _name = 'test.model'
    _description = 'Prueba'

    name = fields.Char(required=True)