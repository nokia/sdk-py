from typing import List, Optional
import math
from . import Namespace
from ..models import Slice
from ..errors import NotFound, AuthenticationException, ServiceError, InvalidParameter
from urllib.error import HTTPError
from pydantic import ValidationError
from slice_client.model.throughput import Throughput
from slice_client.model.slice_data import SliceData
from slice_client.model.network_identifier import NetworkIdentifier
from slice_client.model.slice_info import SliceInfo
from slice_client.model.area_of_service import AreaOfService


class Slices(Namespace):
    """Representation of a 5G network slice.

    Through this class many of the parameters of a
    network slice can be configured and managed.
    """

    def create(self,
               network_id: NetworkIdentifier, 
               slice_info: SliceInfo, 
               area_of_service: AreaOfService, 
               notification_url: str,
               notification_auth_token: Optional[str] = None,
               slice_downlink_throughput: Optional[Throughput] = None, 
               slice_uplink_throughput: Optional[Throughput] = None,
               device_downlink_throughput: Optional[Throughput] = None,
               device_uplink_throughput: Optional[Throughput] = None,
               name: Optional[str] = None,
               max_data_connections: Optional[int] = None,
               max_devices: Optional[int] = None
               ) -> Slice:
        """Create a slice with its network identifier, slice info, area of service, slice downlink throughput, slice uplink throughput, device downlink throughput, and device uplink throughput.

        Args:
            network_id (NetworkIdentifier): Name of the network
            slice_info (SliceInfo): Purpose of this slice
            area_of_service (AreaOfService): Location of the slice
            slice_downlink_throughput (optional): 
            slice_uplink_throughput (optional):
            device_downlink_throughput (optional):
            device_uplink_throughput: (optional):
            name (optional): Optional short name for the slice. Must be ASCII characters, digits and dash. Like name of an event, such as "Concert-2029-Big-Arena".
            max_data_connections (optional): Optional maximum number of data connection sessions in the slice.
            max_devices (optional): Optional maximum number of devices using the slice.
        """

        slice = Slice(
            api=self.api, 
            id = None,
            state = "NOT_SUBMITTED",
            name = name, 
            network_identifier = network_id,
            slice_info = slice_info, 
            area_of_service = area_of_service, 
            maxDataConnections = max_data_connections,
            maxDevices = max_devices,
            sliceDownlinkThroughput = slice_downlink_throughput, 
            slice_uplink_throughput = slice_uplink_throughput,
            device_downlink_throughput = device_downlink_throughput,
            device_uplink_throughput = device_uplink_throughput
        )

        # Error Case: Creating Slice
        try:
            body = {
                "networkIdentifier": network_id,
                "sliceInfo": slice_info,
                "areaOfService": area_of_service,
                "notificationUrl": notification_url,
                "notificationAuthToken": notification_auth_token,
                "name": name,
                "maxDataConnections": max_data_connections,
                "maxDevices": max_devices,
                "sliceUplinkThroughput": slice_uplink_throughput,
                "sliceDownlinkThroughput": slice_downlink_throughput,
                "deviceUplinkThroughput": device_uplink_throughput,
                "deviceDownlinkThroughput": device_downlink_throughput
            }
            slice_data = self.api.slice.create_slice(body)
            slice.sid = slice_data.csi_id
            slice.state = slice_data.state
        except HTTPError as e:
            if e.code == 403:
                raise AuthenticationException(e)
            elif e.code == 404:
                raise NotFound(e)
            elif e.code >= 500:
                raise ServiceError(e)
        except ValidationError as e:
            raise InvalidParameter(e)

        return slice

    def get(self, id: str) -> Slice | None:
        """Get network slice by id.

        #### Args:
            id (str): Resource id.

        #### Example:
            ```python
            slice_data = slice_data.slice.get(id)
            ```
        """
        slice_data = self.api.slice.get_slice(id)

        slice = Slice(
            api=self.api, 
            id = slice_data.csi_id,
            state = slice_data.state,
            name = slice_data.slice.name, 
            networkIdentifier = slice_data.slice.network_id,
            sliceInfo = slice_data.slice.slice_info, 
            areaOfService = slice_data.slice.area_of_service, 
            maxDataConnections = slice_data.slice.max_data_connections,
            maxDevices = slice_data.slice.max_devices,
            sliceDownlinkThroughput = slice_data.slice.slice_downlink_throughput, 
            slice_uplink_throughput = slice_data.slice.slice_uplink_throughput,
            device_downlink_throughput = slice_data.slice.device_downlink_throughput,
            device_uplink_throughput = slice_data.slice.device_uplink_throughput
        )

        return slice

