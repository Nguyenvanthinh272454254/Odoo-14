# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Tags(models.Model):
    _name = 'tags'
    _description = 'tags'

    name = fields.Char()
    description = fields.Text()
