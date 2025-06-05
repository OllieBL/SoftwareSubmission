class Employee:
    def __init__(self, name, employee_id, hourly_wage, shift_hours):
        self.name = name
        self.employee_id = employee_id
        self.hourly_wage = hourly_wage
        self.shift_hours = shift_hours
        self.clock_in_time = 0

    def clock_in(self, time):
        self.clock_in_time = time

    def clock_out(self, time):
        self.shift_hours = time - self.clock_in_time
        self.clock_in_time = 0

    def get_pay(self):
        return 10 * self.shift_hours
    
class Cashier(Employee):
    def __init__(self, name, employee_id, hourly_wage, shift_hours):
        super().__init__(name, employee_id, hourly_wage, shift_hours)
        self.money_made = 0

    def clock_in(self, time):
        super().clock_in(time)
    
    def clock_out(self, time):
        super().clock_out(time)
    
    def get_pay(self):
        return super().get_pay()
    
    def get_money_made(self):
        return self.money_made
    
    def made_sale(self, profit):
        self.money_made += profit

class Cook(Employee):
    def __init__(self, name, employee_id, hourly_wage, shift_hours):
        super().__init__(name, employee_id, hourly_wage, shift_hours)
        self.orders_cooked = 0

    def clock_in(self, time):
        super().clock_in(time)
    
    def clock_out(self, time):
        super().clock_out(time)
    
    def get_pay(self):
        return super().get_pay()
    
    def cooked_order(self):
        self.orders_cooked += 1

    def get_orders_cooked(self):
        return self.orders_cooked
    
class Cleaner(Employee):
    def __init__(self, name, employee_id, hourly_wage, shift_hours):
        super().__init__(name, employee_id, hourly_wage, shift_hours)
        self.areas_cleaned = 0

    def clock_in(self, time):
        super().clock_in(time)
    
    def clock_out(self, time):
        super().clock_out(time)
    
    def get_pay(self):
        return super().get_pay()
    
    def cleaned_area(self):
        self.areas_cleaned += 1

    def get_areas_cleaned(self):
        return self.areas_cleaned