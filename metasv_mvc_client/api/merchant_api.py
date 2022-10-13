"""
    MetaSV API Spec

    API definition for MetaSV provided apis  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: heqiming@metasv.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from metasv_mvc_client.api_client import ApiClient, Endpoint
from metasv_mvc_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from metasv_mvc_client.model.address_utxo import AddressUtxo
from metasv_mvc_client.model.utxo_pick_request import UtxoPickRequest


class MerchantApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __merchant_utxo_post(
            self,
            **kwargs
        ):
            """Pick utxos by addresses and amount.  # noqa: E501

            Selects a set of Utxos with total value higher than the given amount from a given address list . In case of HD wallets, multiple addresses can be specified.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.merchant_utxo_post(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                utxo_pick_request (UtxoPickRequest): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [AddressUtxo]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.merchant_utxo_post = Endpoint(
            settings={
                'response_type': ([AddressUtxo],),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/merchant/utxo',
                'operation_id': 'merchant_utxo_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'utxo_pick_request',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'utxo_pick_request':
                        (UtxoPickRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'utxo_pick_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__merchant_utxo_post
        )