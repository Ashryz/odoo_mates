from  odoo import models, fields, api


class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'

    product_id = fields.Many2one('product.product', string='Product')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    price_unit = fields.Float(related='product_id.lst_price', string='Price')
    qty = fields.Integer(string='Quantity', default=1)
    pl_no = fields.Integer(string='NO.', compute='_compute_line_num')

    @api.depends('appointment_id.pharmacy_line_ids')
    def _compute_line_num(self):
        for record in self.mapped('appointment_id'):
            for rec, line in enumerate(record.pharmacy_line_ids, start=1):
                line.pl_no = rec

