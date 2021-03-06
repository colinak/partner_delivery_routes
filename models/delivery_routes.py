# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api, fields, _
from odoo.exceptions import ValidationError

class DeliveryRoutes(models.Model):
    _name = 'res.delivery.routes'
    _description = 'Rutas de Entrega'
    _order = 'name'
    _rec_name = 'name'

    name = fields.Char(
        string=u"Nombre",
        required=True,
        help=u"Nombre de la Ruta"
    )
    description = fields.Text(
        string=u"Descripción",
        help=u"Descripción de la ruta"
    )
    partner_id = fields.Many2one(
        'hr.employee',
        string="Repartidor",
        domain=[('job_id', '=', 'Repartidor')]
    )
    weekdays_ids = fields.One2many(
        'res.weekdays',
        'day_id',
        string=u"Días de Visita"
    )
    active = fields.Boolean(
        string="Activo?",
        default=True
    )

    _sql_constraints = {
        ('name_unique', 'unique(name)', 
        'Disculpe Ya Existe un Ruta con ese Nombre, Intente con Otro Nombre')        
    }
