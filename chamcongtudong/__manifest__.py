{
    "name": "Cham cong tu dong",
    "version": "15.0.1.0.0",
    "category": "Human Resources",
    "summary": "Close stale Attendances",
    "website": "https://github.com/OCA/hr-attendance",
    "author": "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["hr_attendance_reason"],
    "data": [
        "data/hr_attendance_reason.xml",
        "data/hr_attendance.xml",
        "data/res_company.xml",
        "views/hr_attendance_view.xml",
        "views/hr_employee.xml",
        "views/res_config_settings_view.xml",
    ],
}
