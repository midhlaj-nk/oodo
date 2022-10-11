from odoo import fields, models, api


class Teeth(models.Model):
    _name = "teeth"
    _description = "teeth"

    name = fields.Char()
    code = fields.Char()
