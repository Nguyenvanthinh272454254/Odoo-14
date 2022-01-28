from odoo import models, fields, api


class Department(models.Model):
    _name = 'department'
    _description = 'Department'

    name = fields.Char()

    def custom_remove(self):
        for pet in self:
            pet.unlink()
        pass    
    
    

   
    