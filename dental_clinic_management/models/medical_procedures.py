from odoo import fields, models, api
from datetime import date, datetime, time


class MedicalProcedures(models.Model):
    _name = "medical.procedures"

    code = fields.Char()
    process = fields.Char()
