# ======================================================================
#  AxsHasher
#  The modern text hasher
#
#  License: ISC
#  Copyright (c) 2026, Alessio Saltarin
# ======================================================================

"""Interactive command line flow."""

import pyperclip
import questionary

from axs_hasher.hashing import Algorithm, hash_to_base64
from axs_hasher.models import HashRequest, HashResult


def run() -> None:
    """Ask for an algorithm and a phrase, print the digest, optionally copy it."""
    algorithm = questionary.select(
        "Algorithm:", choices=[a.value for a in Algorithm]
    ).ask()
    if algorithm is None:
        return
    text = questionary.text("Phrase to hash:").ask()
    if text is None:
        return
    request = HashRequest(algorithm=Algorithm(algorithm), text=text)
    result = HashResult(
        algorithm=request.algorithm,
        digest_base64=hash_to_base64(request.algorithm, request.text),
    )
    print(result.digest_base64)
    if questionary.confirm("Copy to clipboard?").ask():
        try:
            pyperclip.copy(result.digest_base64)
        except pyperclip.PyperclipException as exc:
            print(f"Could not copy to clipboard: {exc}")
