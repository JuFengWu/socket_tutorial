import pickle
import time
import sys
from multiprocessing import shared_memory
  

count = 0
start = time.time()

while True:
  
    try:
        shm = shared_memory.SharedMemory(name="test")
    except:
        print("取得エラー")
        break
    else:
  
        try:
            data = pickle.loads(shm.buf)
        except pickle.UnpickingError:
            continue
        except:
            print("読み込みエラー")
            sys.exit(1)
        else:

            if (time.time() - start) > 5:

                shm.close()
                #shm.unlink()
                print("close")

                break
