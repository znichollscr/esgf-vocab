"""
Model (i.e. schema/definition) of the variable data descriptor
"""

from pydantic import Field

from esgvoc.api.data_descriptors.data_descriptor import PlainTermDataDescriptor


class Variable(PlainTermDataDescriptor):
    """
    A climate-related quantity or measurement.

    Examples: "tas", "pr", "psl", "rlut"

    These quantities represent key physical, chemical or biological properties of the Earth system
    and can be the result of direct observation of the climate system or simulations.
    Variables cover a range of aspects of the climate system,
    such as temperature, precipitation, sea level, radiation, or atmospheric composition.
    Some more information for variables that have been used in CMIP:

    - *tas*: Near-surface air temperature (measured at 2 meters above the surface)
    - *pr*: Precipitation
    - *psl*: Sea-level pressure
    - *zg*: Geopotential height
    - *rlut*: Top-of-atmosphere longwave radiation
    - *siconc*: Sea-ice concentration
    - *co2*: Atmospheric CO2 concentration

    Since CMIP7, the concept of a variable has been augmented with the idea of 'branding',
    leading to the idea of a 'branded variable'.
    For details, see :py:class:`BrandedVariable`.
    """

    validation_method: str = Field(default="list")
    # TODO: discuss, what is this?
    # Why is the default a list given the type is str?

    long_name: str
    """
    Long name of the variable

    This is free text and can take any value
    """

    # TODO: discuss whether we should validate that this is known by CF
    # if it is provided.
    # That would require somehow scraping
    # https://cfconventions.org/Data/cf-standard-names/current/build/cf-standard-name-table.html
    # I have asked David if there's a better way
    standard_name: str | None
    """
    Standard name of the variable

    The standard names are defined by the CF-conventions.

    If `None`, this variable has no standard name according to the CF-conventions.
    """

    # # TODO: forbid `None` i.e. change to
    # units: str
    units: str | None
    """
    Units of the variable
    """
