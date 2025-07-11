from sentinel_detector.detector import Detector


def test_detector_instantiation():
    detector = Detector()
    assert detector.rules_path == "data/yara_rules.yar"
