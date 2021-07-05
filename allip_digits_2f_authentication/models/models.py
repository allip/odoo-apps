# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)
from odoo.http import request
from odoo import http


class digitsConfiguration(models.Model):
    _name = 'digits.configuration'

    digits_consumer_key = fields.Char('CONSUMER KEY (API KEY)', size=256)

    @api.model
    def get_digits_consumer_key(self, values):
        userInfo = http.request.env['res.users'].search([('id', '=', request.session.uid)])
        url = 'https://www.allipcloud.com/consumer/key/form?url=' + request.httprequest.host_url +\
            '&appname=' + (userInfo[0].company_id.name or '') +\
            '&email=' + (userInfo[0].company_id.email or '') +\
            '&street=' + (userInfo[0].company_id.street or '') +\
            '&street2=' + (userInfo[0].company_id.street2 or '') +\
            '&city=' + (userInfo[0].company_id.city or '') +\
            '&state=' + (userInfo[0].company_id.state_id.name or '') +\
            '&country=' + (userInfo[0].company_id.country_id.name or '') +\
            '&phone=' + (userInfo[0].company_id.phone or '')

        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': url.encode('ascii', 'ignore')
        }
