# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    route_id = fields.Many2one(
        'res.delivery.routes',
        string=u"Ruta",
        help=u"Seleccione una ruta para asignar al cliente"
    )
    partner_id = fields.Many2one(
        'res.partner',
        'Cliente',
    )    
    invoices_ids = fields.One2many(
        'account.move',
        'partner_id',
        'Facturas',
        help="Selecciones las facturas"
    )
