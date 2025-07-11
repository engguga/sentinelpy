import typer

from sentinel_collector.collector import LogCollector
from sentinel_detector.detector import ThreatDetector
from sentinel_forensics.forensics import ForensicAnalyzer
from sentinel_netmon.netmon import NetworkMonitor
from sentinel_responder.responder import Responder

app = typer.Typer(help="SentinelPy - Cyber Defense Command Line Interface")


@app.command()
def collect(output: str = "data/logs.json"):
    """Collect system logs"""
    LogCollector(output_path=output).collect()
    typer.echo(f"Logs collected and saved to {output}")


@app.command()
def detect(
    input: str = "data/logs.json", output: str = "data/detections.json"
):
    """Detect threats in logs"""
    ThreatDetector(input_path=input, output_path=output).detect()
    typer.echo(f"Detections saved to {output}")


@app.command()
def analyze(
    input: str = "data/detections.json", output: str = "data/forensics.json"
):
    """Perform forensic analysis on detections"""
    ForensicAnalyzer(input_path=input, output_path=output).analyze()
    typer.echo(f"Forensic analysis saved to {output}")


@app.command()
def monitor(
    interface: str = "eth0",
    duration: int = 60,
    output: str = "data/netmon.json",
):
    """Monitor network traffic"""
    NetworkMonitor(
        interface=interface, duration=duration, output_path=output
    ).monitor()
    typer.echo(f"Network monitoring saved to {output}")


@app.command()
def respond(input: str = "data/forensics.json", backup: str = "data/backup"):
    """Trigger automated incident response"""
    Responder(backup_dir=backup).respond(input)
    typer.echo(f"Response actions taken for events in {input}")


if __name__ == "__main__":
    app()
