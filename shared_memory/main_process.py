import pickle
import sys
from multiprocessing import shared_memory
import time

try:
    shm = shared_memory.SharedMemory(create=True, size=100, name="test")
except:
    print("メモリ作成エラー")
    sys.exit(1)

# データ格納
while True:

    brother = {
        "1": "taro",
        "2": "jiro",
        "3": "saburo"
    }
    data = pickle.dumps(brother)
    shm.buf[:len(data)] = data
    time.sleep(1)
