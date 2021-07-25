import functions


def sample():
    print('sample')


menu_list = {
    'ae':
        {
            'name': 'Add employee manually',
            'func': functions.add_employee
        },
    'aef':
        {
            'name': 'Add employee from file',
            'func': functions.add_employee_file
        },
    'de':
        {
            'name': 'Delete employee manually',
            'func': functions.delete_employee
        },
    'def':
        {
            'name': 'Delete employee from file',
            'func': functions.delete_employee_file
        },
    'ma':
        {
            'name': 'Mark attendance',
            'func': functions.mark_attendance
        },
    'gr':
        {
            'name': 'Generate attendance report',
            'func': functions.generate_report
        },
    'prm':
        {
            'name': 'Print a report for current month',
            'func': functions.print_report_month
        },
    'prl':
        {
            'name': 'Print a report for all late employees',
            'func': functions.print_report_late
        }
}
