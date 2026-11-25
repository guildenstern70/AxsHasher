# ======================================================================
#  AxsHasher
#  The modern text hasher
#
#  License: ISC
#  Copyright (c) 2026, Alessio Saltarin
# ======================================================================

"""Pydantic models for hash requests and results."""

from pydantic import BaseModel, Field

from axs_hasher.hashing import Algorithm


class HashRequest(BaseModel):
    """Validated input for a hash operation."""

    algorithm: Algorithm
    text: str = Field(min_length=1)


class HashResult(BaseModel):
    """Outcome of a hash operation."""

    algorithm: Algorithm
    digest_base64: str
