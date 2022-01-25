# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ApplicationJob(models.Model):
    _name = 'applicationjob'
    _description = 'ApplicationJob'

    name = fields.Char()
    description = fields.Text()
