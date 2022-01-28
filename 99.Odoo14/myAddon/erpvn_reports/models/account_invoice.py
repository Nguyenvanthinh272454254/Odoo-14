# -*- coding: utf-8 -*-

from odoo import api, models


#  account invoice reports
class ReportAccountReport(models.AbstractModel):
    _name = 'report.account.report_invoice'

    
    def _get_report_values(self, docids, data=None):
        invoice_obj = self.env['account.invoice'].browse(docids[0])
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
            'docs': invoice_obj,
            'data': data,
            'doc': user,
        }

        return docargs


#  account invoice reports withpayments
class ReportAccountDupReport(models.AbstractModel):
    _name = 'report.account.report_invoice_with_payments'

    
    def _get_report_values(self, docids, data=None):
        sale_obj = self.env['account.invoice'].browse(docids[0])
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
            'docs': sale_obj,
            'data': data,
            'doc': user,
        }

        return docargs
