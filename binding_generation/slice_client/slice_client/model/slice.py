# coding: utf-8

"""
    Slice

    Slice management, creating and deleting network slices.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from slice_client import schemas  # noqa: F401


class Slice(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "areaOfService",
            "notificationUrl",
            "networkIdentifier",
            "sliceInfo",
        }
        
        class properties:
            notificationUrl = schemas.StrSchema
        
            @staticmethod
            def networkIdentifier() -> typing.Type['NetworkIdentifier']:
                return NetworkIdentifier
        
            @staticmethod
            def sliceInfo() -> typing.Type['SliceInfo']:
                return SliceInfo
        
            @staticmethod
            def areaOfService() -> typing.Type['AreaOfService']:
                return AreaOfService
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
                    min_length = 8
                    regex=[{
                        'pattern': r'^[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]$',  # noqa: E501
                    }]
            notificationAuthToken = schemas.StrSchema
            
            
            class maxDataConnections(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
            
            
            class maxDevices(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0
        
            @staticmethod
            def sliceDownlinkThroughput() -> typing.Type['Throughput']:
                return Throughput
        
            @staticmethod
            def sliceUplinkThroughput() -> typing.Type['Throughput']:
                return Throughput
        
            @staticmethod
            def deviceDownlinkThroughput() -> typing.Type['Throughput']:
                return Throughput
        
            @staticmethod
            def deviceUplinkThroughput() -> typing.Type['Throughput']:
                return Throughput
            __annotations__ = {
                "notificationUrl": notificationUrl,
                "networkIdentifier": networkIdentifier,
                "sliceInfo": sliceInfo,
                "areaOfService": areaOfService,
                "name": name,
                "notificationAuthToken": notificationAuthToken,
                "maxDataConnections": maxDataConnections,
                "maxDevices": maxDevices,
                "sliceDownlinkThroughput": sliceDownlinkThroughput,
                "sliceUplinkThroughput": sliceUplinkThroughput,
                "deviceDownlinkThroughput": deviceDownlinkThroughput,
                "deviceUplinkThroughput": deviceUplinkThroughput,
            }
    
    areaOfService: 'AreaOfService'
    notificationUrl: MetaOapg.properties.notificationUrl
    networkIdentifier: 'NetworkIdentifier'
    sliceInfo: 'SliceInfo'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notificationUrl"]) -> MetaOapg.properties.notificationUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["networkIdentifier"]) -> 'NetworkIdentifier': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sliceInfo"]) -> 'SliceInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["areaOfService"]) -> 'AreaOfService': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notificationAuthToken"]) -> MetaOapg.properties.notificationAuthToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxDataConnections"]) -> MetaOapg.properties.maxDataConnections: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxDevices"]) -> MetaOapg.properties.maxDevices: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sliceDownlinkThroughput"]) -> 'Throughput': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sliceUplinkThroughput"]) -> 'Throughput': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deviceDownlinkThroughput"]) -> 'Throughput': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deviceUplinkThroughput"]) -> 'Throughput': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["notificationUrl", "networkIdentifier", "sliceInfo", "areaOfService", "name", "notificationAuthToken", "maxDataConnections", "maxDevices", "sliceDownlinkThroughput", "sliceUplinkThroughput", "deviceDownlinkThroughput", "deviceUplinkThroughput", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notificationUrl"]) -> MetaOapg.properties.notificationUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["networkIdentifier"]) -> 'NetworkIdentifier': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sliceInfo"]) -> 'SliceInfo': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["areaOfService"]) -> 'AreaOfService': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notificationAuthToken"]) -> typing.Union[MetaOapg.properties.notificationAuthToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxDataConnections"]) -> typing.Union[MetaOapg.properties.maxDataConnections, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxDevices"]) -> typing.Union[MetaOapg.properties.maxDevices, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sliceDownlinkThroughput"]) -> typing.Union['Throughput', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sliceUplinkThroughput"]) -> typing.Union['Throughput', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deviceDownlinkThroughput"]) -> typing.Union['Throughput', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deviceUplinkThroughput"]) -> typing.Union['Throughput', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["notificationUrl", "networkIdentifier", "sliceInfo", "areaOfService", "name", "notificationAuthToken", "maxDataConnections", "maxDevices", "sliceDownlinkThroughput", "sliceUplinkThroughput", "deviceDownlinkThroughput", "deviceUplinkThroughput", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        areaOfService: 'AreaOfService',
        notificationUrl: typing.Union[MetaOapg.properties.notificationUrl, str, ],
        networkIdentifier: 'NetworkIdentifier',
        sliceInfo: 'SliceInfo',
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        notificationAuthToken: typing.Union[MetaOapg.properties.notificationAuthToken, str, schemas.Unset] = schemas.unset,
        maxDataConnections: typing.Union[MetaOapg.properties.maxDataConnections, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxDevices: typing.Union[MetaOapg.properties.maxDevices, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sliceDownlinkThroughput: typing.Union['Throughput', schemas.Unset] = schemas.unset,
        sliceUplinkThroughput: typing.Union['Throughput', schemas.Unset] = schemas.unset,
        deviceDownlinkThroughput: typing.Union['Throughput', schemas.Unset] = schemas.unset,
        deviceUplinkThroughput: typing.Union['Throughput', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Slice':
        return super().__new__(
            cls,
            *args,
            areaOfService=areaOfService,
            notificationUrl=notificationUrl,
            networkIdentifier=networkIdentifier,
            sliceInfo=sliceInfo,
            name=name,
            notificationAuthToken=notificationAuthToken,
            maxDataConnections=maxDataConnections,
            maxDevices=maxDevices,
            sliceDownlinkThroughput=sliceDownlinkThroughput,
            sliceUplinkThroughput=sliceUplinkThroughput,
            deviceDownlinkThroughput=deviceDownlinkThroughput,
            deviceUplinkThroughput=deviceUplinkThroughput,
            _configuration=_configuration,
            **kwargs,
        )

from slice_client.model.area_of_service import AreaOfService
from slice_client.model.network_identifier import NetworkIdentifier
from slice_client.model.slice_info import SliceInfo
from slice_client.model.throughput import Throughput
