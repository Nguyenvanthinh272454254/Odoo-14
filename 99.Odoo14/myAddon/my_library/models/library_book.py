# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import UserError,ValidationError
from odoo.tools.translate import _



class my_library(models.Model):
    _name = 'library.book'
    _description = 'Library Book'


    name = fields.Char('Title', required=True)
    state = fields.Selection(
        [('draft', 'Not Available'),
         ('available', 'Available'),
         ('lost', 'Lost')],
        'State', default="draft")
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')
 
    # Add a helper method to check whether a state transition is allowed
    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft', 'available'),
                   ('available', 'borrowed'),
                   ('borrowed', 'available'),
                   ('available', 'lost'),
                   ('borrowed', 'lost'),
                   ('lost', 'available')]
        return (old_state, new_state) in allowed


    # Add a method to change the state of some books to a new state that is passed as anargument
    def change_state(self, new_state):
        for book in self:
            if book.is_allowed_transition(book.state, new_state):
                book.state = new_state
            else:
                message = _('Moving from %s to %s is not allowd') % (book.state, new_state)
                raise UserError(message)
    

    # Add a method to change the book state by calling the change_state method:
    def make_available(self):
        self.change_state('available')

    def make_borrowed(self):
        self.change_state('borrowed')

    def make_lost(self):
        self.change_state('lost')

