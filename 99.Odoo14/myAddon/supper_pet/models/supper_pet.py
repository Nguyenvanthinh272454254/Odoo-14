from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class MyPet(models.Model):
    _name = "supper.pet"
    _description = "supper"
    _inherits = {'my.pet': 'my_pet_id'}
    # _inherit = "my.pet" # <- inherit fields and methods from model "my.pet"

    # add new field
    is_supper_strength = fields.Boolean("Is Super Strength", default=False)
    is_fly = fields.Boolean("Is_fly", default=False)
    planet = fields.Char("Planet")
    my_pet_id = fields.Many2one(
        'my.pet', 'Product Template',
        auto_join=True, index=True, ondelete="cascade", required=True)
    
    # avoid error: TypeError: Many2many fields super.pet.product_ids and my.pet.product_ids use the same table and columns

