# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class salary(models.Model):
    _name = "intrutor"
    _inherits = {'employee': 'intrutor_id'}

    name = fields.Char(string='Title', required=True)
    description = fields.Text('Desription')

    state_date = fields.Date(default=fields.Date.today())
    duration = fields.Float(digits=(16, 2), help="Duration in days",)
    seats = fields.Integer(string="Number of seats")

    taken_seats = fields.Float(string='Taken_seats',compute='_taken_seats')
    ex_price = fields.Float(string="price sliver")

    field_name_ids = fields.Many2many(
        string='Attendee',
        comodel_name='employee',
        column1='task_id',
        column2='instrutor_id',
    )

    state = fields.Selection([
        ('draft', 'Not Confirmed'),
        ('done', 'Confirmed'),
    ], string='Status', index=True, readonly=True, copy=False, default='draft')

    _sql_constraints = [
        (
            'name_descriptions_check',
            'Check(name != description)',
            'the title of the course should not be the description'
        ),
        ('name_unique',
            'UNIQUE(name)',
            'The course title must be unique'
         )
    ]

    intrutor_id = fields.Many2one(
        'employee', 'Intructor',
        auto_join=True, index=True, ondelete="cascade", required=True)

    def custom_remove(self):
        for pet in self:
            pet.unlink()
        pass

    @api.constrains('field_name_ids', 'intrutor_id')
    def _check_(self):
        for record in self:
            # if Many2one in many2any => fasle
            if record.intrutor_id and record.intrutor_id in record.field_name_ids:
                raise UserError("false")

    @api.depends('seats', 'ex_price')
    def _taken_seats(self):
        for i in self:
            if not i.seats:
                i.taken_seats = 0.0
            else:
                i.taken_seats = 50.0 + (i.ex_price/i.seats)
