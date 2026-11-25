"""Tests for models."""

import pytest
from pydantic import ValidationError

from axs_hasher.hashing import Algorithm
from axs_hasher.models import HashRequest


def test_empty_text_rejected():
    """Empty text is invalid."""
    with pytest.raises(ValidationError):
        HashRequest(algorithm=Algorithm.SHA256, text="")


def test_invalid_algorithm_rejected():
    """Unknown algorithm is invalid."""
    with pytest.raises(ValidationError):
        HashRequest(algorithm="MD5", text="abc")
