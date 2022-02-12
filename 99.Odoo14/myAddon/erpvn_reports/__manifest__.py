# -*- coding: utf-8 -*-

{
    'name':'Template Reports All in One',
    'category': 'Reports',
    'author': 'DuyBQ',
    'version': '1.0.9',
    'website': 'http://www.erp-vn.com',
    'description': """ Template Reports All in One
        + Invoice
        + Sale Order
        + Purchase Order
        + Purchase Quotation
        + Stock Delivery
        + Stock Picking
        + Production Order
        + Product Labels
        + Inventory ADJ
    """,
    'depends': [
        'base', 'web', 'sale', 'sale_management', 'product', 'account',
        'purchase', 'stock', 'mrp'
    ],
    'summary':
        ' To Generate Reports for All module',
    'data': [
        'views/res_company_view.xml',
        'views/professional_widget_color_view.xml',
        'views/reports_format.xml',

        'report/invoice/account_invoice_template3.xml',
        'report/invoice/account_invoice_template4.xml',
        'report/invoice/account_invoice_template2.xml',
        'report/invoice/account_invoice_template1.xml',

        'report/sale_order/sale_template1.xml',
        'report/sale_order/sale_template2.xml',
        'report/sale_order/sale_template3.xml',
        'report/sale_order/sale_template4.xml',
        'report/sale_order/sale_template5.xml',

        'report/purchase_order/purchase_template3.xml',
        'report/purchase_order/purchase_template4.xml',
        'report/purchase_order/purchase_template1.xml',
        'report/purchase_order/purchase_template2.xml',

        'report/purchase_quotation/purchase_quotation_template3.xml',
        'report/purchase_quotation/purchase_quotation_template4.xml',
        'report/purchase_quotation/purchase_quotation_template1.xml',
        'report/purchase_quotation/purchase_quotation_template2.xml',

        'report/stock_picking/stock_template3.xml',
        'report/stock_picking/stock_template4.xml',
        'report/stock_picking/stock_template1.xml',
        'report/stock_picking/stock_template2.xml',

        'report/stock_delivery/stock_delivery_template3.xml',
        'report/stock_delivery/stock_delivery_template4.xml',
        'report/stock_delivery/stock_delivery_template1.xml',
        'report/stock_delivery/stock_delivery_template2.xml',

        'report/production_order/production_template1.xml',
        'report/production_order/production_template2.xml',
        'report/production_order/production_template3.xml',
        'report/production_order/production_odoo_standard.xml',

        'report/product_label/product_label_template1.xml',
        'report/product_label/product_label_template2.xml',
        'report/product_label/product_label_template3.xml',
        'report/product_label/product_label_odoo_standard.xml',

        'report/inventory_adj/adj_odoo_standard.xml',
        'report/inventory_adj/adj_template1.xml',
        'report/inventory_adj/adj_template2.xml',
        'report/inventory_adj/adj_template3.xml',

    ],
    'qweb': [
        'static/src/xml/widget.xml',
    ],
    'images': ['static/description/Banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
