# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Agreement(models.Model):
    _name = 'agreement.toratto'
    _description = 'Minutas'

    name = fields.Char(string="Nombre", required=True, size=50)
#    code = fields.Char(string="Codigo", required=True, copy=False)
#    title = fields.Char(string="Titulo", required=True, size=50)
#    tag =  fields.Selection([
#                ('El Comprador', 'El Compredor'),
#                ('Los Compradores', 'Los Compradores'),
#                ('La Compradora', 'La Compradora'),
#                ('Las Compradoras', 'Las Compradoras'),
#                ], string='Itiqueta', required=True
#    )
    contact_1 = fields.Many2one('res.partner', string='Propietario 1')
    contact_2 = fields.Many2one('res.partner', string='Propietario 2')
    contact_3 = fields.Many2one('res.partner', string='Propietario 3')
    contact_4 = fields.Many2one('res.partner', string='Propietario 4')
    order_line = fields.Many2one('sale.order', string='Proforma')
