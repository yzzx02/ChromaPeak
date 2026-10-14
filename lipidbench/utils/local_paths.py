"""Locations for machine-local outputs and caches outside the source checkout."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any


def get_local_root(project_root: Path | None = None) -> Path:
    override = os.environ.get("CHROMAPEAK_LOCAL_ROOT")
    if override:
        return Path(os.path.expandvars(override)).expanduser().resolve()
    root = project_root or Path(__file__).resolve().parents[2]
    return root.parent / f"{root.name}-local"


def get_cache_root(project_root: Path | None = None) -> Path:
    override = os.environ.get("CHROMAPEAK_CACHE_ROOT")
    if override:
        return Path(os.path.expandvars(override)).expanduser().resolve()
    return get_local_root(project_root) / "cache"


def get_dataset_root(project_root: Path | None = None) -> Path:
    """Locate the frozen input dataset independently of the source checkout.

    Existing installations with images inside the checkout remain supported.
    New installations keep the full dataset in the sibling local storage.
    """
    override = os.environ.get("CHROMAPEAK_DATASET_ROOT")
    if override:
        return Path(os.path.expandvars(override)).expanduser().resolve()
    root = project_root or Path(__file__).resolve().parents[2]
    name = "PeakTruthLab_final_merged_20260814"
    external = get_local_root(root) / "inputs" / name
    legacy = root / "PeakTruthLab" / "datasets" / name
    if external.is_dir() or not (legacy / "images").is_dir():
        return external
    return legacy


def expand_local_paths(value: Any) -> Any:
    """Expand the two supported local-storage placeholders in configuration."""
    if isinstance(value, dict):
        return {key: expand_local_paths(item) for key, item in value.items()}
    if isinstance(value, list):
        return [expand_local_paths(item) for item in value]
    if isinstance(value, str):
        return value.replace("${CHROMAPEAK_LOCAL_ROOT}", str(get_local_root())).replace(
            "${CHROMAPEAK_CACHE_ROOT}", str(get_cache_root())
        )
    return value
