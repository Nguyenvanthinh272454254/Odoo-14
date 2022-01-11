# -*- coding: utf-8 -*-
# from odoo import http


# class MyPetPlus(http.Controller):
#     @http.route('/my_pet_plus/my_pet_plus/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_pet_plus/my_pet_plus/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_pet_plus.listing', {
#             'root': '/my_pet_plus/my_pet_plus',
#             'objects': http.request.env['my_pet_plus.my_pet_plus'].search([]),
#         })

#     @http.route('/my_pet_plus/my_pet_plus/objects/<model("my_pet_plus.my_pet_plus"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_pet_plus.object', {
#             'object': obj
#         })
