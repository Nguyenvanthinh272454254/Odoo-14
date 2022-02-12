# -*- coding: utf-8 -*-

from odoo import api, models, fields


#  production reports
class ReportProductionReport(models.AbstractModel):
    _name = 'report.mrp.report_mrporder'

    
    def _get_report_values(self, docids, data=None):
        production_obj = self.env['mrp.production'].browse(docids[0])
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
            'docs': production_obj,
            'data': data,
            'doc': user,
        }
        return docargs
