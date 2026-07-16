{
    'name': 'Club Management',
    'version': '1.1',
    'summary': 'Manage club members and activities',
    'category': 'Productivity',
    'license': 'LGPL-3',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/club_security.xml',
        'security/ir.model.access.csv',
        'views/club_member_views.xml',
        'views/club_event_views.xml',
        'views/club_attendance_views.xml',
        'views/club_task_views.xml',
    ],
    'installable': True,
    'application': True,
}
