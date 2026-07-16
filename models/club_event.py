from odoo import models, fields

class ClubEvent(models.Model):
    _name = 'club.event'
    _description = 'Club Event / Workshop'
    _order = 'event_date desc'

    name = fields.Char(string='Workshop Title', required=True)
    event_date = fields.Date(string='Date', required=True)
    event_time = fields.Float(string='Time')
    presenter_name = fields.Char(string='Presenter/Trainer Name', required=True)
    location = fields.Char(string='Location')
    description = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', required=True)

    attendance_ids = fields.One2many('club.attendance', 'event_id', string='Attendance')
    task_ids = fields.One2many('club.task', 'event_id', string='Tasks')

    attendee_count = fields.Integer(compute='_compute_counts', string='Attendees')
    task_count = fields.Integer(compute='_compute_counts', string='Tasks')

    def _compute_counts(self):
        for rec in self:
            rec.attendee_count = len(rec.attendance_ids)
            rec.task_count = len(rec.task_ids)

    def action_confirm(self):
        self.write({'state': 'confirmed'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_reset_draft(self):
        self.write({'state': 'draft'})

    def action_view_attendance(self):
        self.ensure_one()
        return {
            'name': 'Attendance',
            'type': 'ir.actions.act_window',
            'res_model': 'club.attendance',
            'view_mode': 'list,form',
            'domain': [('event_id', '=', self.id)],
            'context': {'default_event_id': self.id},
        }

    def action_view_tasks(self):
        self.ensure_one()
        return {
            'name': 'Tasks',
            'type': 'ir.actions.act_window',
            'res_model': 'club.task',
            'view_mode': 'list,form',
            'domain': [('event_id', '=', self.id)],
            'context': {'default_event_id': self.id},
        }
