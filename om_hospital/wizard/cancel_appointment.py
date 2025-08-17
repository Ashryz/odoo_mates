import datetime
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    @api.model
    def default_get(self, fields_list):
        res = super(CancelAppointmentWizard, self).default_get(fields_list)
        res['cancellation_date'] = datetime.date.today()
        if self.env.context.get('active_id'):
            res['appointment_id'] = self.env.context.get('active_id')
        return res

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    reason = fields.Text()
    cancellation_date = fields.Date()

    def action_cancel(self):
        for rec in self:
            cancel_day = self.env['ir.config_parameter'].get_param('om_hospital.cancel_days')
            allowed_date = rec.appointment_id.booking_date - relativedelta(days=int(cancel_day))
            if allowed_date <= datetime.date.today():
                raise ValidationError(_("You can not cancel this appointment, grace period is exceeded"))
            else :
                rec.appointment_id.state = 'cancel'
