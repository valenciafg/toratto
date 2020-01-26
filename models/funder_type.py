# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FunderType(models.Model):
    _name = 'funder.type.toratto'

    name = fields.Char(string="Nombre", required=True, size=50)
