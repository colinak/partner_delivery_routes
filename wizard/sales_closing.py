# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class SaleClosingReportWizard(models.TransientModel):
    _name = 'account.invoice.closing.report.wizard'
    _description = 'Reporte de Ventas'

    route_id = fields.Many2one(
        'res.delivery.routes',
        string=u"Ruta",
        required=True,
        help=u"Seleccione una ruta para Filtrar clientes"
    )
    partner_ids = fields.Many2many(
        'res.partner',
        'partner_route_rel',
        'partner_id',
        'route_id',
        'Clientes',
        required=True,
        help="Seleccione los clientes"
    )
    partner_id = fields.Many2one(
        'res.partner',
        string="Cliente"
    )


    @api.onchange('route_id')
    def _onchange_route_id(self):
        if self.route_id:
            self.partner_ids = [(5)]


    def get_report(self):
        if len(self.partner_ids) > 0:
            report = self.env['ir.actions.report']._get_report_from_name(
                'partner_delivery_routes.report_sales_closing_template'
            )
            return report.report_action(docids=self)
        else:
            raise UserError(_(
                """Disculpe debe Seleccionar por lo menos
                un Cliente para Poder Generar el Reporte"""        
            ))

