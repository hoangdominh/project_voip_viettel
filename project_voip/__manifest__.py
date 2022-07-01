{
    'name': "Voip Viettel",
    'version': "1.0",
    'author': "Sythil Tech",
    'category': "Tools",
    'summary': "Viettel - VSS",
    'license':'LGPL-3',
    'data': [
        'data/ir_cron.xml',
        'data/voip_ringtone.xml',
        # 'data/voip_settings.xml',

        'views/ir_actions_server_views.xml',
        'views/voip_settings_views.xml',
        'views/voip_codec_views.xml',
        'views/voip_message_compose_views.xml',
        'views/voip_message_template_views.xml',
        'views/voip_ringtone_views.xml',
        'views/voip_account_views.xml',
        'views/voip_account_action_views.xml',
        'views/voip_account_action_transition_views.xml',
        'views/voip_call_views.xml',
        'views/voip_call_template_views.xml',
        'views/voip_call_template_preview_views.xml',
        'views/voip_dialog_views.xml',
        'views/voip_media_views.xml',
        'views/menus.xml'
    ],
    'demo': [],
    'depends': ['web','crm','bus','base'],
    'qweb': [],
    'images':[

    ],
    'installable': True,
    'application': True,
    'auto_install': False
}