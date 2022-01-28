# -*- coding: utf-8 -*-

from odoo import api, models


#  stock  reports
class ReportStockReport(models.AbstractModel):
    _name = 'report.stock.report_picking'

    
    def _get_report_values(self, docids, data=None):
        picking_obj = self.env['stock.picking'].browse(docids[0])
        self.model = self.env.context.get('active_model')
        user = self.env["res.users"].browse(self._uid)
        company_data = user.company_id
        data = {
            'sale_header_footer': user.company_id.sale_header_footer,
            'primary_color': company_data.primary_color,
            'secondary_color': company_data.secondary_color,
            'sale_font_color': company_data.sale_font_color
        }
        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': picking_obj,
            'data': data,
            'doc': user,
        }
        return docargs


#  stock  delivery
class ReportStockDeliveryReport(models.AbstractModel):
    _name = 'report.stock.report_deliveryslip'

    
    def _get_report_values(self, docids, data=None):
        delivery_obj = self.env['stock.picking'].browse(docids[0])
        self.model = self.env.context.get('active_model')
        user = self.env["res.users"].browse(self._uid)
        company_data = user.company_id
        data = {
            'sale_header_footer': user.company_id.sale_header_footer,
            'primary_color': company_data.primary_color,
            'secondary_color': company_data.secondary_color,
            'sale_font_color': company_data.sale_font_color
        }
        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': delivery_obj,
            'data': data,
            'doc': user,
        }
        return docargs
