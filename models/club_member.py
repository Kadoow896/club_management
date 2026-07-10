from odoo import models, fields

class ClubMember(models.Model):
    _name = 'club.member'
    _description = 'Club Member'

    name = fields.Char(string='Name', required=True)
    university_id = fields.Char(string='University ID', required=True)
    major = fields.Char(string='Major')
    track = fields.Selection([('developer', 'Developer'), ('designer', 'UI/UX Designer'), ('organizer', 'Organizer')], string='Technical Track')
