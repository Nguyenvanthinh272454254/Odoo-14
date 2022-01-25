# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Jobpositions(models.Model):
    _name = 'jobpositions'
    _description = 'jobpositions'

    name = fields.Char()
    description = fields.Text()
