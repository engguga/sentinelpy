from sentinel_responder.responder import Responder


def test_responder_instantiation():
    responder = Responder()
    assert responder is not None


def test_respond_to_threat(monkeypatch):
    responder = Responder()
    events_triggered = []

    def fake_execute_response(event):
        events_triggered.append(event)

    def fake_detect(event):
        if event == "malicious_activity":
            return ["threat_detected"]
        return []

    monkeypatch.setattr(responder, "execute_response", fake_execute_response)
    monkeypatch.setattr(responder.detector, "detect", fake_detect)

    responded = responder.respond("malicious_activity")
    assert responded is True
    assert "malicious_activity" in events_triggered
