# -*- coding: utf-8 -*-
{
    'name': "Toratto",

    'summary': """
        Administración de proyectos de construcción""",

    'description': """
        CRM Inmobiliario
    """,

    'author': "Víctor Valencia",
    'website': "https://www.grupotoratto.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/project_view.xml',
        'views/unit_view.xml',
        'views/unit_type_view.xml',
        'views/menu.xml',
        'views/settings.xml',
        'views/res_country_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
