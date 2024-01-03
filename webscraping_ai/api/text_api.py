# coding: utf-8

"""
    WebScraping.AI

    WebScraping.AI scraping API provides GPT-powered tools with Chromium JavaScript rendering, rotating proxies, and built-in HTML parsing.

    The version of the OpenAPI document: 3.1.2
    Contact: support@webscraping.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictBool, StrictStr, field_validator

from typing import Any, Dict, Optional


from webscraping_ai.api_client import ApiClient
from webscraping_ai.api_response import ApiResponse
from webscraping_ai.rest import RESTResponseType


class TextApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_text(
        self,
        url: Annotated[StrictStr, Field(description="URL of the target page.")],
        text_format: Annotated[Optional[StrictStr], Field(description="Format of the text response (plain by default). \"plain\" will return only the page body text. \"json\" and \"xml\" will return a json/xml with \"title\", \"description\" and \"content\" keys.")] = None,
        return_links: Annotated[Optional[StrictBool], Field(description="[Works only with text_format=json] Return links from the page body text (false by default). Useful for building web crawlers.")] = None,
        headers: Annotated[Optional[Dict[str, Any]], Field(description="HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&headers[One]=value1&headers=[Another]=value2) or as a JSON encoded object (...&headers={\"One\": \"value1\", \"Another\": \"value2\"}).")] = None,
        timeout: Annotated[Optional[Annotated[int, Field(le=30000, strict=True, ge=1)]], Field(description="Maximum web page retrieval time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000).")] = None,
        js: Annotated[Optional[StrictBool], Field(description="Execute on-page JavaScript using a headless browser (true by default).")] = None,
        js_timeout: Annotated[Optional[Annotated[int, Field(le=20000, strict=True, ge=1)]], Field(description="Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page.")] = None,
        proxy: Annotated[Optional[StrictStr], Field(description="Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details.")] = None,
        country: Annotated[Optional[StrictStr], Field(description="Country of the proxy to use (US by default). Only available on Startup and Custom plans.")] = None,
        device: Annotated[Optional[StrictStr], Field(description="Type of device emulation.")] = None,
        error_on_404: Annotated[Optional[StrictBool], Field(description="Return error on 404 HTTP status on the target page (false by default).")] = None,
        error_on_redirect: Annotated[Optional[StrictBool], Field(description="Return error on redirect on the target page (false by default).")] = None,
        js_script: Annotated[Optional[StrictStr], Field(description="Custom JavaScript code to execute on the target page.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> str:
        """Page text by URL

        Returns the visible text content of a webpage specified by the URL. Can be used to feed data to GPT or other LLM models. The response can be in plain text, JSON, or XML format based on the text_format parameter. Proxies and Chromium JavaScript rendering are used for page retrieval and processing. Returns JSON on error.

        :param url: URL of the target page. (required)
        :type url: str
        :param text_format: Format of the text response (plain by default). \"plain\" will return only the page body text. \"json\" and \"xml\" will return a json/xml with \"title\", \"description\" and \"content\" keys.
        :type text_format: str
        :param return_links: [Works only with text_format=json] Return links from the page body text (false by default). Useful for building web crawlers.
        :type return_links: bool
        :param headers: HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&headers[One]=value1&headers=[Another]=value2) or as a JSON encoded object (...&headers={\"One\": \"value1\", \"Another\": \"value2\"}).
        :type headers: Dict[str, str]
        :param timeout: Maximum web page retrieval time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000).
        :type timeout: int
        :param js: Execute on-page JavaScript using a headless browser (true by default).
        :type js: bool
        :param js_timeout: Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page.
        :type js_timeout: int
        :param proxy: Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details.
        :type proxy: str
        :param country: Country of the proxy to use (US by default). Only available on Startup and Custom plans.
        :type country: str
        :param device: Type of device emulation.
        :type device: str
        :param error_on_404: Return error on 404 HTTP status on the target page (false by default).
        :type error_on_404: bool
        :param error_on_redirect: Return error on redirect on the target page (false by default).
        :type error_on_redirect: bool
        :param js_script: Custom JavaScript code to execute on the target page.
        :type js_script: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_text_serialize(
            url=url,
            text_format=text_format,
            return_links=return_links,
            headers=headers,
            timeout=timeout,
            js=js,
            js_timeout=js_timeout,
            proxy=proxy,
            country=country,
            device=device,
            error_on_404=error_on_404,
            error_on_redirect=error_on_redirect,
            js_script=js_script,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '400': "Error",
            '402': "Error",
            '403': "Error",
            '429': "Error",
            '500': "Error",
            '504': "Error",
            '200': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_text_with_http_info(
        self,
        url: Annotated[StrictStr, Field(description="URL of the target page.")],
        text_format: Annotated[Optional[StrictStr], Field(description="Format of the text response (plain by default). \"plain\" will return only the page body text. \"json\" and \"xml\" will return a json/xml with \"title\", \"description\" and \"content\" keys.")] = None,
        return_links: Annotated[Optional[StrictBool], Field(description="[Works only with text_format=json] Return links from the page body text (false by default). Useful for building web crawlers.")] = None,
        headers: Annotated[Optional[Dict[str, Any]], Field(description="HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&headers[One]=value1&headers=[Another]=value2) or as a JSON encoded object (...&headers={\"One\": \"value1\", \"Another\": \"value2\"}).")] = None,
        timeout: Annotated[Optional[Annotated[int, Field(le=30000, strict=True, ge=1)]], Field(description="Maximum web page retrieval time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000).")] = None,
        js: Annotated[Optional[StrictBool], Field(description="Execute on-page JavaScript using a headless browser (true by default).")] = None,
        js_timeout: Annotated[Optional[Annotated[int, Field(le=20000, strict=True, ge=1)]], Field(description="Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page.")] = None,
        proxy: Annotated[Optional[StrictStr], Field(description="Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details.")] = None,
        country: Annotated[Optional[StrictStr], Field(description="Country of the proxy to use (US by default). Only available on Startup and Custom plans.")] = None,
        device: Annotated[Optional[StrictStr], Field(description="Type of device emulation.")] = None,
        error_on_404: Annotated[Optional[StrictBool], Field(description="Return error on 404 HTTP status on the target page (false by default).")] = None,
        error_on_redirect: Annotated[Optional[StrictBool], Field(description="Return error on redirect on the target page (false by default).")] = None,
        js_script: Annotated[Optional[StrictStr], Field(description="Custom JavaScript code to execute on the target page.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[str]:
        """Page text by URL

        Returns the visible text content of a webpage specified by the URL. Can be used to feed data to GPT or other LLM models. The response can be in plain text, JSON, or XML format based on the text_format parameter. Proxies and Chromium JavaScript rendering are used for page retrieval and processing. Returns JSON on error.

        :param url: URL of the target page. (required)
        :type url: str
        :param text_format: Format of the text response (plain by default). \"plain\" will return only the page body text. \"json\" and \"xml\" will return a json/xml with \"title\", \"description\" and \"content\" keys.
        :type text_format: str
        :param return_links: [Works only with text_format=json] Return links from the page body text (false by default). Useful for building web crawlers.
        :type return_links: bool
        :param headers: HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&headers[One]=value1&headers=[Another]=value2) or as a JSON encoded object (...&headers={\"One\": \"value1\", \"Another\": \"value2\"}).
        :type headers: Dict[str, str]
        :param timeout: Maximum web page retrieval time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000).
        :type timeout: int
        :param js: Execute on-page JavaScript using a headless browser (true by default).
        :type js: bool
        :param js_timeout: Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page.
        :type js_timeout: int
        :param proxy: Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details.
        :type proxy: str
        :param country: Country of the proxy to use (US by default). Only available on Startup and Custom plans.
        :type country: str
        :param device: Type of device emulation.
        :type device: str
        :param error_on_404: Return error on 404 HTTP status on the target page (false by default).
        :type error_on_404: bool
        :param error_on_redirect: Return error on redirect on the target page (false by default).
        :type error_on_redirect: bool
        :param js_script: Custom JavaScript code to execute on the target page.
        :type js_script: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_text_serialize(
            url=url,
            text_format=text_format,
            return_links=return_links,
            headers=headers,
            timeout=timeout,
            js=js,
            js_timeout=js_timeout,
            proxy=proxy,
            country=country,
            device=device,
            error_on_404=error_on_404,
            error_on_redirect=error_on_redirect,
            js_script=js_script,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '400': "Error",
            '402': "Error",
            '403': "Error",
            '429': "Error",
            '500': "Error",
            '504': "Error",
            '200': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_text_without_preload_content(
        self,
        url: Annotated[StrictStr, Field(description="URL of the target page.")],
        text_format: Annotated[Optional[StrictStr], Field(description="Format of the text response (plain by default). \"plain\" will return only the page body text. \"json\" and \"xml\" will return a json/xml with \"title\", \"description\" and \"content\" keys.")] = None,
        return_links: Annotated[Optional[StrictBool], Field(description="[Works only with text_format=json] Return links from the page body text (false by default). Useful for building web crawlers.")] = None,
        headers: Annotated[Optional[Dict[str, Any]], Field(description="HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&headers[One]=value1&headers=[Another]=value2) or as a JSON encoded object (...&headers={\"One\": \"value1\", \"Another\": \"value2\"}).")] = None,
        timeout: Annotated[Optional[Annotated[int, Field(le=30000, strict=True, ge=1)]], Field(description="Maximum web page retrieval time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000).")] = None,
        js: Annotated[Optional[StrictBool], Field(description="Execute on-page JavaScript using a headless browser (true by default).")] = None,
        js_timeout: Annotated[Optional[Annotated[int, Field(le=20000, strict=True, ge=1)]], Field(description="Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page.")] = None,
        proxy: Annotated[Optional[StrictStr], Field(description="Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details.")] = None,
        country: Annotated[Optional[StrictStr], Field(description="Country of the proxy to use (US by default). Only available on Startup and Custom plans.")] = None,
        device: Annotated[Optional[StrictStr], Field(description="Type of device emulation.")] = None,
        error_on_404: Annotated[Optional[StrictBool], Field(description="Return error on 404 HTTP status on the target page (false by default).")] = None,
        error_on_redirect: Annotated[Optional[StrictBool], Field(description="Return error on redirect on the target page (false by default).")] = None,
        js_script: Annotated[Optional[StrictStr], Field(description="Custom JavaScript code to execute on the target page.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Page text by URL

        Returns the visible text content of a webpage specified by the URL. Can be used to feed data to GPT or other LLM models. The response can be in plain text, JSON, or XML format based on the text_format parameter. Proxies and Chromium JavaScript rendering are used for page retrieval and processing. Returns JSON on error.

        :param url: URL of the target page. (required)
        :type url: str
        :param text_format: Format of the text response (plain by default). \"plain\" will return only the page body text. \"json\" and \"xml\" will return a json/xml with \"title\", \"description\" and \"content\" keys.
        :type text_format: str
        :param return_links: [Works only with text_format=json] Return links from the page body text (false by default). Useful for building web crawlers.
        :type return_links: bool
        :param headers: HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&headers[One]=value1&headers=[Another]=value2) or as a JSON encoded object (...&headers={\"One\": \"value1\", \"Another\": \"value2\"}).
        :type headers: Dict[str, str]
        :param timeout: Maximum web page retrieval time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000).
        :type timeout: int
        :param js: Execute on-page JavaScript using a headless browser (true by default).
        :type js: bool
        :param js_timeout: Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page.
        :type js_timeout: int
        :param proxy: Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details.
        :type proxy: str
        :param country: Country of the proxy to use (US by default). Only available on Startup and Custom plans.
        :type country: str
        :param device: Type of device emulation.
        :type device: str
        :param error_on_404: Return error on 404 HTTP status on the target page (false by default).
        :type error_on_404: bool
        :param error_on_redirect: Return error on redirect on the target page (false by default).
        :type error_on_redirect: bool
        :param js_script: Custom JavaScript code to execute on the target page.
        :type js_script: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_text_serialize(
            url=url,
            text_format=text_format,
            return_links=return_links,
            headers=headers,
            timeout=timeout,
            js=js,
            js_timeout=js_timeout,
            proxy=proxy,
            country=country,
            device=device,
            error_on_404=error_on_404,
            error_on_redirect=error_on_redirect,
            js_script=js_script,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '400': "Error",
            '402': "Error",
            '403': "Error",
            '429': "Error",
            '500': "Error",
            '504': "Error",
            '200': "str",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_text_serialize(
        self,
        url,
        text_format,
        return_links,
        headers,
        timeout,
        js,
        js_timeout,
        proxy,
        country,
        device,
        error_on_404,
        error_on_redirect,
        js_script,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if text_format is not None:
            
            _query_params.append(('text_format', text_format))
            
        if return_links is not None:
            
            _query_params.append(('return_links', return_links))
            
        if url is not None:
            
            _query_params.append(('url', url))
            
        if headers is not None:
            
            _query_params.append(('headers', headers))
            
        if timeout is not None:
            
            _query_params.append(('timeout', timeout))
            
        if js is not None:
            
            _query_params.append(('js', js))
            
        if js_timeout is not None:
            
            _query_params.append(('js_timeout', js_timeout))
            
        if proxy is not None:
            
            _query_params.append(('proxy', proxy))
            
        if country is not None:
            
            _query_params.append(('country', country))
            
        if device is not None:
            
            _query_params.append(('device', device))
            
        if error_on_404 is not None:
            
            _query_params.append(('error_on_404', error_on_404))
            
        if error_on_redirect is not None:
            
            _query_params.append(('error_on_redirect', error_on_redirect))
            
        if js_script is not None:
            
            _query_params.append(('js_script', js_script))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json', 
                'text/html', 
                'text/xml'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'api_key'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/text',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


