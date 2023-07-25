import psutil
import sys
import hashlib

def get_file_signature(file_path):
    BUF_SIZE = 65536
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

for proc in psutil.process_iter(['pid', 'name', 'exe']):
    try:
        process_info = proc.info
        signature = get_file_signature(process_info['exe'])
        print(f"Process Name: {process_info['name']}")
        print(f"Process Path: {process_info['exe']}")
        print(f"Signature: {signature}\n")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)