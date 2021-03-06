import uuid

from odoo import models,fields,api
class Air_freight_bill(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'
    _description = 'Air Freight Bill'

# ========= IDs ========================================================================================================
    mawb_afb_ID = fields.Many2one("mawb.model",string='MAWB NO')
    hawb_afb_ID = fields.Many2one("hawb.model",string='HAWB NO')

    #services_ID = fields.One2many('services.model', 'invoice_id')

    partner_id = fields.Many2one(related='hawb_afb_ID.h_consignee',string='Partner', store=True, change_default=True,
                                 required=True, readonly=True, states={'draft': [('readonly', False)]},
                                 track_visibility='always')


    afb_no_of_pieces = fields.Integer(related='hawb_afb_ID.h_no_of_pieces',
                                      string='No Of Pieces', store=True, readonly=True)
    afb_gross_weight = fields.Float(related='hawb_afb_ID.total_gross',
                                      string='Gross Weight', store=True, readonly=True)
    afb_Chargeable_Wight = fields.Float(related='hawb_afb_ID.total_chargable',
                                      string='Chargeable Weight', store=True, readonly=True)

    shipping_port = fields.Char('shipping port')
    arrival_port = fields.Char('Arrival port')

    freight_charge = fields.Float(compute='_compute_frieght_charge', string="Frieght Charge",digits=(6, 2))

    account_to = fields.Char('Account To')


    afb_weight = fields.Float(related='hawb_afb_ID.h_weight',
                       string='Weight', store=True, readonly=True)
    afb_price = fields.Float('Price', digits=(6, 2))
    mawb_a = fields.Many2one(related='hawb_afb_ID.mawb_IDs',
                             string='MAWB NO', store=True, readonly=True)
    # ========= modifying existing fields ==============================================================================





#========= Functions ==================================================page2============================================
    @api.one
    @api.depends('afb_weight','afb_price')
    def _compute_frieght_charge(self):

        return self.afb_weight * self.afb_price



