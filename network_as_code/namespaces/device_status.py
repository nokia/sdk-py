from typing import List
import math
from . import Namespace
from ..models.device import Device 
from ..models.device_status import ConnectivitySubscription

from devicestatus_client.models import Device as BindingDevice
from devicestatus_client.models import CreateEventSubscription
from devicestatus_client.models import CreateEventSubscription, EventSubscriptionDetail
from devicestatus_client.models import Webhook

from ..errors import DeviceNotFound, AuthenticationException, ServiceError, InvalidParameter, error_handler
from urllib.error import HTTPError
from pydantic import ValidationError
from typing import Optional


class Connectivity(Namespace):
    """Representation of the status of a device.

    Through this class many of the parameters of a
    device status can be configured and managed.
    """

    def subscribe(self, 
                  event_type: str,
                  max_num_of_reports: int, 
                  notification_url: str,
                  notification_auth_token: str,
                  device: Device,
                  subscription_expire_time: Optional[str] = None,
                  ) -> ConnectivitySubscription:
        """Create subscription for device connectivity status.

        Args:
            max_num_of_reports (str): Number of notifications until the subscription is available
            notification_url (str): Notification URL for session-related events.
            notification_auth_token (optional): Authorization token for notification sending.
            device (Device): Identifier of the device
            dnn (optional): Data Network Name, also known as as Access Point Name (APN)
        """

        connectivity_subscription = ConnectivitySubscription(
            api=self.api, 
            max_num_of_reports = max_num_of_reports, 
            notification_url = notification_url,
            notification_auth_token = notification_auth_token,
            device = device 
        )

        # Error Case: Creating Connectivity Subscription
        try:
            connectivity_data = self.api.devicestatus.create_subscription(
                device,
                event_type,
                notification_url,
                notification_auth_token,
                max_num_of_reports,
                subscription_expire_time
            )
            connectivity_subscription.id = connectivity_data["eventSubscriptionId"]

        except HTTPError as e:
            if e.code == 403:
                raise AuthenticationException(e)
            elif e.code == 404:
                raise DeviceNotFound(e)
            elif e.code >= 500:
                raise ServiceError(e)
        except ValidationError as e:
            raise InvalidParameter(e)

        return connectivity_subscription

    def get_subscription(self, id: str) -> ConnectivitySubscription:
        """Retrieve device connectivity status data

        #### Args:
            id (str): Resource ID

        #### Example:
            ```python
            connectivity_data = device.get_connectivity(id="hadsghsio")
            ```
        """

        # Error Case: Getting connectivity status data
        global connectivity_data
        connectivity_data = self.api.devicestatus.get_subscription(id)

        device_data = connectivity_data["subscriptionDetail"]["device"]

        print(device_data)

        return ConnectivitySubscription(
            id=connectivity_data["eventSubscriptionId"],
            api=self.api, 
            max_num_of_reports = 0,
            notification_url = connectivity_data["webhook"]["notificationUrl"],
            notification_auth_token = connectivity_data["webhook"]["notificationAuthToken"],
            device = Device(api=self.api, sid=connectivity_data["subscriptionDetail"]["device"]["networkAccessIdentifier"], ip="127.0.0.1")
        )
