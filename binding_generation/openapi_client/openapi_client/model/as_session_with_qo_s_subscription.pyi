# coding: utf-8

"""
    QoS

    QoS manages communication bandwidth for a given device.  # noqa: E501

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

from openapi_client import schemas  # noqa: F401


class AsSessionWithQoSSubscription(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "qosReference",
            "flowInfo",
        }
        
        class properties:
            qosReference = schemas.StrSchema
            
            
            class flowInfo(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FlowInfo']:
                        return FlowInfo
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FlowInfo'], typing.List['FlowInfo']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'flowInfo':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FlowInfo':
                    return super().__getitem__(i)
            _self = schemas.StrSchema
            supportedFeatures = schemas.StrSchema
            ueIpv4Addr = schemas.StrSchema
            ueIpv6Addr = schemas.StrSchema
            __annotations__ = {
                "qosReference": qosReference,
                "flowInfo": flowInfo,
                "self": _self,
                "supportedFeatures": supportedFeatures,
                "ueIpv4Addr": ueIpv4Addr,
                "ueIpv6Addr": ueIpv6Addr,
            }
    
    qosReference: MetaOapg.properties.qosReference
    flowInfo: MetaOapg.properties.flowInfo
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["qosReference"]) -> MetaOapg.properties.qosReference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flowInfo"]) -> MetaOapg.properties.flowInfo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supportedFeatures"]) -> MetaOapg.properties.supportedFeatures: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ueIpv4Addr"]) -> MetaOapg.properties.ueIpv4Addr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ueIpv6Addr"]) -> MetaOapg.properties.ueIpv6Addr: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["qosReference", "flowInfo", "self", "supportedFeatures", "ueIpv4Addr", "ueIpv6Addr", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["qosReference"]) -> MetaOapg.properties.qosReference: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flowInfo"]) -> MetaOapg.properties.flowInfo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supportedFeatures"]) -> typing.Union[MetaOapg.properties.supportedFeatures, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ueIpv4Addr"]) -> typing.Union[MetaOapg.properties.ueIpv4Addr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ueIpv6Addr"]) -> typing.Union[MetaOapg.properties.ueIpv6Addr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["qosReference", "flowInfo", "self", "supportedFeatures", "ueIpv4Addr", "ueIpv6Addr", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        qosReference: typing.Union[MetaOapg.properties.qosReference, str, ],
        flowInfo: typing.Union[MetaOapg.properties.flowInfo, list, tuple, ],
        supportedFeatures: typing.Union[MetaOapg.properties.supportedFeatures, str, schemas.Unset] = schemas.unset,
        ueIpv4Addr: typing.Union[MetaOapg.properties.ueIpv4Addr, str, schemas.Unset] = schemas.unset,
        ueIpv6Addr: typing.Union[MetaOapg.properties.ueIpv6Addr, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AsSessionWithQoSSubscription':
        return super().__new__(
            cls,
            *args,
            qosReference=qosReference,
            flowInfo=flowInfo,
            supportedFeatures=supportedFeatures,
            ueIpv4Addr=ueIpv4Addr,
            ueIpv6Addr=ueIpv6Addr,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.flow_info import FlowInfo