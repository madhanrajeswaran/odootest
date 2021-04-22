# -*- coding: utf-8 -*-
{
    'name': "BBTech Admin SSO",

    'summary': """ Admin side SSO """,

    'description': """ Install this module in admin DB to enable SSO """,

    'author': "Bitbrais Technology",

    'website': "www.bitbrainstech.com",

    'category': 'Uncategorized',

    'version': '13.0.0.0.1',

    'depends': ['base'],
    
    'data': [
        'security/ir.model.access.csv',
        'views/sso_sites_views.xml',
    ],
}
