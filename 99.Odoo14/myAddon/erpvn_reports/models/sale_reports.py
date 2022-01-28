# -*- coding: utf-8 -*-

from odoo import api, models


#  sale order reports
class ReportSaleReport(models.AbstractModel):
    _name = 'report.sale.report_saleorder'

    
    def _get_report_values(self, docids, data=None):
        sale_obj = self.env['sale.order'].browse(docids[0])
        # self.filtered(lambda s: s.state == 'draft').write({'state': 'sent'})
        # self.model = self.env.context.get('active_model')
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
            'doc_model': self._name,
            'docs': sale_obj,
            'data': data,
            'doc': user,
        }
        return docargs
