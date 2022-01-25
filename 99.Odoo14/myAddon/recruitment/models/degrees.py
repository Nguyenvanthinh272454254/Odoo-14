# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Degrees(models.Model):
    _name = 'degrees'
    _description = 'degrees'

    name = fields.Char()
    description = fields.Text()
