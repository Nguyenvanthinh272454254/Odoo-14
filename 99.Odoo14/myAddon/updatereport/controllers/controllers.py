# -*- coding: utf-8 -*-
# from odoo import http


# class Updatereport(http.Controller):
#     @http.route('/updatereport/updatereport/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/updatereport/updatereport/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('updatereport.listing', {
#             'root': '/updatereport/updatereport',
#             'objects': http.request.env['updatereport.updatereport'].search([]),
#         })

#     @http.route('/updatereport/updatereport/objects/<model("updatereport.updatereport"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('updatereport.object', {
#             'object': obj
#         })
