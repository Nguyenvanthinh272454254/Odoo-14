# -*- coding: utf-8 -*-

from odoo import models, fields, api


class updatereport(models.Model):
    _inherit ='hr.employee'
    
    grandma = fields.Char(string="Grandma")
    address = fields.Char(string="address")
    category_ids = fields.Many2many('hr.employee', string="Tags")

# class my_company(object):
#     _inherit ='res.company'       

    