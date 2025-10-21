"""
Model (i.e. schema/definition) of the nominal resolution data descriptor
"""

from esgvoc.api.data_descriptors.data_descriptor import PlainTermDataDescriptor


class NominalResolution(PlainTermDataDescriptor):
    """
    Approximate horizontal resolution of a dataset

    Examples: "1 km", "250 km", "500 km"

    Calculated according to the algorithm given in
    [TODO: link to algorithm which can be used to calculate this for a given dataset,
    maybe put this algorithm in esgvoc]
    """

    # Given this isn't a pattern term data descriptor,
    # I suggest splitting these out
    # so people don't have to parse the drs_name themselves
    magnitude: float
    """
    Magnitude of the nominal resolution
    """

    unit: str
    """
    Unit of the nominal resolution
    """
