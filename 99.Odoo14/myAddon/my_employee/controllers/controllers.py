# -*- coding: utf-8 -*-
# from odoo import http


# class MyEmployee(http.Controller):
#     @http.route('/my_employee/my_employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_employee/my_employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_employee.listing', {
#             'root': '/my_employee/my_employee',
#             'objects': http.request.env['my_employee.my_employee'].search([]),
#         })

#     @http.route('/my_employee/my_employee/objects/<model("my_employee.my_employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_employee.object', {
#             'object': obj
#         })
