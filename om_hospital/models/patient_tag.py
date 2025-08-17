from odoo import models, fields


class PatientTag(models.Model):
    _name='patient.tag'
    _description = 'Patient Tag'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    color = fields.Integer()
    color_2 = fields.Char()

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Patient tag name must be unique')
    ]