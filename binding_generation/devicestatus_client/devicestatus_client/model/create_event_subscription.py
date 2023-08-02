# coding: utf-8

"""
    Device Status

    Device Status can provide updates on the device's connectivity state  # noqa: E501

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

from devicestatus_client import schemas  # noqa: F401


class CreateEventSubscription(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "webhook",
            "subscriptionDetail",
        }
        
        class properties:
            
            
            class subscriptionDetail(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            EventSubscriptionDetail,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'subscriptionDetail':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def webhook() -> typing.Type['Webhook']:
                return Webhook
            subscriptionExpireTime = schemas.StrSchema
            
            
            class maxNumberOfReports(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 256
                    inclusive_minimum = 1
            __annotations__ = {
                "subscriptionDetail": subscriptionDetail,
                "webhook": webhook,
                "subscriptionExpireTime": subscriptionExpireTime,
                "maxNumberOfReports": maxNumberOfReports,
            }
    
    webhook: 'Webhook'
    subscriptionDetail: MetaOapg.properties.subscriptionDetail
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriptionDetail"]) -> MetaOapg.properties.subscriptionDetail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook"]) -> 'Webhook': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriptionExpireTime"]) -> MetaOapg.properties.subscriptionExpireTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxNumberOfReports"]) -> MetaOapg.properties.maxNumberOfReports: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["subscriptionDetail", "webhook", "subscriptionExpireTime", "maxNumberOfReports", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriptionDetail"]) -> MetaOapg.properties.subscriptionDetail: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook"]) -> 'Webhook': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriptionExpireTime"]) -> typing.Union[MetaOapg.properties.subscriptionExpireTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxNumberOfReports"]) -> typing.Union[MetaOapg.properties.maxNumberOfReports, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["subscriptionDetail", "webhook", "subscriptionExpireTime", "maxNumberOfReports", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        webhook: 'Webhook',
        subscriptionDetail: typing.Union[MetaOapg.properties.subscriptionDetail, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        subscriptionExpireTime: typing.Union[MetaOapg.properties.subscriptionExpireTime, str, schemas.Unset] = schemas.unset,
        maxNumberOfReports: typing.Union[MetaOapg.properties.maxNumberOfReports, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateEventSubscription':
        return super().__new__(
            cls,
            *args,
            webhook=webhook,
            subscriptionDetail=subscriptionDetail,
            subscriptionExpireTime=subscriptionExpireTime,
            maxNumberOfReports=maxNumberOfReports,
            _configuration=_configuration,
            **kwargs,
        )

from devicestatus_client.model.event_subscription_detail import EventSubscriptionDetail
from devicestatus_client.model.webhook import Webhook