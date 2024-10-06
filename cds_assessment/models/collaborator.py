from odoo import models, fields, api


class ProjectCollaborators(models.Model):
    _name = 'project.collaborators'
    _description = 'Project Collaborator'

    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Employee',
        required=True)
    status = fields.Selection(
        [('active', 'Active'), ('inactive', 'Inactive')],
        string='Status',
        default='active'
    )
    project_id = fields.Many2one(
        comodel_name='project.project',
        string='Project',
        required=False)

    def set_active(self):
        self.status = 'active'

    def set_inactive(self):
        self.status = 'inactive'
