# -*- coding: utf-8 -*-
{
    'name': "CDS Assessment",

    'summary': """
       Customizations for project management""",

    'description': """
       Custom project module to add additional fields and features to the project & employee modules
       to facilitate the track of the projects development progress with the clients.
    """,

    'author': "Mohamed Mamdouh",
    'website': "https://www.cds-solutions.co/",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['project', 'hr'],

    'data': [
        'security/ir.model.access.csv',

        'data/sequence.xml',

        'views/project_view.xml',
        'views/project_task_view.xml',
        'views/hr_employee_view.xml',
        'views/collaborator_view.xml',

        'reports/project_report.xml',
        'reports/report_header.xml',
        'reports/project_template.xml',
    ],
}
