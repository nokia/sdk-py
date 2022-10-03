from .endpoint import Endpoint


class SubscriptionsAPI(Endpoint):
    async def get_subscription(self, id: str):
        res = await self.client.post("/subscriber", json={"sid": id})
        return self.client._result(res, json=True)

    async def create_subscription(
        self,
        id: str,
        imsi: str,
        msisdn: str,
    ):
        res = await self.client.put(
            "/admin/testuser",
            json={"sid": id, "imsi": imsi, "msisdn": msisdn},
        )
        return self.client._result(res, json=True)

    async def delete_subscription(self, id: str, testmode: bool = True):
        res = await self.client.delete(
            f"/admin/testuser/{id}",
            headers={"x-testmode": "true" if testmode else "false"},
        )
        return True if res.status_code == 204 else False

    async def get_subscriber_location(self, id: str):
        res = await self.client.post("/subscriber/location", json={"sid": id})
        return self.client._result(res, json=True)

    async def get_subscriber_bandwidth(self, id: str):
        res = await self.client.post("/subscriber/bandwidth", json={"sid": id})
        return self.client._result(res, json=True)

    async def set_subscriber_bandwidth(self, id: str, bandwidth: str):
        res = await self.client.patch(
            "/subscriber/bandwidth",
            json={"sid": id, "bandwidth": bandwidth},
        )
        return self.client._result(res, json=True)

    async def set_subscriber_custom_bandwidth(self, id: str, up: int, down: int):
        res = await self.client.patch(
            "/subscriber/bandwidth/custom",
            json={"sid": id, "upload": up, "download": down},
        )
        return self.client._result(res, json=True)

    async def get_subscriber_custom_bandwidth(self, id: str):
        res = await self.client.patch("/subscriber/bandwidth/custom", json={"sid": id})
        return self.client._result(res, json=True)