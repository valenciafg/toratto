# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    #required=True,
    code = fields.Char(string="Código", size=15)
    unit_type = fields.Many2one('unit.type.toratto',
        ondelete='set null', string="Tipo de Unidad", index=True)
    sub_division = fields.Char(string="Subdivisión", size=150)
    proyect_id = fields.Many2one('project.toratto',
        ondelete='set null', string="Proyecto", index=True)  
    floor_number = fields.Integer(
        string='Piso',
    )
    #   COMERCIAL
    st_commercial = fields.Selection(
        string='Estado Comercial',
        selection=[('DISPONIBLE', 'Disponible'), ('VENDIDO', 'Vendido'), ('SEPARADO', 'Separado')]
    )
    currency_id = fields.Many2one('res.currency',
        ondelete='set null', string="Moneda", index=True)
    price = fields.Monetary(string="Precio de Venta")
    discount = fields.Float(string="Descuento (%)", digits='Descuento', default=0.0)
    amount_of_separation = fields.Float(string="Monto de Separacion", digits='Monto de Separacion', default=0.0)
    m2_price = fields.Float(string="Precio M2", default=0.0)
    sale_date = fields.Date(
        string='Fecha de venta',
    )
    tea = fields.Char(
        string='Tasa Efectiva Anual %', default=0.0
    )
    contract_modality = fields.Selection(
        string='Modalidad de contrato',
        selection=[('COMPROMISO', 'Compromiso'), ('CONTRATO', 'Contrato')]
    )
    funder_type_id = fields.Many2one('funder.type.toratto',
        ondelete='set null', string="Tipo de Financiamiento", index=True)
    parent_id = fields.Many2one('res.partner',
        ondelete='set null', string="Cliente Interesado", index=True)

    #   CONTRUCTION
    occupied_area = fields.Float(
        string='Area Ocupada m2',
    )
    covered_area = fields.Float(
        string='Area Techada m2',
    )
    free_area = fields.Float(
        string='Area Libre m2',
    )
    #   DISTRIBUTION
    bedroom_number = fields.Integer(
        string='Cantidad de dormitorios',
    )
    
    bathroom_number = fields.Integer(
        string='Cantidad de baños',
    )
    building_view = fields.Char(string="Vista del Departamento", size=50)
    service_room = fields.Char(string="Cuarto de Servicio", size=20)
    plans = fields.Many2one('plans.toratto',
        string="Plano")

