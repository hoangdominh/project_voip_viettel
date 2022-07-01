# -*- coding: utf-8 -*-
from odoo.http import request

from odoo import api, fields, models

class VoipRingtone(models.Model):

    _name = "voip.ringtone"

    name = fields.Char(string="Name")
    media = fields.Binary(string="Media File")
    media_filename = fields.Char(string="Media Filename")