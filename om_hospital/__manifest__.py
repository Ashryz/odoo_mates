{
    "name": "Hospital Management",
    "summary": " hospital management system",
    "description": """ """,
    "author": " Tarek Ashry",
    "depends": ['mail', 'product', 'report_xlsx'],
    "data": [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'data/sequence_data.xml',
        'views/menu.xml',
        'wizard/cancel_appointment.xml',
        'wizard/appointment_report_wizard.xml',
        'views/patient_view.xml',
        'views/patient_female_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
        'views/res_config_settings_views.xml',
        'report/reports.xml',
        'report/appointment_report_template.xml',

    ],
    "assets":{
      "web.assets_backend":[
          "om_hospital/static/src/xml/list_controller.xml",
          "om_hospital/static/src/js/list_controller.js",
      ]
    },
    "application": True,
    "auto_install": False,
    'license': 'LGPL-3'
}
