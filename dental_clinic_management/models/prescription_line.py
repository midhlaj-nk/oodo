from odoo import fields, models, api


class PrescriptionLine(models.Model):
    _name = "prescription.line"
    _description = "prescription lines"

    prescription_id = fields.Many2one('prescription', 'prescription_id_id')

    medicine = fields.Many2one('product.template')
    allow_substitution = fields.Boolean()
    form = fields.Char()  # many
    start_treatment_date = fields.Datetime()
    end_treatment_date = fields.Datetime()
    indication = fields.Char()  # many
    print = fields.Boolean()
    administration_route = fields.Char()  # many

    quantity = fields.Integer()
    treatment_duration = fields.Integer()
    treatment_period = fields.Integer()
    comment = fields.Char()

    dose = fields.Integer()
    dose_unit = fields.Many2one('uom.uom')
    dose_unit_multiple = fields.Integer()

    specific_dosage_frequency = fields.Integer()
    specific_dosage_unit = fields.Many2one('uom.uom')
