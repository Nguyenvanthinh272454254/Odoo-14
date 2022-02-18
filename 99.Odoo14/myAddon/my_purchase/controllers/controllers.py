# -*- coding: utf-8 -*-
# from odoo import http


# class MyPurchase(http.Controller):
#     @http.route('/my_purchase/my_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_purchase/my_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_purchase.listing', {
#             'root': '/my_purchase/my_purchase',
#             'objects': http.request.env['my_purchase.my_purchase'].search([]),
#         })

#     @http.route('/my_purchase/my_purchase/objects/<model("my_purchase.my_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_purchase.object', {
#             'object': obj
#         })
