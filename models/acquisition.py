# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Acquisition(models.Model):
    _name = 'acquisition.toratto'
    _description = 'Adquisiciones'

    name = fields.Char(string="Nombre", required=True, size=50)
    proforma = fields.Many2one('sale.order', string="Proforma", required=True, size=200)
    unit = fields.Many2one('unit.toratto',
        ondelete='set null', string="Unidad", index=True)
    st_commercial = fields.Selection([
		('Proceso de Separacion', 'Proceso de Separacion'),
		('Separado', 'Separado'),
		('Proceso de Venta', 'Proceso de Venta'),
		('Proceso de Anulacion', 'Proceso de Anulacion'),
		('Vendido', 'Vendido'),
		], string='Estado Comercial')

    client = fields.Many2one('res.partner', string="Clientes", required=True, size=200)
    user = fields.Many2one('res.partner', string="Usuario", required=True, size=200)
    quantity_unit = fields.Integer(string="Cant. Unidades")
    financing = fields.Selection([
                ('Hipotecario', 'Hipotecario'),
                ('Ahorro', 'Ahorro'),
                ('Contado', 'Contado'),
                ('Credito Grupo Toratto', 'Credito Grupo Toratto'),
                ], string='Financiamiento')

    separation_date = fields.Date(
        string='Fecha de Separacion',
        default=fields.Date.context_today,
    )

    sale_start_date = fields.Date(
        string='Fecha de inicio de venta',
        default=fields.Date.context_today,
    )
    approval_date = fields.Date(
        string='Fecha de Aprobacion Bancaria',
        default=fields.Date.context_today,
    )

    currency_id = fields.Many2one('res.currency',
        ondelete='set null', string="Moneda", index=True)
    total_cost = fields.Monetary(string="Monto Total de Venta")
    pending_payments = fields.Monetary(string="Pago Pendiente")
    made_payments = fields.Monetary(string="Pago Realizado")
    description = fields.Text(string="Observación")
