from skmultiflow.drift_detection.hddm_a import HDDM_A
from python.detectors.base_detector import BaseDetector


class HDDMADetector(BaseDetector):

    def get_total(self):
        return self.detector.total_n

    def get_width(self):
        return self.detector.total_n

    def new_detector(self):
        return HDDM_A(drift_confidence=0.002, warning_confidence=0.005, two_side_option=True)
