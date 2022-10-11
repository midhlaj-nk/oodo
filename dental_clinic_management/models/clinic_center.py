from odoo import fields, models, api


class ClinicCenter(models.Model):
    _name = "clinic.center"
    _description = "Dental Clinic Center"

    name = fields.Char()
    code = fields.Char()
    extra_info = fields.Char()
    institution = fields.Char()


class ClinicBuilding(models.Model):
    _name = "clinic.building"
    _description = "Dental Clinic Center Building"

    name = fields.Char()
    code = fields.Char()
    extra_info = fields.Char()
    institution = fields.Char()


class ClinicUnit(models.Model):
    _name = "clinic.unit"
    _description = "Dental Clinic Center Unit"

    name = fields.Char()
    code = fields.Char()
    extra_info = fields.Char()
    institution = fields.Char()


class OperatingRoom(models.Model):
    _name = "clinic.operating.room"
    _description = "Dental Clinic Operating Room"

    name = fields.Char()
    code = fields.Char()
    extra_info = fields.Char()
    institution = fields.Char()
    unit = fields.Many2one('clinic.unit')
