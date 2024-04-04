from pytest_httpx import httpx_mock
import pytest
import json
from httpx import HTTPError

from network_as_code.errors import AuthenticationException, NotFound, ServiceError, APIError


from network_as_code.models.device import Device, DeviceIpv4Addr

@pytest.fixture
def device(client) -> Device:
    device = client.devices.get("testuser@open5glab.net", ipv4_address = DeviceIpv4Addr(public_address="1.1.1.2", private_address="1.1.1.2", public_port=80))
    return device

@pytest.fixture
def device_with_just_public_ipv4(client) -> Device:
    device = client.devices.get("testuser@open5glab.net", ipv4_address = "1.1.1.2")
    return device

@pytest.fixture
def device_with_just_phone_number(client) -> Device:
    device = client.devices.get(phone_number="7777777777")
    return device

def to_bytes(json_content: dict) -> bytes:
    return json.dumps(json_content).encode()

def test_updated_device_status_subscription_creation(httpx_mock, client):
    httpx_mock.add_response(
        method="POST",
        json={
            "subscriptionDetail": {
                "device": {
                    "phoneNumber": "123456789",
                    "networkAccessIdentifier": "123456789@domain.com",
                    "ipv4Address": {
                        "publicAddress": "84.125.93.10",
                        "publicPort": 59765
                    },
                    "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                },
                "type": "org.camaraproject.device-status.v0.roaming-status"
            },
            "subscriptionExpireTime": "2023-01-17T13:18:23.682Z",
            "webhook": {
                "notificationUrl": "https://application-server.com",
                "notificationAuthToken": "c8974e592c2fa383d4a3960714"
            },
            "subscriptionId": "qs15-h556-rt89-1298",
            "startsAt": "2024-03-28T12:40:20.398Z",
            "expiresAt": "2024-03-28T12:40:20.398Z"
        },
        match_content=to_bytes(
            {
                "subscriptionDetail": {
                    "device": {
                        "phoneNumber": "123456789",
                        "networkAccessIdentifier": "123456789@domain.com",
                        "ipv4Address": {
                            "publicAddress": "84.125.93.10",
                            "publicPort": 59765
                        },
                        "ipv6Address": "2001:db8:85a3:8d3:1319:8a2e:370:7344"
                    },
                    "type": "org.camaraproject.device-status.v0.roaming-status"
                },
                "subscriptionExpireTime": "2023-01-17T13:18:23.682Z",
                "webhook": {
                    "notificationUrl": "https://application-server.com",
                    "notificationAuthToken": "c8974e592c2fa383d4a3960714"
                }
            }
        )
    )

    device = client.devices.get("123456789@domain.com", phone_number="123456789", ipv4_address=DeviceIpv4Addr(public_address="84.125.93.10", public_port=59765), ipv6_address="2001:db8:85a3:8d3:1319:8a2e:370:7344")

    subscription = client.connectivity.subscribe(
        device=device,
        event_type="org.camaraproject.device-status.v0.roaming-status",
        subscription_expire_time="2023-01-17T13:18:23.682Z",
        notification_url="https://application-server.com",
        notification_auth_token="c8974e592c2fa383d4a3960714"
    )

def test_device_status_creation_minimal_parameters(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        json={
            "subscriptionId": "test-subscription",
        },
        match_content=to_bytes({
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Address": {
                        "publicAddress": "1.1.1.2",
                        "privateAddress": "1.1.1.2",
                        "publicPort": 80
                    },
                },
                "type": "CONNECTIVITY"
            },
            "maxNumberOfReports": 1,
            "webhook": {
                "notificationUrl": "https://localhost:9090/notify",
                "notificationAuthToken": "my_auth_token"
            }
        })
    )

    subscription = client.connectivity.subscribe(event_type="CONNECTIVITY", notification_url="https://localhost:9090/notify", device=device, notification_auth_token="my_auth_token", max_num_of_reports=1)

def test_device_status_creation_minimal_parameters_minimal_ipv4(httpx_mock, device_with_just_public_ipv4, client):
    httpx_mock.add_response(
        method="POST",
        json={
            "subscriptionId": "test-subscription",
        },
        match_content=to_bytes({
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Address": {
                        "publicAddress": "1.1.1.2"
                    }
                },
                "type": "CONNECTIVITY"
            },
            "maxNumberOfReports": 1,
            "webhook": {
                "notificationUrl": "https://localhost:9090/notify",
                "notificationAuthToken": "my_auth_token"
            }
        })
    )

    subscription = client.connectivity.subscribe(event_type="CONNECTIVITY", notification_url="https://localhost:9090/notify", device=device_with_just_public_ipv4, notification_auth_token="my_auth_token", max_num_of_reports=1)

