from random import randint
import queue
from odoo import models,fields

class VoipAccount(models.Model):

    _name = "voip.account"

    name = fields.Char(string="Name", required="True")

    state = fields.Selection([('new','New'), ('inactive','Inactive'), ('active','Active')], default="new", string="State")

    type = fields.Selection([('sip', 'SIP'), ('xmpp', 'XMPP')], default="sip", string="Account Type")

    address = fields.Char(string="SIP Address", required="True")

    password = fields.Char(string="SIP Password", required="True")

    auth_username = fields.Char(string="Auth Username")

    username = fields.Char(string="Username", required="True")

    domain = fields.Char(string="Domain", required="True")

    voip_display_name = fields.Char(string="Display Name", default="Odoo")

    outbound_proxy = fields.Char(string="Outbound Proxy")

    port = fields.Integer(string="Port", default="5060")

    call_dialog_id = fields.Many2one('voip.dialog', string="Call Dialog")

    verified = fields.Boolean(string="Verified")

    bind_port = fields.Integer(string="Bind Port")

    action_id = fields.Many2one('voip.account.action', string="Call Action")

    # bind_port = fields.Integer(string="Bind Port", help="A record of what port the SIP session is bound on so we can deregister if neccassary")
