# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    ESTADO_COMERCIAL = [
        ('DISPONIBLE', 'Disponible'),
        ('VENDIDO', 'Vendido'),
        ('SEPARADO', 'Separado')
    ]
    #required=True,
    code = fields.Char(string="Código", size=15)
    unit_number = fields.Char(
        string='Numero de Unidad',
    )
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
        ESTADO_COMERCIAL,
        string='Estado Comercial',
        index=True,
        default='DISPONIBLE',
    )
    currency_id = fields.Many2one('res.currency',
        ondelete='set null', string="Moneda", index=True)
    price = fields.Monetary(string="Precio de Venta")
    discount = fields.Monetary(string="Descuento Especial")
    funders = fields.Many2one('res.partner.bank', string="N° Cuenta Bancaria Asociada")
    #amount_of_separation = fields.Monetary(string="Monto de Separacion")
    #initial_fee = fields.Float(string='Cuota Inicial (%)', default=10.0)
    m2_price = fields.Monetary(string="Precio M2")
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
    parent_id = fields.Many2one('res.partner', string="Cliente Interesado")
    owner_id = fields.Many2one('res.partner', string="Asesor Bancario")


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

