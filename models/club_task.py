from odoo import models, fields

class ClubTask(models.Model):
    _name = 'club.task'
    _description = 'Club Task'

    name = fields.Char(string='Task Name', required=True)
    member_id = fields.Many2one('club.member', string='Assigned Member')
    deadline = fields.Date(string='Deadline')
    state = fields.Selection([
        ('new', 'New'),
        ('progress', 'In Progress'),
        ('done', 'Done')
    ], string='Status', default='new')