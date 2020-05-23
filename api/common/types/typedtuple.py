from typing import Dict, Any
from collections import namedtuple

class TypedTuple:
    instance: namedtuple = None

    def __init__(self, name: str, keys: list, *args, **kwargs):
        defaults = [None for key in keys]
        self.instance = namedtuple(name, keys, *args, defaults=defaults, **kwargs)

    def __call__(self, *args, **kwargs) -> namedtuple:
        safe_field_keys =  [field for field in self.instance._fields if field in kwargs]
        safe_field_values =  [kwargs[field] for field in safe_field_keys]
        return self.instance(**dict(zip(safe_field_keys, safe_field_values)))


def typed_tuple_to_dict(typedtuple: TypedTuple) -> Dict:
    return unpack(typedtuple)

def isnamedtupleinstance(typedtuple: Any):
    _type = type(typedtuple)
    bases = _type.__bases__
    if len(bases) != 1 or bases[0] != tuple:
        return False
    fields = getattr(_type, '_fields', None)
    if not isinstance(fields, tuple):
        return False
    return all(type(i)==str for i in fields)

def unpack(typedtuple: TypedTuple):
    if isinstance(typedtuple, dict):
        return {key: unpack(value) for key, value in typedtuple.items()}
    elif isinstance(typedtuple, list):
        return [unpack(value) for value in typedtuple]
    elif isnamedtupleinstance(typedtuple):
        return {key: unpack(value) for key, value in typedtuple._asdict().items()}
    elif isinstance(typedtuple, tuple):
        return tuple(unpack(value) for value in typedtuple)
    else:
        return typedtuple
