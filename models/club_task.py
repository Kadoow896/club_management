from odoo import models, fields

class ClubTask(models.Model):
    _name = 'club.task'
    _description = 'Workshop Preparation Task'
    _order = 'priority desc, due_date'

    name = fields.Char(string='Task Description', required=True)
    event_id = fields.Many2one('club.event', string='Workshop / Event', required=True, ondelete='cascade')
    member_id = fields.Many2one('club.member', string='Assigned To')
    due_date = fields.Date(string='Due Date')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'High'),
    ], string='Priority', default='0')
    state = fields.Selection([
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], string='Status', default='todo', required=True)
