import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


@pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected



def test_set_key_value():
    h = Hashtable()
    h.set("foo", "bar")
    assert h.table[h.hash("foo")] == [("foo", "bar")]

def test_get_key_value():
    h = Hashtable()
    h.set("foo", "bar")
    assert h.get("foo") == "bar"

def test_get_null_for_nonexistent_key():
    h = Hashtable()
    assert h.get("nonexistent") is None

def test_keys_list():
    h = Hashtable()
    h.set("foo", "bar")
    h.set("baz", "qux")
    assert h.keys() == ["foo", "baz"]

def test_handle_collision():
    h = Hashtable()
    h.set("foo", "bar")
    h.set("oof", "rab")
    assert h.table[h.hash("foo")] == [("foo", "bar"), ("oof", "rab")]

def test_retrieve_value_from_collision_bucket():
    h = Hashtable()
    h.set("foo", "bar")
    h.set("oof", "rab")
    assert h.get("oof") == "rab"

def test_hash_key_to_in_range_value():
    h = Hashtable()
    assert 0 <= h.hash("key") < 256
