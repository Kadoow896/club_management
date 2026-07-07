{
    'name': 'Club Management',
    'version': '1.0',
    'summary': 'Manage club members and activities',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/club_member_views.xml',

    ],
    'installable': True,
    'application': True,
}