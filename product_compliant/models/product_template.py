from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    # atex_compliant = fields.Boolean(
    #     string="ATEX Compliant",
    #     help="This product is ATEX directive compliant.",
    # )

    atex_compliant = fields.Many2many(
        'product.compliant',
        string='ATEX Compliant',
        help='This product is ATEX directive compliant.'
    )

    # reach_compliant = fields.Boolean(
    #     string="REACH Compliant",
    #     help="This product is Registration, Evaluation, Authorisation and Restriction "
    #     "of Chemicals regulation compliant.",
    # )
    
    reach_compliant = fields.Many2many(
        'product.compliant',
        string='REACH Compliant',
        relation="rel_reach_compliant",
        help='This product is Registration, Evaluation, Authorisation and Restriction of Chemicals regulation compliant.'
    )

    # rohs_compliant = fields.Boolean(
    #     string="RoHS Compliant",
    #     help="This product is Restriction of Hazardous Substances Directive 2002/95/EC "
    #     "compliant.",
    # )

    rohs_compliant = fields.Many2many(
        'product.compliant',
        string='RoHS Compliant',
        relation="rel_rohs_compliant",
        help='This product is Restriction of Hazardous Substances Directive 2002/95/EC compliant.'
    )
