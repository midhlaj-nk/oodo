from odoo import fields, models, api
from datetime import date, datetime, time


class Prescription(models.Model):
    _name = "prescription"
    _description = "prescription"
    _rec_name = "prescription_id_id"
    patient_id = fields.Many2one('patient')
    prescription_id_id = fields.Char(readonly=True)
    prescription_ids = fields.One2many('prescription.line', 'prescription_id')
    log_in_user = fields.Many2one('res.users', 'Current User',
                                  default=lambda self: self.env.user,
                                  readonly=True)

    prescription_date = fields.Datetime(default=datetime.today())
    prescribing_dentist_id = fields.Many2one('dentist')
    appointment_id = fields.Many2one('appointment', 'appointment_id_id')
    Invoice_status = fields.Char()
    pharmacy = fields.Many2one('clinic.center', 'name')
    price_list_clinic_id = fields.Many2one('product.pricelist', required=True)
    invoice_exempt = fields.Boolean()
    state = fields.Selection(
        selection=[('draft', 'Draft'),
                   ('confirmed', 'Confirmed'), ('done', 'Done')],
        default='draft')

    patient_id_id = fields.Many2one('appointment')  # relation

    @api.model
    def create(self, vals):
        vals['prescription_id_id'] = self.env['ir.sequence'].next_by_code(
            'prescription')
        return super(Prescription, self).create(vals)

    def create_invoices(self):
        self.state = "done"
        vals = []
        for record in self.prescription_ids:
            vals.append((0, 0,
                         {
                             'product_id': record.medicine.id,
                             'quantity': record.quantity,
                             'price_unit': record.medicine.list_price,
                         }))
            print(vals)
        invoice = self.env['account.move'].create([
            {'move_type': 'out_invoice',
             'partner_id': self.patient_id.patient_id.id,
             'ref': self.appointment_id.appointment_id_id,
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
