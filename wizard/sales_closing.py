# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class SaleClosingReportWizard(models.TransientModel):
    _name = 'account.invoice.closing.report.wizard'

    route_id = fields.Many2one(
        'res.delivery.routes',
        string=u"Ruta",
        required=True,
        help=u"Seleccione una ruta para Filtrar clientes"
    )
    partner_ids = fields.One2many(
        'res.partner',
        'partner_id',
        'Clientes',
        required=True,
        help="Seleccione los clientes"
    )

    @api.multi
    def get_report(self):
        if len(self.partner_ids) > 0:
            report = self.env['ir.actions.report']._get_report_from_name(
                'partner_delivery_routes.report_sales_closing_template'
            )
            return report.report_action(docids=self)
        else:
            raise ValidationError(
                """Disculpe debe Seleccionar por lo menos
                un Cliente para Poder Generar el Reporte"""        
            )

