from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char(tracking=True)
    date_of_birth = fields.Date()
    age = fields.Integer(compute='_compute_age', inverse='_inverse_compute_age', search='_search_by_age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ])
    ref = fields.Char(string='Reference', tracking=True)
    active = fields.Boolean('Active', default=True)
    image = fields.Image()
    tag_ids = fields.Many2many('patient.tag', string='Tags')
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id')
    appointment_count = fields.Integer(compute='_compute_appointment_count')
    parent = fields.Char()
    marital_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married')
    ])
    partner_name = fields.Char()

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])

    def action_view_appointments(self):
        return {
            'name': _('Appointments'),
            'res_model': 'hospital.appointment',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'target': 'current',
            'context':{'default_patient_id': self.id},
            'domain': [('patient_id', '=' , self.id)],
        }
    @api.model
    def create(self, vals_list):
        vals_list['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals_list)

    def write(self, vals):
        if not self.ref and not  vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)


    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_("The birthdate u entered is not acceptable. "))

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
             if rec.date_of_birth:
                 rec.age = relativedelta(fields.Date.today(), rec.date_of_birth).years
             else:
                 rec.age = 0

    @api.depends('age')
    def _inverse_compute_age(self):
        for rec in self:
            if rec.age:
                rec.date_of_birth = fields.Date.today() - relativedelta(years=rec.age)

    def _search_by_age(self, operator, value):
        date_of_birth = fields.Date.today() - relativedelta(years=value)
        start_of_year = date_of_birth.replace(day=1, month=1)
        end_of_year = date_of_birth.replace(day=31, month=12)
        print(f"start : {start_of_year} ... end : {end_of_year}")
        return [('date_of_birth', '>=',start_of_year),('date_of_birth', '<=',end_of_year)]

    def name_get(self):
        # patient_list =[]
        # for rec in self:
        #     name = f"[{rec.ref}] {rec.name}"
        #     patient_list.append((rec.id, name))
        # return patient_list
        # print("inside name get")
        return [(rec.id, "[%s] %s" % (rec.ref, rec.name)) for rec in self]