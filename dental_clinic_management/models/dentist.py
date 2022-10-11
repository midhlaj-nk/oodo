from odoo import fields, models


class Dentist(models.Model):
    _name = "dentist"
    _description = "dentist"
    _rec_name = 'dentist_id'

    dentist_id = fields.Many2one('res.partner')
    # patient_id_id = fields.Many2one('patient')
    speciality_id = fields.Many2one('medical.speciality')
    ssn = fields.Char()
    dentist_id_id = fields.Char()


class MedicalSpeciality(models.Model):
    _name = "medical.speciality"
    _rec_name = 'speciality'
    speciality = fields.Char()
    code = fields.Char()
