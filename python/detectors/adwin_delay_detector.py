from python.detectors.adwin_detector import ADWINDetector
from python.detectors.base_delay_detector import BaseDetector


class ADWINDelayDetector(BaseDetector):

    def new_detector(self):
        return ADWINDetector()
