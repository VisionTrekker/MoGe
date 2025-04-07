import os
GPU_ID = 2

cmd = f"CUDA_VISIBLE_DEVICES={GPU_ID} \
       python3 infer.py \
       --input /data2/liuzhi/remote_data/dataset_reality/test/t100pro_out_Subway \
       --output /data2/liuzhi/remote_data/dataset_reality/test/t100pro_out_Subway \
       "
print(cmd)
os.system(cmd)