from sentinel_netmon.netmon import NetMonitor


def test_netmon_instantiation():
    monitor = NetMonitor()
    assert monitor.interface == "eth0"
