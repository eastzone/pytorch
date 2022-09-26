# This file was generated by jschema_to_python version 0.0.1.dev29.

from __future__ import annotations

import dataclasses
from typing import List, Optional


@dataclasses.dataclass
class PropertyBag(object):
    """Key/value pairs that provide additional information about the object."""

    tags: Optional[List[str]] = dataclasses.field(
        default=None, metadata={"schema_property_name": "tags"}
    )


# flake8: noqa
