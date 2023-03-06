import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.sessions import Sessions
from openapi_client.apis.paths.sessions_resource_id import SessionsResourceId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SESSIONS: Sessions,
        PathValues.SESSIONS_RESOURCE_ID: SessionsResourceId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SESSIONS: Sessions,
        PathValues.SESSIONS_RESOURCE_ID: SessionsResourceId,
    }
)
