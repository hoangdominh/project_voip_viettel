The technical name of this module is **asterisk_click2dial**, but this module
implements much more than a simple *click2dial* ! This module adds 3
functionalities:

1. It adds a *Dial* button in the partner form view so that users can directly
   dial a phone number through Asterisk. This feature is usually known as
   *click2dial*. Here is how it works :

   * In Odoo, the user clicks on the *Dial* button next to a phone number
     field in the partner form view (or any form view with a phone number).

   * Odoo connects to the Asterisk Manager Interface and Asterisk makes the
     user's phone ring.

   * The user answers his own phone (if he doesn't, the process stops here).

   * Asterisk dials the phone number found in Odoo in place of the user.

   * If the remote party answers, the user can talk to his correspondent.

2. It adds the ability to show the name of the calling party on the screen of
   your IP phone on incoming phone calls if the presented phone number is
   present in the partner/leads/employees/... of Odoo. Here is how it works:

   * On incoming phone calls, the Asterisk dialplan executes an AGI script
     **set_name_incoming_timeout.sh**.

   * The *set_name_incoming_timeout.sh* script calls the *set_name_agi.py*
     script with a short timeout.

   * The *set_name_agi.py* script will make an XML-RPC request on the Odoo
     server to try to find the name of the person corresponding to the phone
     number presented by the calling party.

   * If it finds the name, it is set as the CallerID name of the call, so as
     to be presented on the IP phone of the user.

   It also works on outgoing calls, so as to display the name of the callee on
   the SIP phone of the caller. For that, you should use the script
   *set_name_outgoing_timeout.sh*.

3. It adds a phone icon (*Open Caller*) in the top menu bar
   to get the partner/lead/candidate/event registrations
   corresponding to the calling party in one click. Here is how it works :

   * When the user clicks on the phone icon, Odoo sends a query to the
     Asterisk Manager Interface to get a list of the current phone calls.

   * If it finds a phone call involving the user's phone, it gets the phone
     number of the calling party.

   * It searches the phone number of the calling party in the
     Partners/Leads/Candidates/Event Registrations of Odoo. If a record matches,
     it takes you to the form view of this record. If no record matchs, it
     opens a wizard which proposes to create a new Partner with the presented
     phone number as *Phone* or *Mobile* number or update an existing Partner.

   It is possible to get a pop-up of the record corresponding to the calling
   party without any action from the user via the module *base_phone_popup*.

A detailed documentation for this module is available on `this page <http://www.akretion.com/products-and-services/openerp-asterisk-voip-connector>`_ of Akretion's Web site.
