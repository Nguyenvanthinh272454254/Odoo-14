# -*- coding: utf-8 -*-

from odoo import models, fields, api


class reportingAnays(models.Model):
    _name = 'reportinganalys'
    _description = 'reportingAnays'

    name = fields.Char()
    description = fields.Text()
