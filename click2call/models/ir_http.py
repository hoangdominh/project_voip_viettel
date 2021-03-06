# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models
from odoo.http import request

class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        res = super(IrHttp, self).session_info()
        res['click2call_url'] = request.env['ir.config_parameter'].sudo().get_param('click2call.api.endpoint')
        res['premium_extension'] = request.env.user.premium_extension
        return res
