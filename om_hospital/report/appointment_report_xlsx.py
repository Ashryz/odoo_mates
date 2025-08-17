from odoo import models


class AppointmentReportXlsx(models.AbstractModel):
    _name = 'report.om_hospital.appointment_report_template_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, appointments):
        sheet = workbook.add_worksheet('Appointments')
        # Define formats
        title_format = workbook.add_format({'bold': True, 'align': 'center', 'font_size': 14})
        header_format = workbook.add_format({'bold': True, 'align': 'center', 'border': 1})
        normal_format = workbook.add_format({'align': 'left', 'border': 1})

        # Write the report title
        sheet.merge_range('A1:F1', 'Appointment Details', title_format)
        # Write patient name and  date range
        form_data = data['form_data']
        sheet.write('A2', f"Patient: ", normal_format)
        sheet.merge_range('B2:F2', form_data['patient_id'][1], normal_format)

        sheet.write('A3', f"Date From: ", normal_format)
        if form_data.get('date_from'):
            sheet.merge_range('B3:F3', form_data['date_from'], normal_format)
        else:
            sheet.merge_range('B3:F3','', normal_format)
        sheet.write('A4', f"Date To: ", normal_format)
        if form_data.get('date_to'):
            sheet.merge_range('B4:KF', form_data['date_to'], normal_format)
        else:
            sheet.merge_range('B4:F4','', normal_format)

        headers = ['ref', 'gender', 'state']
        # Write the column headers starting from row 5
        for col_num, header in enumerate(headers, start=1):
            sheet.write(4, col_num, header, header_format)

        # Write data to the report starting from row 6
        row_num = 5
        appointments = data['appointments']
        for line in appointments:
            sheet.write(row_num, 1, line['ref'], normal_format)
            sheet.write(row_num, 2, line['gender'], normal_format)
            sheet.write(row_num, 3, line['state'], normal_format)
            row_num += 1
