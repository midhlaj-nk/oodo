from odoo import fields, models, api
from datetime import date
from dateutil.relativedelta import relativedelta


class IsPatientInResPartner(models.Model):
    _inherit = 'res.partner'
    _description = "patients in res_partner"

    is_patient = fields.Boolean()


class Patient(models.Model):
    _name = 'patient'
    _description = 'Patients in clinic'
    _rec_name = 'patient_id'

    image = fields.Image()
    # main info
    patient_id = fields.Many2one('res.partner')
    dob = fields.Date()
    patient_age = fields.Char(readonly=True)
    patient_id_id = fields.Char(readonly=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')])

    # # General Information
    family = fields.Char()
    marital_status = fields.Selection([
        ('not_married', 'Not Married'),
        ('married', 'Married'),
        ('other', 'Other')])
    blood_type = fields.Selection([
        ('a+', 'A +'),
        ('a-', 'A -'),
        ('b+', 'B +'), ('o+', 'O +'), ('o-', 'O -'), ('ab+', 'AB +'),
        ('ab-', 'AB -')])
    insurance = fields.Char()
    # Patient Extra Info
    deceased = fields.Boolean()
    # Appointment
    appointment_ids = fields.One2many('appointment', 'patient_id')
    # diseases
    diseases_ids = fields.One2many('diseases', 'patient_id')
    # prescription
    prescription_ids = fields.One2many('prescription', 'patient_id')
    # treatment
    treatment_ids = fields.One2many('treatment', 'patient_id')

    @api.model
    def create(self, vals):
        vals['patient_id_id'] = self.env['ir.sequence'].next_by_code(
            'patient')
        return super(Patient, self).create(vals)

    @api.constrains('patient_id')
    def _is_patient(self):
        self.patient_id.is_patient = True

    @api.constrains('dob')
    def _patient_age(self):
        if self.dob:
            years = relativedelta(date.today(), self.dob).years
            months = relativedelta(date.today(), self.dob).months
            day = relativedelta(date.today(), self.dob).days

            self.patient_age = str(int(years)) + ' y ' + str(
                int(months)) + ' m ' + str(day) + ' d'

    def name_get(self):
        patient_list = []
        for rec in self:
            if (type(rec.patient_id_id)) == str and (
                    type(rec.patient_id.name)) == str:
                print(type(rec.patient_id_id))
                name = '['+rec.patient_id_id+']' + ' ' + rec.patient_id.name
                patient_list.append((rec.id, name))
                print(patient_list)
        return patient_list
