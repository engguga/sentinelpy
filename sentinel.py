import argparse

from sentinel_detector.detector import ThreatDetector
from sentinel_forensics.forensics import ForensicAnalyzer
from sentinel_netmon.netmon import NetworkMonitor
from sentinel_responder.responder import Responder


def main():
    parser = argparse.ArgumentParser(
        description="SentinelPy: A professional cyber defense toolkit."
    )
    parser.add_argument("--detect", action="store_true", help="Run threat detection module")
    parser.add_argument("--analyze", action="store_true", help="Run forensic analysis module")
    parser.add_argument("--monitor", action="store_true", help="Run network monitoring module")
    parser.add_argument("--respond", action="store_true", help="Run automated response module")

    args = parser.parse_args()

    if args.detect:
        detector = ThreatDetector()
        detector.run()

    if args.analyze:
        analyzer = ForensicAnalyzer()
        analyzer.run()

    if args.monitor:
        monitor = NetworkMonitor()
        monitor.run()

    if args.respond:
        responder = Responder()
        responder.run()

    if not any(vars(args).values()):
        parser.print_help()


if __name__ == "__main__":
    main()
