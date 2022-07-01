from odoo import api, fields, models
import threading
import time
import datetime
import struct
import base64
from random import randint
import queue

class VoipAccountAction(models.Model):

    _name = "voip.account.action"
    _description = "VOIP Account Action"

    voip_dialog_id = fields.Many2one('voip.dialog', string="Voip Dialog")
    name = fields.Char(string="Name")
    start = fields.Boolean(string="Start Action")
    account_id = fields.Many2one('voip.account', string="VOIP Account")
    action_type_id = fields.Many2one('voip.account.action.type', string="Call Action", required="True")
    action_type_internal_name = fields.Char(related="action_type_id.internal_name", string="Action Type Internal Name")
    recorded_media_id = fields.Many2one('voip.media', string="Recorded Message")
    user_id = fields.Many2one('res.users', string="Call User")
    from_transition_ids = fields.One2many('voip.account.action.transition', 'action_to_id', string="Source Transitions")
    to_transition_ids = fields.One2many('voip.account.action.transition', 'action_from_id', string="Destination Transitions")

class VoipAccountActionTransition(models.Model):

    _name = "voip.account.action.transition"
    _description = "VOIP Call Action Transition"

    name = fields.Char(string="Name")
    trigger = fields.Selection([('dtmf','DTMF Input'), ('auto','Automatic')], default="dtmf", string="Trigger")
    dtmf_input = fields.Selection([('0','0'), ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('8','8'), ('9','9'), ('*','*'), ('#','#')], string="DTMF Input")
    action_from_id = fields.Many2one('voip.account.action', string="From Voip Action")
    action_to_id = fields.Many2one('voip.account.action', string="To Voip Action")

class VoipAccountActionType(models.Model):

    _name = "voip.account.action.type"
    _description = "VOIP Account Action Type"

    name = fields.Char(string="Name")
    internal_name = fields.Char(string="Internal Name", help="function name of code")