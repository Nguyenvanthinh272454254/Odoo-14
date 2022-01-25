# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ApplicationAll(models.Model):
    _name = 'applicationall'
    _description = 'ApplicationAll'

    name = fields.Char()
    description = fields.Text()
