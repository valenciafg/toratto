# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Contact(models.Model):
    _name = 'contact.toratto'
    
    name = fields.Char(string="Nombre de contacto", required=True, size=200)