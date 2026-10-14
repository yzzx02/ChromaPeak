# 数据准备、训练与评估命令

这些脚本共同服务于 ChromaPeak，运行代码和模型实现统一从 `chromapeak` 包导入。
从仓库根目录运行 `python scripts/<分组>/<脚本>.py --help` 查看参数。

|分组|用途|
|---|---|
|`data_prep/`|构建/校验数据、生成清单、划分和EIC|
|`annotation/`|人工标注检查、边界标准化和属性重算|
|`classification/`|候选真假分类及信息融合消融比较|
|`detection/`|联合峰检测与候选验证的训练、评估及审计|
|`reporting/`|结果审计和正式资产打包|
|`rt_validation/`|历史RT平移实验的复现工具|

维护中的模型入口与固定协议见 [工作流说明](../docs/TRAINING_WORKFLOWS.md)。可复用的模型组件放在 `chromapeak/models/`，不是另一套脚本子项目。
