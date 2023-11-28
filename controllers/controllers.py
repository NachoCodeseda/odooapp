# -*- coding: utf-8 -*-
# from odoo import http


# class AureaticAppTransporte3(http.Controller):
#     @http.route('/aureatic_app_transporte3/aureatic_app_transporte3', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aureatic_app_transporte3/aureatic_app_transporte3/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('aureatic_app_transporte3.listing', {
#             'root': '/aureatic_app_transporte3/aureatic_app_transporte3',
#             'objects': http.request.env['aureatic_app_transporte3.aureatic_app_transporte3'].search([]),
#         })

#     @http.route('/aureatic_app_transporte3/aureatic_app_transporte3/objects/<model("aureatic_app_transporte3.aureatic_app_transporte3"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aureatic_app_transporte3.object', {
#             'object': obj
#         })
