# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging
_logger = logging.getLogger(__name__)
from openerp.http import request
from openerp import http

class digitsConfiguration(models.Model):
    _name = 'digits.configuration'
    
    digits_consumer_key = fields.Char('CONSUMER KEY (API KEY)', size=256)
    
    @api.model
    def get_digits_consumer_key(self, values):
        userInfo = http.request.env['res.users'].search([('id','=',request.session.uid)])
        return {
                   'type'     : 'ir.actions.act_url',
                   'target'   : 'new',
                    'url' : 'https://www.allipcloud.com/consumer/key/form?url='+request.httprequest.host_url+'&appname='+str(userInfo[0].company_id.name.encode('ascii','ignore'))+'&email='+str(userInfo[0].company_id.email.encode('ascii','ignore'))+'&street='+str(userInfo[0].company_id.street.encode('ascii','ignore'))+'&street2='+str(userInfo[0].company_id.street2.encode('ascii','ignore'))+'&city='+str(userInfo[0].company_id.city.encode('ascii','ignore'))+'&state='+str(userInfo[0].company_id.state_id.name.encode('ascii','ignore'))+'&country='+str(userInfo[0].company_id.country_id.name.encode('ascii','ignore'))+'&phone='+str(userInfo[0].company_id.phone.encode('ascii','ignore'))
                }
   
