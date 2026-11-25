# ======================================================================
#  AxsHasher
#  The modern text hasher
#
#  License: ISC
#  Copyright (c) 2026, Alessio Saltarin
# ======================================================================

"""Pure hashing logic."""

import base64
import hashlib
from enum import Enum


class Algorithm(str, Enum):
    """Supported algorithms; values are display names."""

    SHA256 = "SHA-256"
    SHA512 = "SHA-512"
    SHA3_256 = "SHA3-256"
    SHA3_512 = "SHA3-512"
    BLAKE2B = "BLAKE2b"
    BLAKE2S = "BLAKE2s"

    @property
    def hashlib_name(self) -> str:
        """Return the name understood by hashlib."""
        name = self.value.lower()
        return name.replace("-", "_") if name.startswith("sha3") else name.replace("-", "")


def hash_to_base64(algorithm: Algorithm, text: str) -> str:
    """Hash text with the algorithm and return the Base64 digest."""
    digest = hashlib.new(algorithm.hashlib_name, text.encode("utf-8")).digest()
    return base64.b64encode(digest).decode("ascii")
