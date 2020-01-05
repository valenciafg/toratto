# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Province(models.Model):
    _name = 'province.toratto'
    
    country_id = fields.Many2one('res.country',
        ondelete='set null', string="País", index=True)
    department_id = fields.Many2one('res.country.state',
        ondelete='set null', string="Departamento", index=True)
    name = fields.Char(string="Provincia", required=True, size=200)

    @api.onchange('country_id')
    def _onchange_country_id(self):
        for rec in self:
            return {
                'domain': {
                    'department_id': [('country_id', '=', rec.country_id.id)]
                }
            }