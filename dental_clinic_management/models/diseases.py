from odoo import fields, models, api


class Diseases(models.Model):
    _name = "diseases"
    _description = "diseases"
    _rec_name = 'diseases'

    diseases = fields.Many2one('diseases.items')
    status = fields.Char()
    active = fields.Boolean()
    infectious = fields.Boolean()
    severity = fields.Char()
    allergy = fields.Boolean()
    pregnancy_warning = fields.Boolean()
    diagnosed = fields.Date()
    end_date = fields.Date()
    remarks = fields.Char()
    patient_id = fields.Many2one('patient')


class DiseasesItems(models.Model):
    _name = "diseases.items"
    _rec_name = 'disease_item'

    disease_item = fields.Char()
