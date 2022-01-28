# -*- coding: utf-8 -*-
# from odoo import http


# class SupperPet(http.Controller):
#     @http.route('/supper_pet/supper_pet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/supper_pet/supper_pet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('supper_pet.listing', {
#             'root': '/supper_pet/supper_pet',
#             'objects': http.request.env['supper_pet.supper_pet'].search([]),
#         })

#     @http.route('/supper_pet/supper_pet/objects/<model("supper_pet.supper_pet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('supper_pet.object', {
#             'object': obj
#         })
