import os
GPU_ID = 0

scene = "t100pro_out_ST"

cmd = f"CUDA_VISIBLE_DEVICES={GPU_ID} \
       python3 infer.py \
       --input /data2/liuzhi/remote_data/dataset_reality/test/{scene}/images \
       --output /data2/liuzhi/remote_data/dataset_reality/test/{scene} \
       "
print(cmd)
os.system(cmd)