class InstancesCounter:

    def __init__(self):
        self.counter_by_date = {}

    def add_instance(self, vehicle_live):
        key = vehicle_live.time.date()
        value = self.counter_by_date.get(key)

        if value is None:
            value = 0

        value = value + 1

        self.counter_by_date[key] = value

    def print(self):
        print(self.counter_by_date)
