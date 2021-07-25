class Employee:
    def __init__(self, employee_id, name, phone, age):
        self.id = employee_id
        self.name = name
        self.phone = phone
        self.age = age

    def get_employee(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'age': self.age
        }


class EmployeeTimeLog:
    def __init__(self, employee_id, enter_date, enter_time):
        self.id = employee_id
        self.date = enter_date
        self.time = enter_time

    def get_employee_time_log(self):
        return {
            'id': self.id,
            'date': self.date,
            'time': self.time
        }
