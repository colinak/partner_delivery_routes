#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Partner Delivery Routes",
    "version": "12.0.1.1.0",
    "category": "Sales",
    "website": "https://github.com/colinak/",
    "author": "Kewitz Colina",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    "depends": [
        'base',
        'hr'
    ],
    "data": [
        'security/ir.model.access.csv',
        'data/weekdays_data.xml',
        'data/job_data.xml',
        'views/partner_delivery_view.xml',
        'views/delivery_routes_view.xml',
        'views/weekdays_view.xml'
    ],
    "demo": [
    ],
}
