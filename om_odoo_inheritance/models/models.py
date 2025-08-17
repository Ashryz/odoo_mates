from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one('res.users',string="Confirmed User")

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        self.confirmed_user_id = self.env.user.id

    def _prepare_invoice(self):
        inv_vals = super(SaleOrder, self)._prepare_invoice()
        inv_vals['so_confirmed_user_id'] = self.confirmed_user_id.id
        return  inv_vals

class AccountMove(models.Model):
    _inherit='account.move'

    so_confirmed_user_id = fields.Many2one('res.users', string='SO Confirmed User')