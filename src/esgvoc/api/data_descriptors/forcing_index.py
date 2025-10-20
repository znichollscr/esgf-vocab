"""
Model (i.e. schema/definition) of the forcing index data descriptor
"""

from esgvoc.api.data_descriptors.data_descriptor import PatternTermDataDescriptor


class ForcingIndex(PatternTermDataDescriptor):
    """
    Label that identifies the forcing variant used to produce a dataset

    Examples: "f1", "f2", "f23"

    This label distinguishes runs conforming to the experiment protocol,
    but with different variants of forcing applied.
    This can be used, for example, to distinguish between two historical simulations,
    one forced with the recommended forcing data sets
    and another forced by a different dataset,
    which might yield information about how forcing uncertainty affects the simulation.
    The value has no intrinsic meaning within the CVs.
    However, in other external sources (to be confirmed which)
    the meaning of this forcing label for a given simulation can be looked up.
    """

    # TODO: in CMIP6 the regexp would have been `\d*` i.e. any integer
    # but apparently for CMIP7 this should now be `f\d*` i.e. "f" followed by any integer.
