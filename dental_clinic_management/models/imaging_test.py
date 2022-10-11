from odoo import fields, models, api


class ImagingTest(models.Model):
    _name = "imaging_test"
    _description = "imaging_test"

    name = fields.Char()
    code = fields.Char()
    service = fields.Char()

    imaging_test_types = fields.Many2one('imaging_test_type',string='Type')
