# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectType(models.Model):
    _name = 'project.type.toratto'
    
    name = fields.Char(string="Nombre", required=True, size=50)