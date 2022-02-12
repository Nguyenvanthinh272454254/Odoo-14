# -*- coding: utf-8 -*-
from odoo import api, models


#  product label reports
class ReportProductLabelReport(models.AbstractModel):
    _name = 'report.product.report_producttemplatelabel'

    
    def _get_report_values(self, docids, data=None):
        label_obj = self.env['product.template'].browse(docids[0])
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
            'docs': label_obj,
            'data': data,
            'doc': user,
        }

        return docargs
