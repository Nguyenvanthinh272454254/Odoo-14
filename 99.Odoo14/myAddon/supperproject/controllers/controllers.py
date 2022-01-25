# -*- coding: utf-8 -*-
# from odoo import http


# class Supperproject(http.Controller):
#     @http.route('/supperproject/supperproject/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/supperproject/supperproject/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('supperproject.listing', {
#             'root': '/supperproject/supperproject',
#             'objects': http.request.env['supperproject.supperproject'].search([]),
#         })

#     @http.route('/supperproject/supperproject/objects/<model("supperproject.supperproject"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('supperproject.object', {
#             'object': obj
#         })
