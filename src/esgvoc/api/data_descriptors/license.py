"""
Model (i.e. schema/definition) of the license data descriptor
"""

from esgvoc.api.data_descriptors.data_descriptor import PlainTermDataDescriptor


class License(PlainTermDataDescriptor):
    """
    License that applies to the dataset

    Examples: "CC-BY-4.0", "CC0-1.0"

    Licenses must be approved by the WIP & CMIP panel
    before they can be used in CMIP exercises.
    """

    kind: str
    # TODO: delete, covered by description, url, spdx_id and id

    spdx_id: str
    """
    SPDX license identifier (https://spdx.org/licenses/)
    """
    # Developer note: the ID will not match the spdx_id
    # exactly because SPDX IDs are not all lowercase,
    # hence we need this extra attribute.

    url: str
    """
    URL with details of the full license and other information
    """
