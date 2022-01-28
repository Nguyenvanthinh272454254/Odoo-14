# -*- coding: utf-8 -*-
# from odoo import http


# class EmployManager(http.Controller):
#     @http.route('/employ__manager/employ__manager/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employ__manager/employ__manager/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employ__manager.listing', {
#             'root': '/employ__manager/employ__manager',
#             'objects': http.request.env['employ__manager.employ__manager'].search([]),
#         })

#     @http.route('/employ__manager/employ__manager/objects/<model("employ__manager.employ__manager"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employ__manager.object', {
#             'object': obj
#         })
