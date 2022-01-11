# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
from odoo.exceptions import UserError


class task_manager(models.Model):
    _name = 'task.manager'
    _description = 'task.manager'

    name = fields.Char("name", required=True)
    
    deadline = fields.Date(string='Deadline')

    
    employee_id = fields.Many2one(string='Employee', comodel_name='employee', )
    

    
    @api.constrains('deadline')
    def _check_Deadline(self):
        today = date.today()
        if self.deadline < today:
            raise UserError('Wrong day')


  
