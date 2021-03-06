# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Unit(models.Model):
    _name = 'unit.toratto'
    _description = 'Unidades'

    code = fields.Char(string="Código", required=True, size=15)
    name = fields.Char(string="Nombre", required=True, size=50)
    logo = fields.Binary(string='Logo', attachment=True)
    unit_type = fields.Many2one('unit.type.toratto',
        ondelete='set null', string="Tipo de Unidad", index=True)
    sub_division = fields.Char(string="Subdivisión", size=150)
    proyect_id = fields.Many2one('project.toratto',
        ondelete='set null', string="Proyecto", index=True)  
    floor_number = fields.Integer(
        string='Piso',
    )
    #   COMERCIAL
    st_commercial = fields.Selection([
                ('DISPONIBLE', 'Disponible'),
                ('VENDIDO', 'Vendido'),
                ('SEPARADO', 'Separado'),
                ], string='Estado Comercial', default='DISPONIBLE'
    )
    currency_id = fields.Many2one('res.currency',
        ondelete='set null', string="Moneda", index=True)
    price = fields.Monetary(string="Precio de Ventas")
    discount = fields.Monetary(string="Descuento Especial")
    m2_price = fields.Monetary(string="Precio M2")
    sale_date = fields.Date(
        string='Fecha de venta',
    )
    tea = fields.Char(
        string='Tasa Efectiva Anual %', required=True, size=50
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
    building_view = fields.Char(string="Vista del Departamento", required=True, size=50)
    service_room = fields.Char(string="Cuarto de Servicio", required=True, size=20)
    plans = fields.Many2one('plans.toratto',
        string="Plano")
    
    @api.model
    def get_import_templates(self):
        return [{
            'label': ('Importar Unidades'),
            'template': '/toratto/static/xls/unit.toratto.xlsx'
        }]

