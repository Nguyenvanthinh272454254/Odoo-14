# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Activity(models.Model):
    _name = 'activity'
    _description = 'activity'

    name = fields.Char()
    description = fields.Text()
