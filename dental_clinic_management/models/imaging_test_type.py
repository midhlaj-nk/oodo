from odoo import fields, models, api


class ImagingTestType(models.Model):
    _name = "imaging_test_type"
    _description = "imaging_test_types"

    name = fields.Char()
    code = fields.Char()
