# -*- coding: utf-8 -*-
import socket
import threading
import logging

_logger = logging.getLogger(__name__)
from lxml import etree
import re
from odoo.exceptions import UserError

from odoo import api, fields, models

class VoipMessageCompose(models.TransientModel):
    _name = "voip.message.compose"

    type = fields.Char(string="Message Type")

    sip_account_id = fields.Many2one('voip.account', string="SIP Account")

    message_template_id = fields.Many2one('voip.message.template', string="Message Template")

    partner_id = fields.Many2one('res.partner', string="Partner (OBSOLETE)")

    model = fields.Char(string="Model")

    record_id = fields.Integer(string="Record ID")

    to_address = fields.Char(string="To Address")

    message = fields.Text(string="Message")
