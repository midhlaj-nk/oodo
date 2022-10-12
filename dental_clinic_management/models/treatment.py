from odoo import fields, models, api


class Treatment(models.Model):
    _name = "treatment"
    _description = "Treatments"
    _rec_name = 'treatment_id_id'

    treatment_id_id = fields.Char(readonly=True)
    patient_id = fields.Many2one('patient')
    date_requested = fields.Date()
    price_list_clinic_id = fields.Many2one('product.pricelist', required=True)
    invoice = fields.Char()  # many
    operating_room = fields.Many2one('clinic.operating.room')
    dentist_id = fields.Many2one('dentist')
    date_of_analysis = fields.Date()
    invoice_exempt = fields.Boolean()
    treatment_line_ids = fields.One2many('treatment.lines', 'treatment_id')
    state = fields.Selection(
        selection=[('draft', 'Draft'),
                   ('confirmed', 'Confirmed'), ('done', 'Done')],
        default='draft')

    def create_invoices(self):
        self.state = "done"
        vals = []
        for record in self.treatment_line_ids:
            vals.append((0, 0,
                         {
                             'product_id': record.product_id.id,
                             'quantity': record.qty,
                             'price_unit': record.product_id.list_price,
                         }))
            print(vals)
        invoice = self.env['account.move'].create([
            {'move_type': 'out_invoice',
             'partner_id': self.patient_id.patient_id.id,
             'ref': self.treatment_id_id,
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

    @api.model
    def create(self, vals):
        vals['treatment_id_id'] = self.env['ir.sequence'].next_by_code(
            'treatment')
        return super(Treatment, self).create(vals)


class TreatmentLines(models.Model):
    _name = 'treatment.lines'

    product_id = fields.Many2one('product.product')
    price_unit = fields.Float(related='product_id.list_price', string='price')
    qty = fields.Integer(default=1, string='quantity')
    treatment_id = fields.Many2one('treatment')

    @api.onchange('qty')
    def _onchange_price_calculate(self):
        for rec in self:
            rec.price_unit = rec.qty * rec.price_unit


class IsTreatmentProduct(models.Model):
    _inherit = 'product.product'

    _is_treatment = fields.Boolean()
