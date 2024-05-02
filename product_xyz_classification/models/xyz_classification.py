from odoo import fields, models


class XyzClassification(models.Model):

    _name = "xyz.classification"
    _description = "XYZ Classification"

    name = fields.Char(string="Name")
