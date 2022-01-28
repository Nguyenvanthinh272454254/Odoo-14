from odoo import http
from odoo.http import request


class Supperproject(http.Controller):
    @http.route('/test/', auth='public', website=True)
    def test_qweb(self, **kw):
        # supperproject.product_test, supperproject tro den idproduct_test trong
        employees = request.env['hr.employee'].sudo().search([])
       

        return request.render("supperproject.product_test",{'employees': employees})
