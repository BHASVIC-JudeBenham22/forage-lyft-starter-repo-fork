from battery.battery import Battery


class CapuletEngine(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def battery_should_be_serviced(self):
        return self.last_service_date.replace(year=original_date.year + 2) < self.current_date
