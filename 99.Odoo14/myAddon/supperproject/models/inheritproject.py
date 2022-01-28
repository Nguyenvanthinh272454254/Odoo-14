# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api


class supperproject(models.Model):
    _name = 'my.project'
    _description = 'my project'

    name=fields.Char('name')
    
    parent_id = fields.Many2one(
        string='parent',
        comodel_name='my.project',
    )
    
    task_ids = fields.Many2many(
        string='task',
        comodel_name='my.task',
    )
    
    

class supperprojecttask(models.Model):
    _name = 'my.task'
    _description = 'my task'

    name=fields.Char('name')
    
    project_id = fields.Many2one(
        string='Name Project',
        comodel_name='my.project',
    )
    assign_to = fields.Many2one(
        string='Assign to',
        comodel_name='res.users',
       
    )
    follower_user_ids = fields.Many2many(
        string='Follower',
        comodel_name='res.users',
    )
    is_public = fields.Boolean(groups='my_project.group_my_supperviewer_rule')

    active= fields.Boolean()
    deadline= fields.Date(string='Deadlinee')
    datecreate= fields.Date(string='datecreate')
    manager=fields.Char(string="Manager")
    state = fields.Selection([
        ('Prioritize LV1', 'Prioritize LV1'),
        ('Prioritize LV2', 'Prioritize LV2'),
        ('Prioritize LV3', 'Prioritize LV3'),
        ('Prioritize LV4', 'Prioritize LV4'),
        ('Prioritize LV5', 'Prioritize LV5'),
        ('Prioritize LV6', 'Prioritize LV6'),
        ], string="IPrioritize",
        required=True,)

