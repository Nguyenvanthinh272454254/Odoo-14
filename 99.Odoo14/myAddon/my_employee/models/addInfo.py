from odoo import models, fields, api
from odoo.exceptions import UserError



class addinfo(models.Model):
    _name = 'addinfo'

    
    user_id = fields.Many2one(
        string='employee',
        comodel_name='hr.employee',
    )
    department_id = fields.Many2one(
        string='employee',
        comodel_name='hr.department',
    )

    
    Seniority = fields.Float('Seniority')
    bonus_price = fields.Float("Bonus Price", default=0)
    DateWork = fields.Float("Final Price",)
    salary = fields.Float('Salary',compute='_compute_final_price')

   
    def _compute_final_price(record):
        for record in self:
            if record.Seniority <0:
                raise UserError('Wrong roi')
            if record.Seniority > 1 and record.Seniority <5:
                record.salary = (record.bonus_price) + record.DateWork*1500
            if record.Seniority > 5:
                record.salary = (record.bonus_price) + record.DateWork*2500
   


