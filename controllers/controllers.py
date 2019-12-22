# -*- coding: utf-8 -*-
# from odoo import http


# class Toratto(http.Controller):
#     @http.route('/toratto/toratto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/toratto/toratto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('toratto.listing', {
#             'root': '/toratto/toratto',
#             'objects': http.request.env['toratto.toratto'].search([]),
#         })

#     @http.route('/toratto/toratto/objects/<model("toratto.toratto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('toratto.object', {
#             'object': obj
#         })
