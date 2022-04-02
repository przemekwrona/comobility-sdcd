import matplotlib.pyplot as plot
from abc import ABC, abstractmethod


class BaseDetector(ABC):

    def __init__(self, name):
        self.name = name
        self.detectors = {}

        self.number_of_rows = 0
        self.number_of_detectors = 0
        self.number_of_detected_changes = 0

    @abstractmethod
    def new_detector(self):
        pass

    def add_element(self, key, delay):
        self.number_of_rows = self.number_of_rows + 1

        if self.detectors.get(key) is None:
            self.detectors[key] = self.new_detector()
            self.number_of_detectors = self.number_of_detectors + 1

        detector = self.detectors.get(key)

        is_detected_change = detector.add_element(delay)

        if is_detected_change:
            self.number_of_detected_changes = self.number_of_detected_changes + 1

        return is_detected_change

    def ratio_of_detectors(self):
        return "{:.2f}".format(self.number_of_detectors / self.number_of_rows * 100)

    def get_number_of_rows(self):
        return self.number_of_rows

    def get_average_value_in_window(self, key):
        return self.detectors.get(key).get_average_value_in_window()

    def print_summary(self):
        print("Detector {}.".format(self.name))
        print("Total detected changes: {}.".format(self.number_of_detected_changes))
        print("Number of rows {}.".format(self.number_of_rows))
        print("Number of detectors {}, {}% of rows.\n".format(self.number_of_detectors, self.ratio_of_detectors()))

    def draw_number_of_elements_histogram(self, path):
        elements = [i.get_number_of_elements() for i in self.detectors.values()]

        plot.hist(elements, color="grey")
        plot.grid(True)
        plot.savefig(path)

    def draw_number_of_detections_histogram(self, path):
        detections = [i.get_number_of_detection() for i in self.detectors.values()]

        plot.hist(detections, color="grey")
        plot.grid(True)
        plot.savefig(path)
