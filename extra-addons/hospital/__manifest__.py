# -*- coding: utf-8 -*-
{
    'name': "Tarea18 Hospital",

    'summary': "Administrar hospital",

    'description': """
        Crea un módulo para odoo 18 community que permita gestionar pacientes y médicos de un hospital. 
    """,

    'author': "Oliver Miguez Alonso",
    'website': "https://xogosaqui.itch.io/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        "views/diagnosticos_views.xml",
        "views/medicos_views.xml",
        "views/pacientes_views.xml",
        "views/menu.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

