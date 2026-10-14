# ChromaPeak on NVIDIA RTX

The current release uses 480 x 480 EIC images, exactly 16 candidate attributes, shared ConvNeXt-Tiny + FPN, Faster R-CNN detection, and naive concatenation in the candidate head.

## Environment

The validated NVIDIA runtime is Python 3.12, PyTorch 2.9.1 + CUDA 12.8, and torchvision 0.24.1. Install the matching NVIDIA driver, then run from the checkout root:

```powershell
. .\scripts\use_local_workspace.ps1
powershell -ExecutionPolicy Bypass -File scripts\setup_nvidia_cu128.ps1
& "$env:CHROMAPEAK_LOCAL_ROOT\runtime\environments\nvidia-cu128\Scripts\Activate.ps1"
```

The setup installs the common training dependencies and the CUDA wheels, then checks GPU availability.

## Final data

Set `CHROMAPEAK_DATASET_ROOT` to the extracted final dataset, containing 19,817 EIC windows and their 16-attribute manifests. The default location is `<CHROMAPEAK_LOCAL_ROOT>/inputs/PeakTruthLab_final_merged_20260814`. See [the benchmark documentation](BENCHMARK.md) for the published dataset and protocol.

## Released joint workflow

```powershell
python scripts/detection/run_rtx4070_multitask_concat_pipeline.py
```

Default training settings are physical/effective batch size 16, up to 30 epochs, 480 x 480 input, FP16 AMP, AdamW, learning rate 1e-4, weight decay 1e-4, and no augmentation. The pipeline selects checkpoints and thresholds on Val before locked target evaluation.

For candidate-classification comparisons and LODO, use the maintained entry points listed in `docs/TRAINING_WORKFLOWS.md`. Each command supports `--help`; none of the removed staged-training wrappers is needed.

Paths are inferred from the checkout. `CHROMAPEAK_PROJECT_ROOT` may override the root; existing `LIPIDBENCH_PROJECT_ROOT` settings are also accepted.
