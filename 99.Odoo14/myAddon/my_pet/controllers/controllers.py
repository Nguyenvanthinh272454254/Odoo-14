# -*- coding: utf-8 -*-
# from odoo import http


# class MyPet(http.Controller):
#     @http.route('/my_pet/my_pet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_pet/my_pet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_pet.listing', {
#             'root': '/my_pet/my_pet',
#             'objects': http.request.env['my_pet.my_pet'].search([]),
#         })

#     @http.route('/my_pet/my_pet/objects/<model("my_pet.my_pet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_pet.object', {
#             'object': obj
#         })
