
from network_as_code.models.device import DeviceIpv4Addr

def test_serializing_device_with_network_id(client):
    device = client.devices.get("test_device_id")

    assert device.to_json_dict() == { "networkAccessIdentifier": "test_device_id" }

def test_serializing_device_with_ipv4_public_address(client):
    device = client.devices.get("test_device_id", ipv4_address="1.1.1.2")

    assert device.to_json_dict() == {
        "networkAccessIdentifier": "test_device_id",
        "ipv4Address": {
            "publicAddress": "1.1.1.2"
        }
    }

def test_serializing_device_with_ipv4_private_address(client):
    device = client.devices.get("test_device_id", ipv4_address=DeviceIpv4Addr(private_address="1.1.1.2"))

    assert device.to_json_dict() == {
        "networkAccessIdentifier": "test_device_id",
        "ipv4Address": {
            "privateAddress": "1.1.1.2"
        }
    }

def test_serializing_device_with_ipv4_public_port(client):
    device = client.devices.get("test_device_id", ipv4_address=DeviceIpv4Addr(public_port=80))

    assert device.to_json_dict() == {
        "networkAccessIdentifier": "test_device_id",
        "ipv4Address": {
            "publicPort": 80
        }
    }

def test_serializing_device_with_ipv6(client):
    device = client.devices.get("test_device_id", ipv6_address="2345:0425:2CA1:0000:0000:0567:5673:23b5")

    assert device.to_json_dict() == {
        "networkAccessIdentifier": "test_device_id",
        "ipv6Address": "2345:0425:2CA1:0000:0000:0567:5673:23b5"
    }

def test_serializing_device_with_phone_number(client):
    device = client.devices.get("test_device_id", phone_number="+1 206 555 0100")

    assert device.to_json_dict() == {
        "networkAccessIdentifier": "test_device_id",
        "phoneNumber": "+1 206 555 0100"
    }