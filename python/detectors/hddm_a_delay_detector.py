from python.detectors.hddm_a_detector import HDDMADetector
from python.detectors.base_delay_detector import BaseDetector


class KSWINDelayDetector(BaseDetector):

    def new_detector(self):
        return HDDMADetector()
