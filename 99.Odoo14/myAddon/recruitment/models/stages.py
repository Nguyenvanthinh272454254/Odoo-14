# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Stages(models.Model):
    _name = 'stages'
    _description = 'stages'

    name = fields.Char()
    description = fields.Text()
