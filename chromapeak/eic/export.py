"""Deprecated module.

EIC export pipeline has been unified to:
  chromapeak.eic.extract_eic_pyopenms.build()

Please update callers to use the unified build-based flow.
"""

from __future__ import annotations


def __getattr__(name: str):
    raise AttributeError(
        "chromapeak.eic.export is deprecated. "
        "Use chromapeak.eic.extract_eic_pyopenms.build instead."
    )
