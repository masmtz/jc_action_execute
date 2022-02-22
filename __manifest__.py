# -*- coding: utf-8 -*-
{
    'name': "JC Action Execute",
    'summary': """
        Acción de servidor que ejecuta un wizard para el cambio de fechas en 4013""",
    'description': """
        Acción de servidor que ejecuta un wizard para el cambio de fechas en 4013
    """,
    'author': "Samuel Martínez",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '12.0.1',
    'depends': ['base', 'prodigia_mrp_production_jc'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
