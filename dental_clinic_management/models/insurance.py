from odoo import fields, models, api
from datetime import date, datetime, time


class IsInsuranceCompany(models.Model):
    _inherit = 'res.partner'
    _description = "patients in res_partner"

    is_insurance_company = fields.Boolean()


class Insurance(models.Model):
    _name = "insurance"
    _description = "insurances"

    Insurance_number = fields.Char()
    Insurance_type = fields.Char()
    insurance_plan = fields.Char()
    member_since_date = fields.Date()
    extra_info = fields.Char()
    owner = fields.Many2one('patient')
    Insurance_company = fields.Many2one('res.partner')
    category = fields.Char()
    expiration_date = fields.Char()
