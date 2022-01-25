# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Setting(models.Model):
    _name = 'setting'
    _description = 'setting'

    name = fields.Char()
    description = fields.Text()
