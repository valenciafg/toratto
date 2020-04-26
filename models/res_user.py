from odoo import models, fields, api

class Users(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    _columns = {
        'firma': fields.Binary('Firma', attachment=True)
    }


    firma = fields.Binary(string='Firma', attachment=True)
