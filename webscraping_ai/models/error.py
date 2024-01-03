# coding: utf-8

"""
    WebScraping.AI

    WebScraping.AI scraping API provides GPT-powered tools with Chromium JavaScript rendering, rotating proxies, and built-in HTML parsing.

    The version of the OpenAPI document: 3.1.2
    Contact: support@webscraping.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Error(BaseModel):
    """
    Error
    """ # noqa: E501
    message: Optional[StrictStr] = Field(default=None, description="Error description")
    status_code: Optional[StrictInt] = Field(default=None, description="Target page response HTTP status code (403, 500, etc)")
    status_message: Optional[StrictStr] = Field(default=None, description="Target page response HTTP status message")
    body: Optional[StrictStr] = Field(default=None, description="Target page response body")
    __properties: ClassVar[List[str]] = ["message", "status_code", "status_message", "body"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Error from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Error from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message": obj.get("message"),
            "status_code": obj.get("status_code"),
            "status_message": obj.get("status_message"),
            "body": obj.get("body")
        })
        return _obj


