from odoo import fields, models


class IsMedicineProduct(models.Model):
    _inherit = 'product.product'

    _is_medicine = fields.Boolean()

