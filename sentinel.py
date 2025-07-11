import argparse
import logging

from sentinel_detector.detector import ThreatDetector
from sentinel_forensics.forensics import ForensicAnalyzer
from sentinel_netmon.netmon import NetMonitor
from sentinel_responder.responder import Responder

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_detection():
    detector = ThreatDetector()
    result = detector.detect("sample_data")
    logger.info(f"Detection result: {result}")


def run_monitor():
    monitor = NetMonitor()
    monitor.monitor()


def run_response():
    responder = Responder()
    responder.respond("malicious_event")


def run_analysis():
    analyzer = ForensicAnalyzer()
    result = analyzer.analyze("log_data")
    logger.info(f"Analysis result: {result}")


def main():
    parser = argparse.ArgumentParser(prog="sentinel", description="SentinelPy CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("detect", help="Run threat detection")
    subparsers.add_parser("monitor", help="Monitor network activity")
    subparsers.add_parser("respond", help="Trigger automated response")
    subparsers.add_parser("analyze", help="Run forensic analysis")

    args = parser.parse_args()

    if args.command == "detect":
        run_detection()
    elif args.command == "monitor":
        run_monitor()
    elif args.command == "respond":
        run_response()
    elif args.command == "analyze":
        run_analysis()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
