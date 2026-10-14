# ChromaPeak

ChromaPeak 用于 LC–MS 色谱峰检测、候选峰真假验证、边界修正与积分，并支持 MS2 注释引导的漏检 MS1 峰补检。

模型采用共享 ConvNeXt-Tiny + FPN：全窗口检测分支只使用图像；候选验证分支结合给定候选 RoI 的视觉特征与其自身的16项属性。MS2补峰先检测并修正新候选，再计算属性和验证真假；差异分析不属于软件范围。

## 仓库结构

|目录|用途|
|---|---|
|`chromapeak/`|唯一运行代码包：模型、EIC处理、边界/属性计算、算法适配器和补峰接口|
|`scripts/`|数据准备、训练、消融比较、评估与结果打包命令|
|`configs/`|模型与标注配置，不含模型权重|
|`benchmarks/`|冻结基准清单、数据划分及审计元数据，不放原始图像|
|`docs/`|使用说明、训练协议、方法说明及历史审查记录|
|`tests/`|运行接口、模型与数据处理测试|

`chromapeak/models/` 保存正式多任务模型及论文比较所需组件；`scripts/classification/` 是候选分类比较实验，`scripts/detection/` 是联合检测/验证的训练与评估命令。正式使用的固定模型仍是同一套发布检查点。

## 安装与运行

在源码根目录执行。Python环境、缓存和输出均放在源码目录之外：

```powershell
. .\scripts\use_local_workspace.ps1
python -m venv "$env:CHROMAPEAK_LOCAL_ROOT\runtime\environments\main"
& "$env:CHROMAPEAK_LOCAL_ROOT\runtime\environments\main\Scripts\Activate.ps1"
pip install -r requirements.txt
python -m chromapeak --help
```

NVIDIA训练依赖另见 `requirements-peak-nvidia-cu128.txt` 和 [训练环境说明](docs/NVIDIA_RTX_TRAINING.md)。

所有软件功能统一从 `python -m chromapeak` 进入，例如：

```powershell
python -m chromapeak --algo pyopenms
python -m chromapeak --algo xcms,asari
python -m chromapeak --algo pyopenms --export-eic --eic-mzml /path/to/sample.mzML
python -m chromapeak rescue-ms2 --help
```

算法参数在根目录 `config.yaml`。MS2补峰接受 CSV/TSV/XLSX 鉴定表，提取前体 m/z 和MS2 RT附近的MS1 EIC，输出去重后的补回物理峰及计数，详见 [输入表与补峰接口](docs/MS2_GUIDED_RESCUE.md)。

Python接口统一从 `chromapeak` 导入，例如：

```python
from chromapeak.models import PeakMultiTaskRCNN
from chromapeak.workflows.ms2_rescue import RescueOptions, rescue_ms2_peaks
```

## 固定模型与实验数据

- 正式版本：RTX4070最终发布（2026-08-18），480×480 EIC、16项属性、朴素拼接。
- 两个正式检查点：`best_detection.pt` 与 `best_seed.pt`；后者是候选分类检查点的历史文件名。
- 属性填补和标准化只在Train拟合；Val用于模型和阈值选择；Test/LODO留出集在锁定后评估。
- Main基准含19,817个候选、18,915个峰实例，Train/Val/Test为15,853/1,982/1,982。Main保持来源比例及重复组隔离，不代表完全mzML独立划分；跨域结论采用LODO实验。
- 源码内冻结元数据位于 `benchmarks/main_20260814/`；完整输入通过 `CHROMAPEAK_DATASET_ROOT` 或默认独立输入目录定位。

校验冻结数据、查看训练入口：

```powershell
python scripts/data_prep/verify_rtx4070_final_merged_dataset.py
python scripts/detection/run_rtx4070_multitask_concat_pipeline.py --help
```

完整训练/评估说明见 [工作流入口](docs/TRAINING_WORKFLOWS.md)、[基准与协议](docs/BENCHMARK.md) 和 [冻结实验协议](docs/FROZEN_EXPERIMENT_PROTOCOL.md)。

正式模型和数据集通过 [GitHub Release](https://github.com/yzzx02/ChromaPeak/releases/tag/rtx4070-final-20260818) 获取。历史发布包文件名、数据集版本标识、`seed_*` 字段与固定校验值用于核对原始实验。历史RT平移实验的输入和运行方式见 [RT复现指南](scripts/rt_validation/README.md)。

## 数据目录配置

输入数据、模型权重、运行结果和缓存建议保存在源码目录之外，使用软件不需要将这些文件上传 GitHub。

`CHROMAPEAK_LOCAL_ROOT` 设置外部工作目录，默认使用源码同级的 `<项目名>-local`；`CHROMAPEAK_CACHE_ROOT` 和 `CHROMAPEAK_DATASET_ROOT` 分别设置缓存目录与完整基准数据集目录。训练入口支持通过 `CHROMAPEAK_PROJECT_ROOT` 指定源码根目录。

`.gitignore` 排除原始数据、模型权重、图表、运行环境、结果和缓存；仓库仅保留源码、通用配置、文档及明确列出的冻结基准元数据。
