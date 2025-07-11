from sentinel_forensics.forensics import ForensicAnalyzer


def test_forensic_analyzer_basic():
    analyzer = ForensicAnalyzer()
    assert analyzer is not None
