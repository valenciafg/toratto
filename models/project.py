# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    _name = 'project.toratto'
    _description = 'Proyectos de construccion'

#    @api.onchange('country_id')
 #   def _onchange_country_id(self):
  #      for rec in self:
   #         return {
    #            'domain': {
     #               'department_id': [('country_id', '=', rec.country_id.id)]
      #          }
       #     }

   # @api.onchange('department_id')
   # def _onchange_department_id(self):
    #    for rec in self:
     #       return {
      #          'domain': {
       #             'province_id': [
        #                ('country_id', '=', rec.country_id.id),
         #               ('department_id', '=', rec.department_id.id)
          #          ]
           #     }
           # }

   # @api.onchange('province_id')
   # def _onchange_province_id(self):
    #    for rec in self:
     #       return {
      #          'domain': {
       #             'district_id': [
        #                ('country_id', '=', rec.country_id.id),
         #               ('department_id', '=', rec.department_id.id),
          #              ('province_id', '=', rec.province_id.id)
           #         ]
            #    }
           # }

    code = fields.Char(string="Código", required=True, size=15)
    name = fields.Char(string="Nombre", required=True, size=50)
    logo = fields.Binary(string='Imagen Fachada', attachment=True)
    logo2 = fields.Binary(string='Logo del Proyecto', attachment=True)
    currency_id = fields.Many2one('res.currency',
        ondelete='set null', string="Moneda", index=True)
   # building_type_id = fields.Many2one('building.type.toratto',
        #ondelete='set null', string="Tipo de Edificación", index=True)
    sale_start_date = fields.Date(
        string='Fecha de inicio de venta',
        default=fields.Date.context_today,
    )    
    bank = fields.Many2one('res.bank', string="Entidad Bancaria")
    amount_of_letter_separation = fields.Monetary(string="Monto de separación de letra")
    project_type_id = fields.Many2one('project.type.toratto',
        ondelete='set null', string="Tipo de Proyecto", index=True)
    owner_id = fields.Many2one('res.partner',
        ondelete='set null', string="Propietario", index=True)
    total_cost = fields.Monetary(string="Costo total")
    amount_of_separacion = fields.Monetary(string="Monto de separación")
    type_of_bank_account = fields.Char(string="Tipo de cuenta bancaria", size=100)
    number_of_floors = fields.Integer(string="Número de pisos")
    number_of_unit = fields.Integer(string="Número de Unidades")
    description = fields.Text(string="Descripción")
    #construction_dt_start = fields.Date.today()
    contact_id = fields.Many2one('res.partner',
        ondelete='set null', string="Contacto", index=True)
    work_progress = fields.Float(
        string='Avence de obra',
        digits=(3,2)
    )
    real_project_delivery_date = fields.Date(
        string='Fecha real de entrega de proyecto'
    )
    estimate_project_delivery_date = fields.Date(
        string='Fecha estimada de entrega de proyecto'
    )
    construction_state_id = fields.Many2one('construction_state.toratto',
        ondelete='set null', string="Estado de construccion", index=True)
    #LOCATION
    country_id = fields.Many2one('res.country',
        ondelete='set null', string="País", index=True)
    department_id = fields.Many2one('res.city',
        ondelete='set null', string="Departamento", index=True)
    province_id = fields.Many2one('res.city',
        ondelete='set null', string="Provincia", index=True)
    district_id = fields.Many2one('district.toratto',
        ondelete='set null', string="Distrito", index=True)
    address = fields.Text(string="Dirección")

    # Advanced Data
    limit_discount_30_initial = fields.Char(string='Limite Descuanto 30 Inicial')
    limit_discount_60_initial = fields.Char(string='Limite Descuanto 60 Inicial')
    limit_discount_seving_four_month = fields.Char(string='Limite Descuanto Ahorro 4 Meses')
    limit_discount_seving_six_month = fields.Char(string='Limite Descuanto Ahorro 6 Meses')
    limit_discount_seving_nine_month = fields.Char(string='Limite Descuanto Ahorro 9 Meses')
    licence_construction = fields.Char(string='Licencia de Construcción')
    developer = fields.Many2one('res.partner',
        ondelete='set null', string="Promotor Inmobiliario", index=True)
    funders_id = fields.Many2one('res.partner.bank', string="N° Cuenta Bancaria Asociada")

