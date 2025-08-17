from  odoo import models, fields


class AppointmentReportWizard(models.TransientModel):
    _name = 'appointment.report.wizard'
    _description = 'Appointment Report Wizard'

    patient_id = fields.Many2one('hospital.patient')
    date_from = fields.Date()
    date_to = fields.Date()


    def action_print(self):
        self.ensure_one()
        domain=[]
        patient_id = self.patient_id
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('appointment_time', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('appointment_time', '<=', date_to)]

        appointments = self.env['hospital.appointment'].search_read(domain)
        data = {
            'form_data': self.read()[0],
            'appointments': appointments,
        }
        return self.env.ref('om_hospital.action_appointment_report').report_action(self, data=data)

    def action_print_xlsx(self):
        self.ensure_one()
        domain = []
        patient_id = self.patient_id
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('appointment_time', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('appointment_time', '<=', date_to)]

        appointments = self.env['hospital.appointment'].search_read(domain)
        data = {
            'form_data': self.read()[0],
            'appointments': appointments,
        }
        print(data['form_data'])
        print("++++++++++++++++")
        print(data['appointments'])

        return self.env.ref('om_hospital.action_appointment_report_xlsx').report_action(self, data=data)