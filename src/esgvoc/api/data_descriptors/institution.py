"""
Model (i.e. schema/definition) of the institution data descriptor
"""

from pydantic import Field

from esgvoc.api.data_descriptors.data_descriptor import PlainTermDataDescriptor


class Institution(PlainTermDataDescriptor):
    """
    A registered institution acronym

    Examples: "IPSL", "CR", "NCAR"
    """

    # TODO: discuss whether there are any restrictions in the ID

    acronyms: list[str] = Field(default_factory=list)
    """
    Known acronyms for this institution apart from the registered one

    The registered acronym is given in `self.drs_name`.
    """

    aliases: list[str] = Field(default_factory=list)
    # TODO: remove as we already have acronyms?

    established: int | None
    """
    Year in which this institute was established

    If `None`, no establishment year is defined/was supplied at registration time.
    """

    labels: list[str] = Field(default_factory=list)
    """
    Labels that can be used for this institute

    These are free-text and can be used when the label needs to be referred to in full,
    rather than by its acronym.
    This can also be thought of as 'long names'.
    """
    # TODO: discuss whether there is any meaning to the order of these
    # and what it means to have more than one label.
    # TODO: discuss whether we should just call this long_names
    # for consistency with other conventions.

    location: dict = Field(default_factory=dict)
    """
    Location of the institute

    Any keys can be used here.
    [TODO consider whether we want to be more careful than this
    and introduce a Location class]
    Recommend keys are "city" (str),
    "country" (str),
    "lat" (float, degrees north) and "lon" (float, degres east).
    """

    name: str
    # TODO: surely delete given we already have description,
    # drs_name, acronyms and labels.

    ror: str | None
    """
    Research organisation registry (https://ror.org/) ID

    If `None`, this organisation is not registered with ROR
    or the ROR was not supplied at the time of registration.
    """

    urls: list[str] = Field(default_factory=list)
    """
    URLs relevant for finding out more information about this institute
    """
