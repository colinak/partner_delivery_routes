# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api, fields, _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('partner_id')
    def _compute_route(self):
        if self.partner_id:
            self.route_id = self.partner_id.route_id

    route_id = fields.Many2one(
        'res.delivery.routes',
        compute="_compute_route",
        store=True,
        string=u"Ruta",
        help=u"Seleccione una ruta para asignar al cliente"
    )

    def get_total_quantity(self):
            total_quantity = 0
            for rec in self.order_line:
                total_quantity += rec.product_uom_qty
            return total_quantity
