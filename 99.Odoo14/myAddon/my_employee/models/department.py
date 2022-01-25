
from odoo import models, fields, api

class department(models.Model):
    _inherit = 'hr.department'

    datecreated = fields.Date(string="Date created")

