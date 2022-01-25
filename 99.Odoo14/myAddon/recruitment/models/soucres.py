# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Soucres(models.Model):
    _name = 'sources'
    _description = 'sources'

    name = fields.Char()
    description = fields.Text()
