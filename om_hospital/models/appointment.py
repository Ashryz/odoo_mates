from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', 'Patient')
    appointment_time = fields.Date(default=fields.Date.context_today)
    booking_date = fields.Date(default=fields.Date.context_today)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], related='patient_id.gender')
    ref = fields.Char(string='Reference')
    prescription = fields.Html()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], default='draft', tracking=1)
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='Pharmacy Lines')

    def unlink(self):
        if self.state != 'draft':
            raise ValidationError(_("you can only delete appointment in 'draft' state"))

    @api.onchange('patient_id')
    def change_patient_id(self):
        for rec in self:
            rec.ref = rec.patient_id.ref

    def set_to_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def set_to_done(self):
        for rec in self:
            rec.state = 'done'

    def set_to_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def set_to_draft(self):
        for rec in self:
            if rec.state != 'done':
                rec.state = 'draft'

