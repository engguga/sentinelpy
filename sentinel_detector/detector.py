import json
from datetime import datetime


class ThreatDetector:
    def __init__(
        self, input_path="data/logs.json", output_path="data/detections.json"
    ):
        self.input_path = input_path
        self.output_path = output_path

    def detect(self):
        with open(self.input_path, "r") as f:
            logs = json.load(f)
        detections = [log for log in logs if "failed" in log["entry"].lower()]
        for detection in detections:
            detection["detected_at"] = datetime.now().isoformat()
        with open(self.output_path, "w") as f:
            json.dump(detections, f, indent=2)
