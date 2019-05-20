# -*- coding: utf-8 -*-
###############################################################################
#
#   Copyright (C) 2004-today OpenERP SA (<http://www.openerp.com>)
#   Copyright (C) 2016-today Geminate Consultancy Services (<http://geminatecs.com>).
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name' : 'Product Cost Price Calculation',
    'version': '12.0.1',
    'author': 'Geminate Consultancy Services',
    'license': 'Other proprietary',
    'description': """Product Cost Price Calculation:
This module calculate a product cost on your purchase order and base on your 
product tracking if inventory 

if inventory No Tracking --> Average Costing Method, Serial --> Realtime Costing Method, Lot --> Standard Costing Method
    """,
    'website': 'http://www.geminatecs.com',
    'depends' : ['stock_account'],
    'category' : 'product',
    'data': [
        'views/product_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}
