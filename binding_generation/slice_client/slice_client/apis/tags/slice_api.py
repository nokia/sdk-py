# coding: utf-8

"""
    Slice

    Slice management, creating and deleting network slices.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

from slice_client.paths.slices_id_activate.post import ActivateSlice
from slice_client.paths.slices.post import CreateSlice
from slice_client.paths.slices_id_deactivate.post import DeactivateSlice
from slice_client.paths.slices_id.delete import DeleteSlice
from slice_client.paths.slices_id.get import GetSlice


class SliceApi(
    ActivateSlice,
    CreateSlice,
    DeactivateSlice,
    DeleteSlice,
    GetSlice,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
