# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Job(models.Model):
    _name='job'
    _inherits = {'hr.job':'user_id'}
    

    user_id = fields.Many2one('hr.job', 'Job',
        auto_join=True, index=True, ondelete="cascade", required=True)

    
    name = fields.Char()
    description = fields.Text()
