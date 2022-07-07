# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, _

class Weekdays(models.Model):
    _name = 'res.weekdays'
    _description = u'Días de la semana'
    _order = 'id'
    _rec_name = 'name'

    name = fields.Char(
        string="Nombre",
        required=True,
        help="Nombre del día de la semana"
    )
    day_id = fields.Many2one(
        'res.delivery.routes',
        string=u"Día"
    )
    active = fields.Boolean(
        string="Activo?",
        default=True
    )
