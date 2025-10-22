"""
Model (i.e. schema/definition) of the realm data descriptor
"""

from esgvoc.api.data_descriptors.data_descriptor import PlainTermDataDescriptor


class Realm(PlainTermDataDescriptor):
    """
    Realm associated with the dataset

    Examples: "atmos", "land", "ocean", "atmosChem"

    This is intended as a rough categorisation only
    and is not precisely defined.
    """

    # TODO: delete? redundant with description and drs_name
    name: str

    # TODO: discuss. Karl had written,
    # "Note that "realm" may be assigned multiple realms, "
    # "separated by a single space, with the first one listed considered primary."
    # Can we not do this and just have single values please?
    # Otherwise this becomes a composite term,
    # which just feels annoying/overkill.
