# 一个项目、一个运行包

当前项目统一叫 ChromaPeak，Python运行代码全部在 `chromapeak/`。它负责色谱峰检测、候选验证、EIC处理、峰边界与属性计算、外部算法适配及MS2引导补峰。

之前三个并列名称的实际职责与本次整理如下：

|旧位置|原用途|当前位置|
|---|---|---|
|`chromapeak/`|仅提供命令入口|扩展为唯一的完整运行包|
|`lipidbench/`|实际运行代码|合并到 `chromapeak/`，旧目录移除|
|`PeakTruthLab/scripts/`|数据准备、训练及评估|`scripts/`|
|`PeakTruthLab/scripts/convnext/candidate_components.py`|可复用的分类比较模型|`chromapeak/models/candidate_classifier.py`|
|`PeakTruthLab/configs/`|模型和标注配置|`configs/`|
|`PeakTruthLab/docs/`|协议、方法与审查记录|`docs/`|
|`PeakTruthLab/datasets/`|冻结清单及基准元数据|`benchmarks/`，Main基准为 `benchmarks/main_20260814/`|

这是职责分工，不是几个独立软件。`scripts/classification/` 与 `scripts/detection/` 分别服务论文分类比较和正式联合模型的训练/评估，不再各自另起一个项目名。

模型源码与可复用组件在运行包里；训练入口仍在脚本目录。真实数据、检查点、图表和依赖环境放在源码之外的本地资料目录。

## 原模型为何可以继续使用

两份正式检查点经检查只引用PyTorch张量及普通配置，没有指向旧Python包名的自定义类。使用新 `chromapeak` 包加载同一状态字典即可，不需要保留旧名称的空壳目录。
本次不改变模型数学结构、权重、16属性顺序、Train预处理、阈值、数据划分或图表数值。

历史Release的ZIP文件名、数据集标识 `PeakTruthLab_final_merged_20260814`、`seed_*` 字段及 `best_seed.pt` 文件名保留，用于与已发布文件、输入和校验值逐项核对。它们是实验版本标识，不是当前源代码项目的边界。

统一入口：`python -m chromapeak`。Python接口从 `chromapeak` 导入；数据准备和训练命令使用 `scripts/...` 的新路径。
