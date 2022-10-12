# -*- coding: utf-8 -*-

{
    'name': 'Dental Clinic Management',
    'version': '16.0.1.0.0',
    'summary': 'An app to manage dental clinic',
    'description': "Dental Clinic Management V16",
    'depends': [
        'base', 'contacts', 'stock', 'hr_expense'
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/appointment_tree.xml',
        'views/prescription_form.xml',
        'views/prescription_tree.xml',
        'views/patients_res_partner.xml',
        'views/patient_form.xml',
        'views/patient_tree.xml',
        'views/insurances_form.xml',
        'views/insurances_tree.xml',
        'views/insurance_company.xml',
        'views/treatment_config.xml',
        'views/treatment_form.xml',
        'views/imaging_test_type_tree.xml',
        'views/imaging_test_tree.xml',
        'views/medical_procedures_tree.xml',
        'views/teeth_tree.xml',
        'views/dentist_form.xml',
        'views/treatment_tree.xml',
        'views/appointment_form.xml',
        'views/medicine_config.xml',
        'views/dental_clinic.xml',

    ],

    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
