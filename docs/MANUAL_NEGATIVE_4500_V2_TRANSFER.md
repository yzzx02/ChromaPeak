# ChromaPeak manual-negative 4500 v2 transfer

This release contains two completed LabelMe batches (3000 + 1500 images).
It is an additive dataset package for the final merged benchmark. Rebuilding
that benchmark requires the version-verified, reviewed old-batch annotations.

## Release asset

- Tag: `peaktruthlab-manual-negative-4500-v2`
- Asset: `PeakTruthLab_manual_negative_4500_v2_20260814.zip`
- SHA256: `F89632310064E5F92A484AB7FD75A05ABF3DC55631F7077B2C9A328D4F0CB409`

## Validated contents

- 4,500 corrected PNG files and 4,500 corrected LabelMe JSON files.
- 4,242 images without retained boxes (negative Seed candidates).
- 328 `True_Peak` boxes and 7 `OUT_FIG` boxes (335 boxes total).
- 4,500 rows in `原始种子属性表.csv`.
- 335 rows in `真峰实例属性表.csv`.
- All 16 Seed and retained-peak attributes are finite; no NaN or infinity.
- All seven `OUT_FIG` boxes are pinned to the appropriate plot edge.
- `HARDNEG3000_20260813READY__PLAT__D03P_POS__F0108` was restored to its
  original Seed bounds and passed full recomputation.

The archive intentionally omits the byte-identical original-annotation backup
to avoid duplicating roughly 125 MB. The source-repair audit and the full
standardization self-check are included.

## Merge and split

Follow [the frozen experiment protocol](FROZEN_EXPERIMENT_PROTOCOL.md) to
reconstruct the merged benchmark. The main benchmark uses a
leakage-controlled, sample-level stratified random split. A separate manifest
must be produced for whole-source cross-domain evaluation.
