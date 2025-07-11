import json
import logging
from datetime import datetime
from pathlib import Path


class Responder:
    def __init__(self, backup_dir="data/backup"):
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        logging.basicConfig(level=logging.INFO)

    def respond(self, events_path):
        try:
            with open(events_path, "r") as f:
                events = json.load(f)
        except FileNotFoundError:
            logging.warning("Events file not found")
            return
        for event in events:
            entry = event.get("entry", "")
            if "failed" in entry.lower():
                self._backup_and_log(entry)

    def _backup_and_log(self, entry):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_file = self.backup_dir / f"event_{timestamp}.log"
        backup_file.write_text(entry)
        logging.info("Backed up suspicious event: %s", backup_file)
