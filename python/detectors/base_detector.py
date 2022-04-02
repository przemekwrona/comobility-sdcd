from abc import ABC, abstractmethod


class BaseDetector(ABC):

    def __init__(self):
        self.number_of_elements = 0
        self.number_of_detections = 0
        self.detector = self.new_detector()

    @abstractmethod
    def new_detector(self):
        pass

    @abstractmethod
    def get_total(self):
        pass

    @abstractmethod
    def get_width(self):
        pass

    def add_element(self, value):
        self.detector.add_element(value)
        self.number_of_elements = self.number_of_elements + 1

        is_detected_change = self.detector.detected_change()

        if is_detected_change:
            self.number_of_detections = self.number_of_detections + 1

        return is_detected_change

    def get_average_value_in_window(self):
        return self.get_total() / self.get_width()

    def detected_change(self):
        return self.detector.detected_change()

    def get_number_of_elements(self):
        return self.number_of_elements

    def get_number_of_detection(self):
        return self.number_of_detections
