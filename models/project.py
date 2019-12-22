# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    _name = 'project.toratto'
    _description = 'Proyectos de construccion'

    code = fields.Char(required=True, size=15)
    name = fields.Char(required=True, size=50)
    currency_id = fields.Many2one('currency.type.toratto',
        ondelete='set null', string="Currency", index=True)
    building_type_id = fields.Many2one('building.type.toratto',
        ondelete='set null', string="Building Type", index=True)
    project_type_id = fields.Many2one('project.type.toratto',
        ondelete='set null', string="Project Type", index=True)
