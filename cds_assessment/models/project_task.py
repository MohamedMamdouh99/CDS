from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    developer_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Developer',
    )
    functional_consultant_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Functional Consultant',
    )
    development_status = fields.Selection(
        [('pending', 'Pending'),
         ('ongoing', 'Ongoing'),
         ('delivered', 'Delivered'),
         ('onhold', 'On Hold'),
         ('cancelled', 'Cancelled')],
        string='Development Status'
    )
    module = fields.Char(string='Module')
    branch = fields.Char(string='Branch')
    release_notes = fields.Text(string='Release Notes')
    task_priority = fields.Selection(
        [('low', 'Low'),
         ('medium', 'Medium'),
         ('high', 'High')],
        string='Priority'
    )
    internal_deadline = fields.Date(string='Internal Deadline')
    research_time = fields.Float(string='Research and Solution Design Time')
    development_time = fields.Float(string='Development Time')
    testing_time = fields.Float(string='Testing Time')
    allocated_time = fields.Float(
        string='Allocated Time', compute='_compute_allocated_time'
    )
    task_number = fields.Char(string='Task Number', readonly=True, required=True, copy=False, default='New')

    @api.model
    def create(self, vals):
        if vals.get('task_number', 'New') == 'New':
            vals['task_number'] = self.env['ir.sequence'].next_by_code('project.task.seq') or 'New'
        result = super(ProjectTask, self).create(vals)
        return result

    @api.depends('research_time', 'development_time', 'testing_time')
    def _compute_allocated_time(self):
        for rec in self:
            rec.allocated_time = rec.research_time + rec.development_time + rec.testing_time
