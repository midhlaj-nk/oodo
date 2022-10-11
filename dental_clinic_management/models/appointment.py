from odoo import fields, models, api
from datetime import date, datetime, time


class Appointment(models.Model):
    _name = "appointment"
    _description = "Appointments"
    _rec_name = 'patient_id'

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
    product_id = fields.Many2one('product.template')
    invoice_exempt = fields.Boolean()
    state = fields.Selection(
        selection=[('draft', 'Draft'),
                   ('confirmed', 'Confirmed'), ('done', 'Done')],
        default='draft')

    prescription_line_ids = fields.One2many('prescription', 'patient_id_id')
    initial_treatment_line_ids = fields.One2many('initial.treatment',
                                                 'patient_id_id')

    @api.model
    def create(self, vals):
        print(self.env['ir.sequence'])
        vals['appointment_id_id'] = self.env['ir.sequence'].next_by_code(
            'appointment')
        return super(Appointment, self).create(vals)
