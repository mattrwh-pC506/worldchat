from collections import namedtuple

from common.utils.safe_getattr import safe_getattr

def build_obj(goodkey: str):
    SUT = namedtuple("SUT", [goodkey])
    return SUT(goodkey=True)


def test_safe_getattr_returns_value_when_exists():
    goodkey = "goodkey"
    test_obj = build_obj(goodkey)
    assert safe_getattr(test_obj, goodkey) == True, "goodkey returns value"

def test_safe_getattr_returns_none_when_it_doesnt_exist():
    goodkey = "goodkey"
    badkey = "badkey"
    test_obj = build_obj(goodkey)
    assert safe_getattr(test_obj, badkey) == None, "badkey returns None"

def test_safe_getattr_returns_default_when_it_doesnt_exist_but_default_is_provided():
    goodkey = "goodkey"
    badkey = "badkey"
    default = "default"
    test_obj = build_obj(goodkey)
    assert safe_getattr(test_obj, badkey, default) == default, "badkey returns default when provided"
