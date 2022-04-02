from python.detectors.kswin_detector import KSWINDetector
from python.detectors.base_delay_detector import BaseDetector


class KSWINDelayDetector(BaseDetector):

    def new_detector(self):
        return KSWINDetector()
