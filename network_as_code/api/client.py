import sys

from .binding_generation.openapi_client import Configuration, ApiClient

from .binding_generation.openapi_client.apis.tags import qos_api

# import httpx
# import json as JSON
# # from .endpoints import AdminAPI, ServicesAPI, NotificationsAPI, SubscriptionsAPI

class APIClient:
    """A client for communicating with Network as Code APIs.

    ### Args:
        token (str): Authentication token for the Network as Code API.
        base_url (str): Base URL for the Network as Code API.
        testmode (bool): Whether to use simulated or real resources.
    """

    def __init__(
        self,
        token: str,
        testmode: bool = False,
        base_url: str = "https://network-as-code-poc.p.rapidapi.com",
        **kwargs,
    ):
        headers = {
            "X-RapidAPI-Key": token,
            "X-RapidAPI-Host": "poc4.nokia-evaluation.rapidapi.com",
            "x-testmode": "true" if testmode else "false",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        config = Configuration(
            host=base_url
        )

        self._openapi_client = ApiClient(config)

        self.sessions = qos_api.QosApi(self._openapi_client)
