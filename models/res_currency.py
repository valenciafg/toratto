from odoo import models, fields, api


class ResCurrency(models.Model):
    _name = 'res.currency'
    _inherit = 'res.currency'
    _columns = {
        'long_name': fields.Char('Nombre Completo', size=64)
   }
    long_name = fields.Char(string='Nombre Completo')

