# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from odoo import api, fields, models, tools
from odoo.exceptions import UserError

class VoipCallTemplatePreview(models.TransientModel):

    _name = "voip.call.template.preview"

    @api.model
    def _get_records(self):
        """ Returns the first 10 records of the VOIP call template's model """

        #Get call template through context since we can't get it through self
        call_template = self.env['voip.call.template'].browse( self._context.get('default_call_template_id') )

        if call_template:
            records = self.env[call_template.model_id.model].search([], limit=10)
            return records.name_get()
        else:
            return []

    call_template_id = fields.Many2one('voip.call.template', string="Call Template")

    rec_id = fields.Selection(_get_records, string="Record")