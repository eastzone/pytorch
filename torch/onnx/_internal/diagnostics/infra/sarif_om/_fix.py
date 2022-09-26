# This file was generated by jschema_to_python version 0.0.1.dev29.

from __future__ import annotations

import dataclasses
from typing import List, Optional

from torch.onnx._internal.diagnostics.infra.sarif_om import (
    _artifact_change,
    _message,
    _property_bag,
)


@dataclasses.dataclass
class Fix(object):
    """A proposed fix for the problem represented by a result object. A fix specifies a set of artifacts to modify. For each artifact, it specifies a set of bytes to remove, and provides a set of new bytes to replace them."""

    artifact_changes: List[_artifact_change.ArtifactChange] = dataclasses.field(
        metadata={"schema_property_name": "artifactChanges"}
    )
    description: Optional[_message.Message] = dataclasses.field(
        default=None, metadata={"schema_property_name": "description"}
    )
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(
        default=None, metadata={"schema_property_name": "properties"}
    )


# flake8: noqa
