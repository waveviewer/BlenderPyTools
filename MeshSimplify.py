import bpy
import os
import time
import argparse
import logging
from pathlib import Path, PurePath

meshpath = Path("D:\\Mesh\\test1\\combine1_sub.ply")
ratio = 0.1

if not meshpath.exists():
    print("Can not open mesh file : ", meshpath)
    exit(-1)

meshname = meshpath.stem
print(meshname)
logger = logging.getLogger(meshname)
time_now = time.strftime("%Y%m%d", time.localtime())
logger_dir = "simplify_logs"
if not os.path.isdir(logger_dir):
    os.mkdir(logger_dir)
logger_filename = "{}/{}_{}.log".format(logger_dir, time_now, meshname)
ch = logging.FileHandler(filename=logger_filename, encoding="utf-8")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)


# simplify
read_mesh_start = time.perf_counter_ns()
if meshpath.suffix == ".ply":
    bpy.ops.import_mesh.ply(filepath=str(meshpath))
elif meshpath.suffix == ".obj":
    bpy.ops.import_scene.obj(filepath=str(meshpath), filter_glob="*.obj;*.mtl")
read_mesh_end = time.perf_counter_ns()
logger.info("read mesh takes {} ms".format((read_mesh_end-read_mesh_start)/1000/1000))

# for obj in bpy.data.objects:
#     print(obj.name)

bpy.ops.object.select_all(action="DESELECT")

for elem in bpy.data.objects:
    if elem.name == meshname:
        decimate_start = time.perf_counter_ns()
        modifier = elem.modifiers.new("collapse", "DECIMATE")
        modifier.ratio = ratio
        modifier.use_collapse_triangulate = True
        elem.select_set(True)
        decimate_end = time.perf_counter_ns()
        print("Collapse time used {} ms".format((decimate_end-decimate_start) / 1000000))
        logger.info("ratio is {}".format(modifier.ratio))
        logger.info("Collapse takes {} ms".format((decimate_end - decimate_start) / 1000 / 1000))
savepath = Path("results") / "blender_{}_{}.ply".format(ratio, meshname)
print(savepath)
bpy.ops.export_mesh.ply(filepath=str(savepath), filter_glob="*.ply", use_selection=True)
logger.info("write result into {}".format(savepath))
