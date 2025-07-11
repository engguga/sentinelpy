import datetime
import logging

from sentinel_detector.detector import ThreatDetector

logger = logging.getLogger(__name__)


class Responder:
    def __init__(self):
        self.detector = ThreatDetector()
        self.last_response_time = None

    def should_respond(self):
        if self.last_response_time is None:
            return True
        elapsed = datetime.datetime.now() - self.last_response_time
        return elapsed.total_seconds() > 60

    def respond(self, event):
        if not self.should_respond():
            logger.info("Response cooldown active, skipping response.")
            return False
        # Usa detect para identificar ameaças
        if bool(self.detector.detect(event)):
            logger.info(f"Responding to threat: {event}")
            self.execute_response(event)
            self.last_response_time = datetime.datetime.now()
            return True
        logger.debug("No threat detected, no response needed.")
        return False

    def execute_response(self, event):
        # Aqui implemente a resposta real (alerta, bloqueio, etc)
        logger.info(f"Executing response actions for event: {event}")
        print(f"Response executed for event: {event}")
