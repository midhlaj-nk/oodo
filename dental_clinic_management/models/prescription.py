from odoo import fields, models, api
from datetime import date, datetime, time


class Prescription(models.Model):
    _name = "prescription"
    _description = "prescription"
    _rec_name = "prescription_id_id"
    patient_id_id = fields.Many2one('appointment')
    patient_id = fields.Many2one('patient')
    prescription_id_id = fields.Char()
    prescription_ids = fields.One2many('prescription.line', 'prescription_id')
    log_in_user = fields.Many2one('res.users','Current User', default=lambda self: self.env.user,readonly=True)

    prescription_date = fields.Datetime(default=datetime.today())
    prescribing_dentist_id = fields.Many2one('dentist')
    appointment_id = fields.Many2one('appointment', 'appointment_id_id')
    Invoice_status = fields.Char()
    pharmacy = fields.Char()
    price_list_clinic_id = fields.Many2one('product.pricelist', required=True)
    invoice_exempt = fields.Boolean()

    @api.model
    def create(self, vals):
        vals['prescription_id_id'] = self.env['ir.sequence'].next_by_code(
            'prescription')
        return super(Prescription, self).create(vals)

