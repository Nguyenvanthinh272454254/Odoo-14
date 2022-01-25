# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Department(models.Model):
    _name = 'deprtment'
    _description = 'department'

    name = fields.Char()
    description = fields.Text()
