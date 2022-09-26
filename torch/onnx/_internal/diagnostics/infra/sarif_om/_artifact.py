# This file was generated by jschema_to_python version 0.0.1.dev29.

from __future__ import annotations

import dataclasses
from typing import Any, List, Optional

from typing_extensions import Literal

from torch.onnx._internal.diagnostics.infra.sarif_om import (
    _artifact_content,
    _artifact_location,
    _message,
    _property_bag,
)


@dataclasses.dataclass
class Artifact(object):
    """A single artifact. In some cases, this artifact might be nested within another artifact."""

    contents: Optional[_artifact_content.ArtifactContent] = dataclasses.field(
        default=None, metadata={"schema_property_name": "contents"}
    )
    description: Optional[_message.Message] = dataclasses.field(
        default=None, metadata={"schema_property_name": "description"}
    )
    encoding: Optional[str] = dataclasses.field(
        default=None, metadata={"schema_property_name": "encoding"}
    )
    hashes: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "hashes"}
    )
    last_modified_time_utc: Optional[str] = dataclasses.field(
        default=None, metadata={"schema_property_name": "lastModifiedTimeUtc"}
    )
    length: int = dataclasses.field(
        default=-1, metadata={"schema_property_name": "length"}
    )
    location: Optional[_artifact_location.ArtifactLocation] = dataclasses.field(
        default=None, metadata={"schema_property_name": "location"}
    )
    mime_type: Optional[str] = dataclasses.field(
        default=None, metadata={"schema_property_name": "mimeType"}
    )
    offset: Optional[int] = dataclasses.field(
        default=None, metadata={"schema_property_name": "offset"}
    )
    parent_index: int = dataclasses.field(
        default=-1, metadata={"schema_property_name": "parentIndex"}
    )
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(
        default=None, metadata={"schema_property_name": "properties"}
    )
    roles: Optional[
        List[
            Literal[
                "analysisTarget",
                "attachment",
                "responseFile",
                "resultFile",
                "standardStream",
                "tracedFile",
                "unmodified",
                "modified",
                "added",
                "deleted",
                "renamed",
                "uncontrolled",
                "driver",
                "extension",
                "translation",
                "taxonomy",
                "policy",
                "referencedOnCommandLine",
                "memoryContents",
                "directory",
                "userSpecifiedConfiguration",
                "toolSpecifiedConfiguration",
                "debugOutputFile",
            ]
        ]
    ] = dataclasses.field(default=None, metadata={"schema_property_name": "roles"})
    source_language: Optional[str] = dataclasses.field(
        default=None, metadata={"schema_property_name": "sourceLanguage"}
    )


# flake8: noqa
