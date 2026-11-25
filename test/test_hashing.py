"""Tests for hashing."""

import base64
import hashlib

import pytest

from axs_hasher.hashing import Algorithm, hash_to_base64


@pytest.mark.parametrize("algorithm", list(Algorithm))
def test_hash_matches_hashlib(algorithm):
    """Digest equals the independently computed Base64 hash."""
    name = algorithm.hashlib_name
    expected = base64.b64encode(hashlib.new(name, b"abc").digest()).decode()
    assert hash_to_base64(algorithm, "abc") == expected


def test_sha256_known_vector():
    """SHA-256 of 'abc' is a known value."""
    assert hash_to_base64(Algorithm.SHA256, "abc") == (
        "ungWv48Bz+pBQUDeXa4iI7ADYaOWF3qctBD/YfIAFa0="
    )
