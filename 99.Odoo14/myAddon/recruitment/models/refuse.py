# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Refuse_Reasons(models.Model):
    _name = 'refuse'
    _description = 'refuse'

    name = fields.Char()
    description = fields.Text()
