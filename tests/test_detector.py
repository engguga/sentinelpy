from sentinel_detector.detector import ThreatDetector


def test_detector_instantiation():
    detector = ThreatDetector()
    assert detector is not None
