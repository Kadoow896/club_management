from odoo import models, fields

class ClubMember(models.Model):
    _name = 'club.member'
    _description = 'Club Member'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    university_id = fields.Char(string='University ID', required=True)
    major = fields.Char(string='Major')
    track = fields.Selection([('developer', 'Developer'), ('designer', 'UI/UX Designer'), ('organizer', 'Organizer')], string='Technical Track')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    join_date = fields.Date(string='Join Date', default=fields.Date.context_today)
    active = fields.Boolean(string='Active', default=True)

    attendance_ids = fields.One2many('club.attendance', 'member_id', string='Attendance')
    task_ids = fields.One2many('club.task', 'member_id', string='Assigned Tasks')
    attended_event_count = fields.Integer(compute='_compute_counts', string='Events Attended')

    def _compute_counts(self):
        for rec in self:
            rec.attended_event_count = len(rec.attendance_ids.filtered('attended'))

    def action_view_attendance(self):
        self.ensure_one()
        return {
            'name': 'Attendance',
            'type': 'ir.actions.act_window',
            'res_model': 'club.attendance',
            'view_mode': 'list,form',
            'domain': [('member_id', '=', self.id)],
            'context': {'default_member_id': self.id},
        }

    _sql_constraints = [
        ('unique_university_id', 'unique(university_id)',
         'A member with this University ID already exists.')
    ]
