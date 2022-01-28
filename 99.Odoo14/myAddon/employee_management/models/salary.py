# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class salary(models.Model):
    _name = "salary"
    _inherits = {'employee': 'salary_id'}

    position = fields.Selection(
        [('nhan vien', 'nhan vien'),
         ('truong phong', 'Truong phong'),
            ('pho phong', 'Pho phong')],
        'Chuc vu', default="pho phong")
    

    Songay_lamviec = fields.Float(string="so ngay lam viec")
    LCB_nv = fields.Float(compute='_compute_LCB_nv', string="Luong co ban")

    final_price = fields.Float("Final Price", compute='_compute_final_price')

    # _description = "Product Pet"

    salary_id = fields.Many2one(
        'employee', 'Employee',
        auto_join=True, index=True, ondelete="cascade", required=True)

    bonus_price = fields.Float("Bonus Price", default=0)

    final_price = fields.Float("Final Price", compute='_compute_final_price')

    @api.depends("position")
    def _compute_LCB_nv(self):
        for record in self:
            if record.position == "nhan vien":
                record.LCB_nv = 5000
            if record.position == "truong phong":
                record.LCB_nv = 7000
            if record.position == "pho phong":
                record.LCB_nv = 6000

    # @api.depen("department")
    def _compute_final_price(self):
        for record in self:
            record.final_price = (record.Songay_lamviec) + record.LCB_nv*3

    @api.onchange('Songay_lamviec', 'bonus_price')
    def item_delivered_ids_onchange(self):
        if self.Songay_lamviec < 0:
            raise UserError('Wrong roi')
        if self.bonus_price < 0:
            raise UserError('Wrong roi')

        else:
            pass
    
    def custom_remove(self):
        for pet in self:
            pet.unlink()
        #_logger.warning(self.id) # 5
        #_logger.warning(self.ids) # [5]
        pass

    
    # @api.constrains('bonus_price')
    # def _check_(self):
    #     for record in self:
            
    
#
