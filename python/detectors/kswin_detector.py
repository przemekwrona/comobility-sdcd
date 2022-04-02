from skmultiflow.drift_detection.kswin import KSWIN
from python.detectors.base_detector import BaseDetector


class KSWINDetector(BaseDetector):

    def get_total(self):
        return self.detector.n

    def get_width(self):
        return self.detector.window_size

    def new_detector(self):
        return KSWIN(alpha=0.002, window_size=100, stat_size=30)
