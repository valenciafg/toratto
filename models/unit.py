# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Unit(models.Model):
    _name = 'unit.toratto'
    _description = 'Unidades'

    code = fields.Char(string="Código", required=True, size=15)
    name = fields.Char(string="Nombre", required=True, size=50)
    unit_type = fields.Many2one('unit.type.toratto',
        ondelete='set null', string="Tipo", index=True)
    sub_division = fields.Char(string="Subdivisión", required=True, size=150)
    proyect_id = fields.Many2one('project.toratto',
        ondelete='set null', string="Proyecto", index=True)  
    floor_number = fields.Integer(
        string='Piso',
    )
    #   COMERCIAL
    st_commercial = fields.Selection(
        string='Estado Comercial',
        selection=[('DISPONIBLE', 'Disponible'), ('VENDIDO', 'Vendido')]
    )
    currency_id = fields.Many2one('res.currency',
        ondelete='set null', string="Moneda", index=True)
    price = fields.Monetary(string="Precio")
    m2_price = fields.Monetary(string="Precio M2")
    sale_date = fields.Date(
        string='Fecha de venta',
    )
    #   CONTRUCTION
    contract_modality = fields.Selection(
        string='Modalidad de contrato',
        selection=[('COMPROMISO', 'Compromiso'), ('CONTRATO', 'Contrato')]
    )
    occupied_area = fields.Float(
        string='Area Ocupada',
    )
    covered_area = fields.Float(
        string='Area Techada',
    )
    free_area = fields.Float(
        string='Area Libre',
    )
    #   DISTRIBUTION
    bedroom_number = fields.Integer(
        string='Cantidad de dormitorios',
    )
    
    bathroom_number = fields.Integer(
        string='Cantidad de baños',
    )
    building_view = fields.Char(string="Vista del Edificio", required=True, size=50)
    service_room = fields.Char(string="Cuarto de Servicio", required=True, size=20)
    
