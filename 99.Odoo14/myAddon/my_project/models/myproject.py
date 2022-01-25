# -*- coding: utf-8 -*-

from odoo import models, fields, api


class my_project(models.Model):
    # _name= 'my.project'
    # _inherits = {'project.project': 'partner_id'}
    _inherit = 'project.project'


    
    
    # partner_id = fields.Many2one(
    #     string='Partner_id',
    #     comodel_name='project.project',
    #     auto_join=True, index=True, ondelete="cascade", required=True
    # )
    name = fields.Char()
    
    
class project_task(models.Model):
    # _name='my.project.task'
    # _inherits = {'project.task':'project_id'}
    
    _inherit = 'project.task'
    

    
    # project_id = fields.Many2one(
    #     string='Project id',
    #     comodel_name='project.task', auto_join=True, index=True, ondelete="cascade", required=True
    # )
    
    

    name = fields.Date()
    
class leader(models.Model):
    
    _name="leader"
    

    name = fields.Char(string="leader")

class viewer(models.Model):
    
    _name='viewer'
    

    name = fields.Char(string="viewer")
