
import network_as_code as nac

# We begin by creating a client for Network as Code
client = nac.NetworkAsCodeClient(
    token="<MY-TOKEN>",
)

# We get the device by querying subscriptions with the UE's external identifer
device = client.devices.get("testuser@testcsp.net", ipv4_address="127.0.0.1")

session = device.create_qod_session(service_ipv4="1.1.1.1", profile="DOWNLINK_L_UPLINK_L", notification_url="https://notify.me/here", notification_auth_token="my_auth_token")

session.delete()
