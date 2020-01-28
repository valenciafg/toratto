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
import logging
from PIL import Image
import requests
import pytesseract
from bs4 import BeautifulSoup
try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3
from lxml import etree
from odoo.exceptions import Warning

import requests

def get_data_doc_number(tipo_doc, numero_doc, format='json'):
    user, password = 'demorest', 'demo1234'
    url = 'http://py-devs.com/api'
    url = '%s/%s/%s' % (url, tipo_doc, str(numero_doc))
    print(url)
    res = {'error': True, 'message': None, 'data': {}}
    try:
        response = requests.get(url, auth=(user, password))
    except requests.exceptions.ConnectionError as e:
        res['message'] = 'Error en la conexion'
        return res

    if response.status_code == 200:
        res['error'] = False
        print(response.json())
        res['data'] = response.json()
    else:
        try:
            res['message'] = response.json()['detail']
        except Exception as e:
            res['error'] = True
    return res


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

#    registration_name = fields.Char('Registration Name', size=128, index=True, )
 #   catalog_06_id = fields.Many2one('einvoice.catalog.06','Tipo Doc.', index=True)
  #  state = fields.Selection([('habido','Habido'),('nhabido','No Habido')],'State')
    """
    def _get_captcha(self, type):
        s = requests.Session() 
        if type.upper() == 'R':
            try:
                r = s.get('http://www.sunat.gob.pe/cl-ti-itmrconsruc/captcha?accion=image')
            except s.exceptions.RequestException as e:
                return (False,e)
            img=Image.open(StringIO.StringIO(r.content))
            captcha_val=pytesseract.image_to_string(img)
            captcha_val=captcha_val.strip().upper()
            return (s, captcha_val)
        elif type.upper() == 'D':
            try:
                r = s.get('https://cel.reniec.gob.pe/valreg/codigo.do')
            except s.exceptions.RequestException as e:
                return (False,e)
            img=Image.open(StringIO.StringIO(r.content))
            img = img.convert("RGBA")
            pixdata = img.load()
            for y in xrange(img.size[1]):
                for x in xrange(img.size[0]):
                    red, green, blue, alpha=pixdata[x, y]
                    if blue<100:
                        pixdata[x, y] = (255, 255, 255, 255)
            temp_captcha_val=pytesseract.image_to_string(img)
            temp_captcha_val=temp_captcha_val.strip().upper()
            captcha_val=''
            for i in range(len(temp_captcha_val)):
                if temp_captcha_val[i].isalpha() or temp_captcha_val[i].isdigit():
                    captcha_val=captcha_val+temp_captcha_val[i]
            return (s, captcha_val.upper())
            

    def vat_change(self, vat):
        if not vat:
            return False
        vat=vat[2:]
        validate = self.check_vat_pe(vat)
        vat_type,vat = vat and len(vat)>=2 and (vat[0], vat[1:]) or (False, False)
        res={}
        if vat_type and vat_type.upper() == 'D':
            if len(vat)==8:
                for i in range(10):
                    consuta, captcha_val= self._get_captcha(vat_type.upper())
                    if not consuta:
                        res['warning'] = {}
                        res['warning']['title'] = _('Connection error')
                        res['warning']['message'] = _('The server is not available! try again!')
                        return res
                    if len(captcha_val)==4:
                        break
                payload={'accion': 'buscar', 'nuDni': vat, 'imagen': captcha_val}
                post = consuta.post("https://cel.reniec.gob.pe/valreg/valreg.do", params=payload)
                texto_consulta=post.text
                parser = etree.HTMLParser()
                tree   = etree.parse(StringIO.StringIO(texto_consulta), parser)
                res= {}
                name=''
                for _td in tree.findall("//td[@class='style2']"):
                    if _td.text:
                        _name=_td.text.split("\n")
                        for i in range(len(_name)):
                            _name[i]=_name[i].strip()
                        name=' '.join(_name)
                        break
                error_captcha="Ingrese el código que aparece en la imagen"
                error_dni="El DNI N°"
                if error_captcha==name.strip().encode('utf-8'):
                    return self.vat_change(vat)
                elif error_dni==name.strip().encode('utf-8'):
                    return osv.except_osv(
                        _('Error'),
                        _('the DNI entered is incorrect')) 
                res['name'] = name.strip()
                return {'value': res}
            elif vat_type and vat_type.upper() == 'R':
                factor = '5432765432'
                sum = 0
                dig_check = False
                if len(vat) != 11:
                    return False
                try:
                    int(vat)
                except ValueError:
                    return False 
                             
                for f in range(0,10):
                    sum += int(factor[f]) * int(vat[f])
                    
                subtraction = 11 - (sum % 11)
                if subtraction == 10:
                    dig_check = 0
                elif subtraction == 11:
                    dig_check = 1
                else:
                    dig_check = subtraction
                
                if not int(vat[10]) == dig_check:
                    raise osv.except_osv(
                        _('Error'),
                        _('the RUC entered is incorrect')) 
                for i in range(10):
                    consuta, captcha_val= self._get_captcha(vat_type.upper())
                    if not consuta:
                        res['warning'] = {}
                        res['warning']['title'] = _('Connection error')
                        res['warning']['message'] = _('The server is not available! try again!')
                        return res
                    if captcha_val.isalpha():
                        break
                get=consuta.get("http://www.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias?accion=consPorRuc&razSoc="+
                                "&nroRuc="+vat+"&nrodoc=&contexto=rrrrrrr&tQuery=on&search1="+vat+
                                "&codigo="+captcha_val+"&tipdoc=1&search2=&coddpto=&codprov=&coddist=&search3=")
                texto_error='Surgieron problemas al procesar la consulta'
                texto_consulta=get.text
                print(texto_consulta)
                #busqueda_error=texto_consulta.find(texto_error)
                if texto_error in (texto_consulta):
                    raise osv.except_osv(
                        _('Error'),
                        _('Consulte nuevamente'))
                else:
                    #consulta(ruc)
                    texto_consulta=StringIO.StringIO(texto_consulta).readlines()

                    temp=0;
                    tnombre=False
                    tdireccion=False

                    for li in texto_consulta:
                        if temp==1:
                            soup = BeautifulSoup(li)
                            tdireccion= soup.td.string
                            #tdireccion=tdireccion.string

                            break
                    
                        if li.find("Domicilio Fiscal:") != -1:
                            temp=1
                    #print texto_consulta
                    for li in texto_consulta:
                        if li.find("desRuc") != -1:
                            soup = BeautifulSoup(li)
                            tnombre=soup.input['value']

                            break 
                    #raise osv.except_osv(
                    #    _(tnombre),
                    #    _(tdireccion))
                
                    return {
                        'value': {'name': tnombre,'street': tdireccion, 'vat_subjected': True}
                    }
        else:
            return False
    """
   # @api.onchange('catalog_06_id','vat')
    def vat_change(self):
        self.update_document()
        
    def update_document(self):
        print("*****update_document******")
        if not self.vat:
            return False
        print(self.catalog_06_id.code)
        print(self.catalog_06_id.name)
        print(self.vat)
        if self.catalog_06_id and self.catalog_06_id.name == 'DNI':
           #Valida DNI
            if self.vat and len(self.vat) != 8:
                raise Warning('El Dni debe tener 8 caracteres')
            else:
                d = get_data_doc_number(
                    'dni', self.vat, format='json')
                if not d['error']:
                    d = d['data']
                    self.name = '%s %s %s' % (d['nombres'],
                                               d['ape_paterno'],
                                               d['ape_materno'])

        elif self.catalog_06_id and self.catalog_06_id.name == 'RUC':
            # Valida RUC
            if self.vat and len(self.vat) != 11:
                raise Warning('El Ruc debe tener 11 caracteres')
            else:
                d = get_data_doc_number(
                    'ruc', self.vat, format='json')
                if d['error']:
                    print("???")
                    return True
                d = d['data']
                """
                #~ Busca el distrito
                ditrict_obj = self.env['res.country.state']
                prov_ids = ditrict_obj.search([('name', '=', d['provincia']),
                                               ('province_id', '=', False),
                                               ('state_id', '!=', False)])
                dist_id = ditrict_obj.search([('name', '=', d['distrito']),
                                              ('province_id', '!=', False),
                                              ('state_id', '!=', False),
                                              ('province_id', 'in', [x.id for x in prov_ids])], limit=1)
                if dist_id:
                    self.district_id = dist_id.id
                    self.province_id = dist_id.province_id.id
                    self.state_id = dist_id.state_id.id
                    self.country_id = dist_id.country_id.id
                """
                # Si es HABIDO, caso contrario es NO HABIDO
                tstate = d['condicion_contribuyente']
                if tstate == 'HABIDO':
                    tstate = 'habido'
                else:
                    tstate = 'nhabido'
                self.state = tstate
            
                self.name = d['nombre_comercial'] != '-' and d['nombre_comercial'] or d['nombre']
                #self.registration_name = d['nombre']
                self.street = d['domicilio_fiscal']
                self.vat_subjected = True
                self.is_company = True
        else:
            True

