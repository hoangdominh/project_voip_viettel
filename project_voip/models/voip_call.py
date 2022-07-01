import time
from random import randint
from hashlib import sha1
#import ssl
#from dtls import do_patch
#from dtls.sslconnection import SSLConnection
import hmac
import hashlib
import random
import string
import passlib
import struct
import zlib
import re
from odoo.exceptions import UserError
import binascii
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT
from odoo import api, fields, models

class VoipCall(models.Model):

    _name = "voip.call"
    _order = 'create_date desc'

    from_address = fields.Char(string="From Address")

    from_partner_id = fields.Many2one('res.partner', string="From Partner", help="From can be blank if the call comes from outside of the system")

    from_partner_sdp = fields.Text(string="From Partner SDP")

    partner_id = fields.Many2one('res.partner', string="(OBSOLETE)To Partner")

    to_address = fields.Char(string="To Address")

    to_partner_id = fields.Many2one('res.partner', string="To Partner", help="To partner can be blank if the source is external and no record with mobile or sip is found")

    status = fields.Selection([('pending','Pending'),
                               ('missed','Missed'), ('accepted','Accepted'),
                               ('rejected','Rejected'),('active','Active'),
                               ('over','Complete'), ('failed','Failed'),
                               ('busy','Busy'), ('cancelled','Cancelled')],
                              string='Status', default="pending", help="Pending = Calling person\nActive = currently talking\nMissed = Call timed out\nOver = Someone hit end call\nRejected = Someone didn't want to answer the call")

    ring_time = fields.Datetime(string="Ring Time", help="Time the call starts dialing")

    start_time = fields.Datetime(string="Start Time", help="Time the call was answered (if answered)")

    end_time = fields.Datetime(string="End Time", help="Time the call end")

    duration = fields.Char(string="Duration", help="Length of the call")

    transcription = fields.Text(string="Transcription", help="Automatic transcription of the call")

    notes = fields.Text(string="(OBSOLETE)Notes", help="Additional comments outside the transcription (use the chatter instead of this field)")

    client_ids = fields.One2many('voip.call.client', 'vc_id', string="Client List")

    type = fields.Selection([('internal','Internal'),('external','External')], string="Type")

    mode = fields.Selection([('videocall','video call'),
                             ('audiocall','audio call'),
                             ('screensharing','screen sharing call')],
                            string="Mode",
                            help="This is only how the call starts, i.e a video call can turn into a screen sharing call mid way")

    sip_tag = fields.Char(string="SIP Tag")

    voip_account = fields.Many2one('voip.account', string="VOIP Account")

    to_audio = fields.Binary(string="Audio")

    to_audio_filename = fields.Char(string="(OBSOLETE)Audio Filename")

    media = fields.Binary(string="Media")

    media_filename = fields.Char(string="Media Filename")

    server_stream_data = fields.Binary(string="Server Stream Data", help="Stream data sent by the server, e.g. automated call")

    media_url = fields.Char(string="Media URL", compute="_compute_media_url")

    codec_id = fields.Many2one('voip.codec', string="Codec")

    direction = fields.Selection([('internal','Internal'), ('incoming','Incoming'), ('outgoing','Outgoing')], string="Direction")

    sip_call_id = fields.Char(string="SIP Call ID")

    ice_username = fields.Char(string="ICE Username")

    ice_password = fields.Char(string="ICE Password")

    call_dialog_id = fields.Many2one('voip.codec', string="Call Dialog")


class VoipCallClient(models.Model):
    _name = "voip.call.client"

    vc_id = fields.Many2one('voip.call', string="VOIP Call")
    partner_id = fields.Many2one('res.partner', string="Partner")
    sip_address = fields.Char(string="SIP Address")
    name = fields.Char(string="Name", help="Can be a number if the client is from outside the system")
    model = fields.Char(string="Model")
    record_id = fields.Integer(string="Record ID")
    state = fields.Selection([('invited', 'Invited'), ('joined', 'joined'), ('media_access', 'Media Access')],
                             string="State", default="invited")
    sdp = fields.Char(string="SDP")
    sip_invite = fields.Char(string="SIP INVITE Message")
    sip_addr = fields.Char(string="Address")
    sip_addr_host = fields.Char(string="SIP Address Host")
    sip_addr_port = fields.Char(string="SIP Address Port")
    audio_media_port = fields.Integer(string="Audio Media Port")
    audio_stream = fields.Binary(string="Audio Stream")
