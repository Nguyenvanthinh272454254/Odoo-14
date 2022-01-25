from odoo import models, fields, api


class headquarter(models.Model):
    _name = 'headquarter'
    _description = 'headquarter'

    name = fields.Char()
    
    parent_id = fields.Many2one(
        string='parent',
        comodel_name='headquarter',
    )
    

    def custom_remove(self):
        for pet in self:
            pet.unlink()
        pass    
    
    

   
    