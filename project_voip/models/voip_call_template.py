 # -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)
import functools
from werkzeug import urls
from datetime import datetime
import base64

from odoo import api, fields, models, tools

class VoipCallTemplate(models.Model):

    _name = "voip.call.template"

    name = fields.Char(string="Name")

    model_id = fields.Many2one('ir.model', string="Applies to", help="The kind of document with with this template can be used")

    voip_account_id = fields.Many2one('voip.account', string="VOIP Account")

    to_address = fields.Char(string="To Address", help="Use placeholders")

    media_id = fields.Many2one('voip.media', string="Media")

    codec_id = fields.Many2one('voip.codec', string="Codec")

    call_dialog_id = fields.Many2one('voip.dialog', string="Call Dialog")

    type = fields.Selection(
        [('prerecorded','Pre Recorded')],
        string="Template Type",
        default="prerecorded")

    model_object_field_id = fields.Many2one('ir.model.fields', string="Field", help="Select target field from the related document model.\nIf it is a relationship field you will be able to select a target field at the destination of the relationship.")

    sub_object_id = fields.Many2one('ir.model', string='Sub-model', readonly=True, help="When a relationship field is selected as first field, this field shows the document model the relationship goes to.")

    sub_model_object_field_id = fields.Many2one('ir.model.fields', string='Sub-field', help="When a relationship field is selected as first field, this field lets you select the target field within the destination document model (sub-model).")

    null_value = fields.Char(string='Default Value', help="Optional value to use if the target field is empty")

    copyvalue = fields.Char(string='Placeholder Expression', help="Final placeholder expression, to be copy-pasted in the desired template field.")