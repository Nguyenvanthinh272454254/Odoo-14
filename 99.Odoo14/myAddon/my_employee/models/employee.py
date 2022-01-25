# -*- coding: utf-8 -*-

from odoo import models, fields, api


class my_employee(models.Model):
    _inherit = 'hr.employee'

    grandparents=fields.Char(string="grandparents")
    grandfather = fields.Char(string="Grandfather")
    grandma = fields.Char(string="Grandma")
    address = fields.Char(string="address")
    

    
    
    
    
    

    
        
    
