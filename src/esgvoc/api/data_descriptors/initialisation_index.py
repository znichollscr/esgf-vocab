"""
Model (i.e. schema/definition) of the initialisation index data descriptor
"""

from esgvoc.api.data_descriptors.data_descriptor import PatternTermDataDescriptor


# TODO: check spelling c/f InitializationIndex
class InitialisationIndex(PatternTermDataDescriptor):
    r"""
    Label that identifies the initialisation variant used to produce a dataset

    Examples: "i1", "i2", "i196001", "i201001", "i201001a", "i201001b"

    This label can be used, for example, to distinguish between two simulations
    that were initialised in different ways or on different dates
    (this is most commonly used for decadal prediction simulations).

    When this is of the form `i\d*`, the value has no intrinsic meaning within the CVs.
    However, in other external sources (to be confirmed which)
    the meaning of this initialisation label for a given simulation can be looked up.

    When this is of the form `i\d{6}[abcde]?`,
    the digits indicate the year and month used for initialising the simulation,
    with any suffix letter used to distinguish
    between simulations that differ in their initialisation
    but nonetheless use the same year and month.
    """

    # TODO: in CMIP6 the regexp would have been `\d*` i.e. any integer
    # but apparently for CMIP7 this should now be
    # `i\d*` i.e. "i" followed by any integer
    # or `i(?<year>\d{4})(?<month>\d{2})[abcde]?`
    # i.e. "i" followed by initialisation year and month
    # and then an optional a, b, c, d or e.
