from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    github_account = fields.Char(string='GitHub Account')
    project_ids = fields.One2many(
        comodel_name='project.collaborators',
        inverse_name='employee_id',
        string='Projects',
    )

    def unlink(self):
        for employee in self:
            active_projects = employee.project_ids.filtered(lambda c: c.status == 'active')
            if active_projects:
                raise UserError("Cannot delete employee with active projects.")
        super(HrEmployee, self).unlink()
