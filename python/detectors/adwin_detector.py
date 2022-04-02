from skmultiflow.drift_detection.adwin import ADWIN
from python.detectors.base_detector import BaseDetector


class ADWINDetector(BaseDetector):

    def get_total(self):
        return self.detector.total

    def get_width(self):
        return self.detector.width

    def new_detector(self):
        return ADWIN(delta=.002)
