## SentinelPy – Cyber Defense Suite

SentinelPy is a professional-grade, modular Python suite designed for cybersecurity defense. It offers comprehensive capabilities for log collection, threat detection, automated response, forensic analysis, network monitoring, and a real-time web dashboard. Built to support both Linux and Windows environments, SentinelPy adheres to best practices in software engineering, code quality, testing, and documentation.

## Features

    Log Collection: Aggregates and normalizes system logs from Linux and Windows, storing data for in-depth analysis.

    Detection Engine: Implements rule-based detection using YARA signatures alongside heuristic analysis for advanced threat identification.

    Automated Response: Provides automatic process termination, IP blocking via firewall rules, and secure file backups before mitigation actions.

    Forensic Analysis: Creates detailed timelines of events and exports comprehensive reports in JSON and PDF formats.

    Network Monitoring: Performs network traffic sniffing, detects suspicious patterns such as DNS tunneling or data exfiltration, and exports PCAP files.

    Web Dashboard: Offers a real-time alert and log visualization interface with capabilities to configure detection rules and upload files, built with Flask or Streamlit.

## Installation

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Usage

python -m sentinel_collector.collector
python -m sentinel_detector.detector
python -m sentinel_responder.responder
python -m sentinel_forensics.forensics
python -m sentinel_netmon.netmon
python -m sentinel_dashboard.dashboard

## Project Structure

sentinelpy/
├── sentinel_collector/
├── sentinel_detector/
├── sentinel_responder/
├── sentinel_forensics/
├── sentinel_netmon/
├── sentinel_dashboard/
├── data/
├── tests/
├── docs/
├── requirements.txt
├── requirements-dev.txt
├── setup.py
├── README.md
└── .github/workflows/

## Contributing

Contributions are welcome. Please adhere to the project's coding standards, run tests before submitting, and follow the established commit message conventions.
License

This project is licensed under the MIT License.