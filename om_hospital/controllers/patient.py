import json

from odoo import http
from odoo.http import request


class Patient(http.Controller):

    @http.route('/get_patients', type='json', auth='user')
    def get_patient(self):
        patient_rec = request.env['hospital.patient'].sudo().search([])
        patients = []
        for rec in patient_rec:
            vals = {
                'id':rec.id,
                'name':rec.name,
            }
            patients.append(vals)
        print('Patient list ---->',patients)
        return patients