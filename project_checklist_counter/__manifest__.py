# -*- coding: utf-8 -*-
{
    'name': "Project Checklist Counter",
    'summary': """Manage checklist counter""",
    'description': """
        You can manage checklist counter.
    """,
    "version": "17.0.0.1",
    'sequence': '1',
    'author': "Reliution",
    'depends': ['base', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_task_view.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
