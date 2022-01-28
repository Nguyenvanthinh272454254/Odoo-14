# -*- coding: utf-8 -*-

from odoo import models, fields, api


class imformation(models.Model):
    
    _inherit = 'res.users'
    age = fields.Integer(
        string='Age employee',
    )
    