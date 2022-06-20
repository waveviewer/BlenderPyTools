# Blender Simplification
本工具调用Blender的python接口，在命令行中对模型进行化简，不打开blender的图形界面，并记录简化耗时在日志文件中。

## Requirements
- Blender https://www.blender.org/ 
- python >= 3.7 (在python 3.9.7 中测试成功)

## 用法
在MeshSimplify.py中给出需要简化的模型和简化比例
```python
meshpath = Path("D:\\Mesh\\test1\\combine1_sub.ply")
ratio = 0.1
```
然后在命令行中将.py脚本做参数传递给Blender.exe(Linux系统下方法一致)
```commandline
blender.exe -b -P .\MeshSimplify.py
```

日志文件写入`simplify_logs`文件夹，命名格式为`{年月日}_{模型名}.log`

日志内容示例
```text
2022-06-16 16:38:24,393 - INFO - read mesh takes 411.06559999999996 ms
2022-06-16 16:38:24,393 - INFO - ratio is 0.10000000149011612
2022-06-16 16:38:24,393 - INFO - Collapse takes 0.0668 ms
2022-06-16 16:38:24,536 - INFO - write result into results\blender_0.1_combine1_sub.ply
```