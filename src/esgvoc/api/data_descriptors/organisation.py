"""
Model (i.e. schema/definition) of the organisation data descriptor
"""

from esgvoc.api.data_descriptors.consortium import Consortium
from esgvoc.api.data_descriptors.data_descriptor import PlainTermDataDescriptor
from esgvoc.api.data_descriptors.institution import Institution


class Organisation(PlainTermDataDescriptor):
    """
    A registered organisation acronym

    Examples: "IPSL", "CR", "SOLARIS-HEPPA"

    This can either be a single institute or a consortium of institutes.
    """

    # TODO: discuss - this is a bit messy.
    # Could just move these attributes onto `Source` and delete `Organisation` altogether.
    # Might be cleaner/simpler because it removes a layer?
    consortium: Consortium | None
    """
    Consortium that defines this organisation

    If `None`, then this organisation is composed of a single institute
    """

    institution: Institution | None
    """
    Institution that defines this organisation

    If `None`, then this organisation is a consortium
    """

    # TODO: add validation that either institution or consortium
    # is provided but not neither and not both
