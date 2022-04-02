from datetime import datetime

from python.plot.warsaw_map import warsaw_stops

ONE_DAY = 24 * 60 * 60


class VehicleDelayBetweenStops:
    def __init__(self, city_code, course_identifier, line, vehicle_number, current_stop_id, current_stop_name,
                 current_stop_x, current_stop_y, delay_in_seconds, time,
                 previous_stop_id, previous_stop_name, previous_stop_x, previous_stop_y, delay_in_seconds_minus_1_stop,
                 time_minus_1_stop, delta_delay_in_seconds, delay_at_stop_name, delay_at_stop_id):
        self.city_code = city_code
        self.course_identifier = course_identifier
        self.line = line
        self.vehicle_number = vehicle_number

        self.current_stop_id = current_stop_id
        self.current_stop_name = current_stop_name
        self.current_stop_x = current_stop_x
        self.current_stop_y = current_stop_y
        self.delay_in_seconds = delay_in_seconds
        self.time = time

        self.previous_stop_id = previous_stop_id
        self.previous_stop_name = previous_stop_name
        self.previous_stop_x = previous_stop_x
        self.previous_stop_y = previous_stop_y
        self.delay_in_seconds_minus_1_stop = delay_in_seconds_minus_1_stop
        self.time_minus_1_stop = time_minus_1_stop

        self.delta_delay_in_seconds = delta_delay_in_seconds
        self.delay_at_stop_name = delay_at_stop_name
        self.delay_at_stop_id = delay_at_stop_id

    def __str__(self):
        return "{city_code} {time} ({previous_stop_id} {previous_stop_name}) -> ({current_stop_id} {current_stop_name}). Delay: {delay}, delay on previous stop: {delay_minus_1_stop}, delta delay: {delta_delay}".format(
            city_code=self.city_code, time=self.time, line=self.line, previous_stop_id=self.previous_stop_id,
            previous_stop_name=self.previous_stop_name, current_stop_id=self.current_stop_id,
            current_stop_name=self.current_stop_name,
            delay=self.delay_in_seconds,
            delay_minus_1_stop=self.delay_in_seconds_minus_1_stop,
            delta_delay=self.delta_delay_in_seconds)

    def get_key_by_type(self, key_type):
        if key_type == "TWO_STOPS":
            return self.get_bus_stops_key()
        if key_type == "TWO_STOPS_AND_HOUR":
            return self.get_bus_stops_key_by_hour()

        raise Exception("key_type is not defined")

    def get_bus_stops_key(self):
        return "{city_code}::{previous_stop_id}->{current_stop_id}".format(
            city_code=self.city_code,
            previous_stop_id=self.previous_stop_id,
            current_stop_id=self.current_stop_id)

    def get_bus_stops_key_by_hour(self):
        return "{city_code}::{previous_stop_id}->{current_stop_id}::{hour}:00".format(
            city_code=self.city_code,
            previous_stop_id=self.previous_stop_id,
            current_stop_id=self.current_stop_id,
            hour=self.get_hour())

    def get_row(self, algorithm_name, detector_name, average_delay):
        return [algorithm_name, detector_name, self.city_code, self.course_identifier, self.line, self.vehicle_number,
                self.current_stop_id, self.current_stop_name, self.current_stop_x, self.current_stop_y,
                self.get_delay(), self.time,
                self.previous_stop_id, self.previous_stop_name, self.previous_stop_x, self.previous_stop_y,
                self.get_delay_minus_1_stop(),
                self.time_minus_1_stop, self.get_delta_delay(), self.delay_at_stop_name,
                self.delay_at_stop_id, average_delay]

    def get_hour(self):
        return "{:02d}".format(self.time.hour)

    def get_delay(self):
        if abs(self.delay_in_seconds - ONE_DAY) < 1 * 60 * 60:
            return self.delay_in_seconds - ONE_DAY
        else:
            return self.delay_in_seconds

    def get_delay_minus_1_stop(self):
        if abs(self.delay_in_seconds_minus_1_stop - ONE_DAY) < 1 * 60 * 60:
            return self.delay_in_seconds_minus_1_stop - ONE_DAY
        else:
            return self.delay_in_seconds_minus_1_stop

    def get_delta_delay(self):
        if abs(self.delta_delay_in_seconds - ONE_DAY) < 1 * 60 * 60:
            return self.delta_delay_in_seconds - ONE_DAY
        else:
            return self.delta_delay_in_seconds


def build_from_row(row):
    previous_stop = warsaw_stops.get_stop(row[8])
    current_stop = warsaw_stops.get_stop(row[4])
    return VehicleDelayBetweenStops(city_code=row[0],
                                    course_identifier=row[1],
                                    line=row[2],
                                    vehicle_number=row[3],
                                    current_stop_id=row[4],
                                    current_stop_name=row[5],
                                    current_stop_x=current_stop[4],
                                    current_stop_y=current_stop[5],
                                    time=datetime.fromisoformat(row[6]),
                                    delay_in_seconds=int(row[7]),
                                    previous_stop_id=row[8],
                                    previous_stop_name=row[9],
                                    previous_stop_x=previous_stop[4],
                                    previous_stop_y=previous_stop[5],
                                    time_minus_1_stop=datetime.fromisoformat(row[10]) if row[10] != '' else None,
                                    delay_in_seconds_minus_1_stop=int(row[11]) if row[11] != '' else 0,
                                    delta_delay_in_seconds=int(row[12]) if row[12] != '' else 0,
                                    delay_at_stop_id=row[13],
                                    delay_at_stop_name=row[14])
