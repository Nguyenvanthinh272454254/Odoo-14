# -*- coding: utf-8 -*-
{
    'name': "updatereport",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'report/template.xml',
        # 'views/asset.xml',
        'report/product_label_reports.xml',
        'report/information_employee.xml',
        'views/views.xml',
        # 'report/report_youtube.xml',
        # 'views/change_scss.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
