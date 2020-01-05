# -*- coding: utf-8 -*-

from odoo import models, fields, api

class District(models.Model):
    _name = 'district.toratto'
    
    country_id = fields.Many2one('res.country',
        ondelete='set null', string="País", index=True)
    department_id = fields.Many2one('res.country.state',
        ondelete='set null', string="Departamento", index=True)
    province_id = fields.Many2one('province.toratto',
        ondelete='set null', string="Provincia", index=True)
    name = fields.Char(string="Distrito", required=True, size=200)

    @api.onchange('country_id')
    def _onchange_country_id(self):
        for rec in self:
            return {
                'domain': {
                    'department_id': [('country_id', '=', rec.country_id.id)]
                }
            }
    
    @api.onchange('department_id')
    def _onchange_department_id(self):
        for rec in self:
            return {
                'domain': {
                    'province_id': [
                        ('country_id', '=', rec.country_id.id),
                        ('department_id', '=', rec.department_id.id)
                    ]
                }
            }
