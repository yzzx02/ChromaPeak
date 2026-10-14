# 冻结基准元数据

这里只保留模型实验的可审查清单：候选/峰实例表、训练验证测试划分、重复组审计与锁定校验。

- `main_20260814/`：正式Main基准的冻结元数据。
- `feature_table_final_10000.csv`：历史候选来源参考表；`source_path` 使用相对于原始mzML目录的文件名，不含机器绝对路径。

完整PNG、LabelMe标注和原始mzML放在源码之外，通过 `CHROMAPEAK_DATASET_ROOT` 或 `<CHROMAPEAK_LOCAL_ROOT>/inputs/` 定位。
不要把生成图、训练输出、权重或缓存写进此目录。`main_20260814/` 内的冻结元数据及锁定哈希保持原样；历史参考表的路径字段仅用于定位来源文件。

实验背景及数量口径见 [基准说明](../docs/BENCHMARK.md)。