def test_device_status_creation_minimal_parameters_only_phone_number(httpx_mock, device_with_just_phone_number, client):
    httpx_mock.add_response(
        method="POST",
        json={
            "subscriptionId": "test-subscription",
        },
        match_content=to_bytes({
            "subscriptionDetail": {
                "device": {
                    "phoneNumber": "7777777777"
                },
                "type": "CONNECTIVITY"
            },
            "maxNumberOfReports": 1,
            "webhook": {
                "notificationUrl": "https://localhost:9090/notify",
                "notificationAuthToken": "my_auth_token"
            }
        })
    )

    subscription = client.connectivity.subscribe(event_type="CONNECTIVITY", notification_url="https://localhost:9090/notify", device=device_with_just_phone_number, notification_auth_token="my_auth_token", max_num_of_reports=1)

def test_device_status_creation_with_optional_parameters(httpx_mock, device, client):
    httpx_mock.add_response(
        json={
            "subscriptionId": "test-subscription",
        },
        match_content=to_bytes({
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Address": {
                        "publicAddress": "1.1.1.2",
                        "privateAddress": "1.1.1.2",
                        "publicPort": 80
                    },
                },
                "type": "CONNECTIVITY"
            },
            "maxNumberOfReports": 1,
            "subscriptionExpireTime": "2023-08-31",
            "webhook": {
                "notificationUrl": "https://localhost:9090/notify",
                "notificationAuthToken": "my_auth_token"
            }
        })
    )
    
    subscription = client.connectivity.subscribe(event_type="CONNECTIVITY", notification_url="https://localhost:9090/notify", device=device, notification_auth_token="my_auth_token", subscription_expire_time="2023-08-31", max_num_of_reports=1)

def test_device_status_creation_with_roaming_status(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        json={
            "subscriptionId": "test-subscription",
        },
        match_content=to_bytes({
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Address": {
                        "publicAddress": "1.1.1.2",
                        "privateAddress": "1.1.1.2",
                        "publicPort": 80
                    },
                },
                "type": "ROAMING_STATUS"
            },
            "maxNumberOfReports": 1,
            "webhook": {
                "notificationUrl": "https://localhost:9090/notify",
                "notificationAuthToken": "my_auth_token"
            }
        })
    )

    subscription = client.connectivity.subscribe(event_type="ROAMING_STATUS", notification_url="https://localhost:9090/notify", device=device, notification_auth_token="my_auth_token", max_num_of_reports=1)

def test_getting_device_status_subscription(httpx_mock, device, client):
    httpx_mock.add_response(
        method="GET",
        json={
            "subscriptionId": "test-subscription",
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Addresss": {
                        "publicAddress": "1.1.1.2",
                    },
                },
                "type": "CONNECTIVITY"
            },
            "maxNumberOfReports": 1,
            "webhook": {
                "notificationUrl": "http://localhost:9090/notify",
                "notificationAuthToken": "my-token"
            },
            "startsAt": "now",
        }
    )
    
    subscription = client.connectivity.get_subscription("test-subscription")


def test_deleting_device_status_subscription(httpx_mock, device, client):
    httpx_mock.add_response(
        method="GET",
        json={
            "subscriptionId": "test-subscription",
            "subscriptionDetail": {
                "device": {
                    "networkAccessIdentifier": "testuser@open5glab.net",
                    "ipv4Addresss": {
                        "publicAddress": "1.1.1.2"
                    },
                },
                "type": "CONNECTIVITY"
            },
            "maxNumberOfReports": 1,
            "webhook": {
                "notificationUrl": "http://localhost:9090/notify",
                "notificationAuthToken": "my-token"
            },
            "startsAt": "now",
        }
    )
    
    subscription = client.connectivity.get_subscription("test-subscription")

    httpx_mock.add_response(
        method="DELETE",
    )

    subscription.delete()


def test_subscribe_authentication_exception(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        status_code=403
    )
    
    with pytest.raises(AuthenticationException):
        client.connectivity.subscribe(
            event_type="CONNECTIVITY",
            device=device, 
            max_num_of_reports=5, 
            notification_url="http://localhost:9090/notify", 
            notification_auth_token="INVALID_TOKEN", 
        )

def test_subscribe_not_found(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        status_code=404
    )
    
    with pytest.raises(NotFound):
        client.connectivity.subscribe(
            event_type="CONNECTIVITY",
            device=device,  
            max_num_of_reports=5, 
            notification_url="http://localhost:9090/notify", 
            notification_auth_token="my-token"
        )

def test_subscribe_service_error(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        status_code=500
    )
    
    with pytest.raises(ServiceError):
        client.connectivity.subscribe(
            event_type="CONNECTIVITY",
            device=device, 
            max_num_of_reports=5, 
            notification_url="http://localhost:9090/notify", 
            notification_auth_token="my-token"
        )

def test_subscribe_api_error(httpx_mock, device, client):
    httpx_mock.add_response(
        method="POST",
        status_code=400  
    )
    
    with pytest.raises(APIError):
        client.connectivity.subscribe(
            event_type="CONNECTIVITY",
            device=device, 
            max_num_of_reports=5, 
            notification_url="http://localhost:9090/notify", 
            notification_auth_token="my-token"
        )
