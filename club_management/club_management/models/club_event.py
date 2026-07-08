from odoo import models, fields

class ClubEvent(models.Model):
    _name = 'club.event'
    _description = 'Club Event / Workshop'

    name = fields.Char(string='Workshop Title', required=True)
    event_date = fields.Date(string='Date', required=True)
    event_time = fields.Float(string='Time')
    presenter_name = fields.Char(string='Presenter/Trainer Name', required=True)
