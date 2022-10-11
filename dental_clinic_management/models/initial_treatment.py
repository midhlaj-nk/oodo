from odoo import fields, models, api


class InitialTreatment(models.Model):
    _name = "initial.treatment"
    _description = "Initial Treatment details"

    patient_id_id = fields.Many2one('appointment')
    code = fields.Char()
    process = fields.Char()
