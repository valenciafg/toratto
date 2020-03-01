# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Plans(models.Model):
    _name = 'plans.toratto'
    _description = 'Planos'

    name = fields.Char(string="Nombre", required=True, size=50)
    logo = fields.Binary(string='Imagen del Plano', attachment=True)
