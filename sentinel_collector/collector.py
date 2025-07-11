import json
import logging
import os
import platform
from datetime import datetime


class LogCollector:
    def __init__(self, output_path="data/logs.json"):
        self.system = platform.system()
        self.output_path = output_path
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        logging.basicConfig(level=logging.INFO)

    def collect(self):
        if self.system == "Linux":
            logs = self._collect_linux_logs()
        elif self.system == "Windows":
            logs = self._collect_windows_logs()
        else:
            logs = []
        self._write_output(logs)

    def _collect_linux_logs(self):
        paths = ["/var/log/auth.log", "/var/log/syslog"]
        logs = []
        for path in paths:
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        logs.append(
                            {
                                "timestamp": datetime.now().isoformat(),
                                "source": path,
                                "entry": line.strip(),
                            }
                        )
        return logs

    def _collect_windows_logs(self):
        if self.system != "Windows":
            return []
        try:
            import win32evtlog

            server = "localhost"
            log_type = "Security"
            hand = win32evtlog.OpenEventLog(server, log_type)
            flags = (
                win32evtlog.EVENTLOG_BACKWARDS_READ
                | win32evtlog.EVENTLOG_SEQUENTIAL_READ
            )
            events = win32evtlog.ReadEventLog(hand, flags, 0)
            logs = []
            for event in events:
                logs.append(
                    {
                        "timestamp": event.TimeGenerated.Format(),
                        "source": log_type,
                        "entry": str(event.StringInserts),
                    }
                )
            return logs
        except Exception:
            return []

    def _write_output(self, logs):
        with open(self.output_path, "w") as f:
            json.dump(logs, f, indent=2)
