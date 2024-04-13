import os
import subprocess
import concurrent.futures

# 检查调用路径
call_path = os.path.abspath(os.getcwd())
call_hp_modbus = str(os.getcwd()) + "/src/application/modbus"


#这样我们就可以根据需要添加对新HoneyPot的调用
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(lambda: subprocess.run(["python3", "honeypot.py"], cwd=call_hp_modbus))