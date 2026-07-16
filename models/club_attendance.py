from odoo import models, fields

class ClubAttendance(models.Model):
    _name = 'club.attendance'
    _description = 'Workshop Attendance'
    _rec_name = 'member_id'
    _order = 'event_id desc, member_id'

    event_id = fields.Many2one('club.event', string='Workshop / Event', required=True, ondelete='cascade')
    member_id = fields.Many2one('club.member', string='Member', required=True, ondelete='cascade')
    attended = fields.Boolean(string='Attended', default=False)

    _sql_constraints = [
        ('unique_member_event', 'unique(event_id, member_id)',
         'This member is already listed for this event.')
    ]
