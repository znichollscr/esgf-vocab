"""
Model (i.e. schema/definition) of the forcing index data descriptor
"""

from esgvoc.api.data_descriptors.data_descriptor import CompositeTermDataDescriptor


class VariantLabel(CompositeTermDataDescriptor):
    """
    The variant which provides information about how a dataset was created

    Examples: "r1i1p1f1", "r2i2p2f1", "r1i198001p1f1", "r1i198001ap1f1", "r1i199001bp1f1"

    The variant label is composed of the following components:

    #. :py:class:`RealisationIndex`
    #. :py:class:`InitialisationIndex`
    #. :py:class:`PhysicIndex`
    #. :py:class:`ForcingIndex`
    """

    # TODO discuss: verification isn't an issue,
    # because the components are all governed by regexp's
    # (so if the components match the regexp, the variant label will be valid).
    # However, as there is no separator,
    # it would be much harder to support splitting the variant label
    # back into its parts (if that is something we want to support).
