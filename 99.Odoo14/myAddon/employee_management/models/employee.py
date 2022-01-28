# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError


class Employrr(models.Model):
    _name = 'employee'
    _description = 'Employee'

    name = fields.Char()
    address = fields.Text("Address")
    gender = fields.Selection(string='Gender', selection=[
                              ('male', 'Male'), ('female', 'Female')],)
    department_id = fields.Many2one(string='Depar', comodel_name='department')
    
    
    @api.depends('department_id') 
    def _domain_depart(self):
        # list_task=self.env['task.manager'].search([('employee_id','=',self.id)])
        # deparment_emp=self.department_id
        # res = []
        # for task in list_task:
        #     if task.department_id.id == deparment_emp.id:
        #         res.append(task.department_id.id)
        # return [('id','in',res)]

        for dm in self:
            if dm.department_id:
                # raise UserError(dm.department_id.id)
                partner_ids =dm.department_id
                partner_task_ids=(dm.env['task.manager'].search([('department_id', 'in', dm.department_id.ids)])).department_id
                return {'domain': {'department_id': [( partner_task_ids, 'in',partner_ids.ids)]}}
            else: return 

    # @api.onchange('department_id')
    # def onchange_department_id(self):
    #     for rec in self:
    #         return {'domain':{'department_id':[{'department_id','=',rec.department_id.id}]}}

    task_ids = fields.Many2many(
        string='Task',
        comodel_name='task.manager',
        column1='task_id',
        column2='employee_id',
        # domain=_domain_depart
        domain="[('department_id', '=', department_id),('employee_id','=',name)]" 
    )
    
    def custom_remove(self):
        for pet in self:
            pet.unlink()
        pass

