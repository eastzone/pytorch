# This file was generated by jschema_to_python version 0.0.1.dev29.

from __future__ import annotations

import dataclasses
from typing import Any, List, Optional

from torch.onnx._internal.diagnostics.infra.sarif_om import (
    _multiformat_message_string,
    _property_bag,
    _reporting_configuration,
    _reporting_descriptor_relationship,
)


@dataclasses.dataclass
class ReportingDescriptor(object):
    """Metadata that describes a specific report produced by the tool, as part of the analysis it provides or its runtime reporting."""

    id: str = dataclasses.field(metadata={"schema_property_name": "id"})
    default_configuration: Optional[
        _reporting_configuration.ReportingConfiguration
    ] = dataclasses.field(
        default=None, metadata={"schema_property_name": "defaultConfiguration"}
    )
    deprecated_guids: Optional[List[str]] = dataclasses.field(
        default=None, metadata={"schema_property_name": "deprecatedGuids"}
    )
    deprecated_ids: Optional[List[str]] = dataclasses.field(
        default=None, metadata={"schema_property_name": "deprecatedIds"}
    )
    deprecated_names: Optional[List[str]] = dataclasses.field(
        default=None, metadata={"schema_property_name": "deprecatedNames"}
    )
    full_description: Optional[
        _multiformat_message_string.MultiformatMessageString
    ] = dataclasses.field(
        default=None, metadata={"schema_property_name": "fullDescription"}
    )
    guid: Optional[str] = dataclasses.field(
        default=None, metadata={"schema_property_name": "guid"}
    )
    help: Optional[
        _multiformat_message_string.MultiformatMessageString
    ] = dataclasses.field(default=None, metadata={"schema_property_name": "help"})
    help_uri: Optional[str] = dataclasses.field(
        default=None, metadata={"schema_property_name": "helpUri"}
    )
    message_strings: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "messageStrings"}
    )
    name: Optional[str] = dataclasses.field(
        default=None, metadata={"schema_property_name": "name"}
    )
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(
        default=None, metadata={"schema_property_name": "properties"}
    )
    relationships: Optional[
        List[_reporting_descriptor_relationship.ReportingDescriptorRelationship]
    ] = dataclasses.field(
        default=None, metadata={"schema_property_name": "relationships"}
    )
    short_description: Optional[
        _multiformat_message_string.MultiformatMessageString
    ] = dataclasses.field(
        default=None, metadata={"schema_property_name": "shortDescription"}
    )


# flake8: noqa
