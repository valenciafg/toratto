# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2009-TODAY Odoo Peru(<http://www.odooperu.pe>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from odoo import models, fields, api
try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3
from odoo.exceptions import Warning
import http.client
import json


def get_data_doc_number(tipo_doc, numero_doc, format='json'):
    conn = http.client.HTTPSConnection('api.migoperu.pe')
    headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json'
    }
    token_code = 'f877da41-3a1e-4b87-a58b-8a4d92c8926d-6e1634f5-0cab-4156-977a-1072f49a2d1e'
    if tipo_doc == "ruc":
        post_body = {
        'token': token_code,
        'ruc': numero_doc
        }
        api_end_point = "/api/v1/ruc"
    else:
        post_body = {
        'token': token_code,
        'dni': numero_doc
        }
        api_end_point = "/api/v1/dni"
    json_data = json.dumps(post_body)
    conn.request('POST', api_end_point, json_data, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    print(response.status, response.reason)
    res = {'error': True, 'message': None, 'data': {}}
    if response.status == 200:
        res['error'] = False
        print(data)
        print(data.decode())
        res['data'] = json.loads(data.decode())
    else:
        res['error'] = True
        res['message'] = "No se obtuvo informacion del documento solicitado"
    return res


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    #registration_name = fields.Char('Registration Name', size=128)
    #catalog_06_id = fields.Many2one('einvoice.catalog.06','Tipo Doc.', index=True)
    #state = fields.Selection([('habido','Habido'),('nhabido','No Habido')],'State')
    @api.onchange('l10n_latam_identification_type_id','vat')
    def vat_change(self):
        self.update_document()
        
    def update_document(self):
        if not self.vat:
            return False
        """
        #print(self.l10n_pe_vat_code.l10n_pe_vat_code)
        #print(self.l10n_pe_vat_code.name)
        print(self.l10n_latam_identification_type_id.id)
        print(self.l10n_latam_identification_type_id.name)
        print(self.vat)
        tipo_doc_name = self.l10n_latam_identification_type_id.name
        tipo_doc_id = self.l10n_latam_identification_type_id.id
        nro_doc = self.vat
        """
        if self.l10n_latam_identification_type_id and self.l10n_latam_identification_type_id.name == 'RUC':
            # Valida RUC
            if self.vat and len(self.vat) != 11:
                raise Warning('El Ruc debe tener 11 caracteres')
            else:
                d = get_data_doc_number(
                    'ruc', self.vat, format='json')
                print(d)
                #print(type(d))
                if d['error']:
                    return True
                d = d['data']                
                self.name = d['nombre_o_razon_social']
                self.street = d['direccion']
                self.vat_subjected = True
                self.is_company = True
        if self.l10n_latam_identification_type_id and self.l10n_latam_identification_type_id.name == 'DNI':
            if self.vat and len(self.vat) < 8:
                raise Warning('El DNI debe tener al menos 8 caracteres')
            else:
                d = get_data_doc_number(
                        'dni', self.vat, format='json')
                print(d)
                if d['error']:
                    return True
                d = d['data']
                self.name = d['nombre']
        return True

