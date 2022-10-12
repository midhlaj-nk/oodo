from odoo import fields, models, api
from datetime import date, datetime, time


class Appointment(models.Model):
    _name = "appointment"
    _description = "Appointments"
    _rec_name = 'appointment_id_id'

    appointment_id_id = fields.Char(readonly=True)
    patient_id = fields.Many2one('patient', required=True)
    appointment_start_date = fields.Datetime(default=datetime.today(),
                                             required=True)
    appointment_end_date = fields.Datetime(default=datetime.today(),
                                           required=True)
    dentist_id = fields.Many2one('dentist', required=True)
    price_list_clinic_id = fields.Many2one('product.pricelist', required=True)
    health_center_id = fields.Many2one('res.partner')
    urgency_level = fields.Selection(
        selection=[('normal', 'Normal'),
                   ('high_risk', 'High Risk'), ('low_risk', 'Low Risk')],
        default='normal')
    product_id = fields.Many2one('product.product',
                                 domain="[('can_be_expensed', '=', True)]")
    invoice_exempt = fields.Boolean()
    state = fields.Selection(
        selection=[('draft', 'Draft'),
                   ('confirmed', 'Confirmed'), ('done', 'Done')],
        default='draft')

    prescription_line_ids = fields.One2many('prescription', 'patient_id_id')
    initial_treatment_line_ids = fields.One2many('initial.treatment',
                                                 'patient_id_id')
    prescription_line_id = fields.Many2one('prescription')

    @api.model
    def create(self, vals):
        print(self.env['ir.sequence'])
        vals['appointment_id_id'] = self.env['ir.sequence'].next_by_code(
            'appointment')
        return super(Appointment, self).create(vals)

    def create_invoices(self):
        self.state = "done"
        vals = []
        for rec in self:
            print(self.product_id.id)
            vals.append((0, 0,
                         {
                             'product_id': rec.product_id.id,
                             'quantity': 1,
                             'price_unit': rec.product_id.list_price,
                         }))
            print(vals)
        invoice = self.env['account.move'].create([

            {'move_type': 'out_invoice',
             'partner_id': self.patient_id.patient_id.id,
             'ref': self.appointment_id_id,
             'invoice_date': fields.Date.today(),
             'invoice_line_ids': vals
             }, ])

        return {
            'res_model': 'account.move',
            'res_id': invoice.id,
            'view_mode': 'form',
            'view_type': 'form',
            'type': 'ir.actions.act_window',
        }

    def button_confirm(self):
        self.state = 'confirmed'

    def button_cancel(self):
        self.state = 'draft'
