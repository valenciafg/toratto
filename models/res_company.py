from odoo import models, fields, api, _



class company(models.Model):
    _inherit = 'res.company'
    _columns = {
        'watermark_image': fields.Binary(string='Watermark image'),

   }

    watermark_image  = fields.Binary(string='Watermark image')
