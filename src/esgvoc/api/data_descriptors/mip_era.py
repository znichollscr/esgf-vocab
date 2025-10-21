"""
Model (i.e. schema/definition) of the MIP era data descriptor
"""

from esgvoc.api.data_descriptors.data_descriptor import PlainTermDataDescriptor


# TODO: rename to MIPEra ?
# Mip isn't a word, it's an acronym
class MipEra(PlainTermDataDescriptor):
    """
    Label that identifies the MIP era to which a dataset belongs

    Examples: "CMIP6", "CMIP7"

    The MIP era is useful to distinguish among experiments performed during different CMIP phases
    but with differences in experimental protocol in each phase.
    For example, the "historical" experiments appear in multiple phases of CMIP
    but have different input forcings in each.
    This difference can be identified using the MIP era data descriptor.
    """

    start: int
    """
    Year in which this phase started
    """
    # TODO: discuss whether we actually want to capture this in the CVs

    end: int | None
    """
    Year in which this phase ended
    """
    # TODO: discuss how to define 'ended'

    # TODO: remove as we already have drs_name and description
    name: str

    # TODO: use pydantic URL type instead
    url: str
    """
    URL that links to further information about the MIP era
    """
