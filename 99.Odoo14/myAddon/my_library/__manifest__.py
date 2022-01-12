# -*- coding: utf-8 -*-
{
    'name': "My library",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Thinh nguyen
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/librarybook.xml',
        'views/library_book_categ.xml',
        'views/library_book_rent.xml',
        'wizard/library_book_rent_wizard.xml',
        'wizard/library_book_return_wizard.xml',
        'views/library_book_statistics.xml',
        'views/res_config_settings_views.xml'


    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'data/demo.xml'
    # ],
}
