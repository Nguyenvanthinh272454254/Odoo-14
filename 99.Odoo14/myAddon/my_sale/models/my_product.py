# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api


class my_sale(models.Model):
    _inherit ='sale.order'

class sale_orders_line(models.Model):
    _inherit ='sale.order.line'

    length = fields.Float(string="L", default=0.0)
    weight = fields.Float(string="W",default=0.0)
    height = fields.Float(string="H",default=0.0)

    shippingcost=fields.Float(string="SHIPPING COST",default=13998)
    pallets=fields.Float(string="PALLETS", default=250)
    deposit_paid=fields.Float(string="DEPOSIT PAID 30%",default=1)

    # @api.depends('deposit_paid,')
    # def BALANCE_DUE(self):
    #     for record in self:
    #         record.field = sdsa

    
        
class my_produc(models.Model):
    
    _inherit ='product.product'
           