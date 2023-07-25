import psutil
import sys
import hashlib
import time

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

def check_and_terminate(signature_to_check):
    
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            try:
                process_info = proc.info
                signature = get_file_signature(process_info['exe'])
                if signature == signature_to_check:
                    print(f"Matching process found: {process_info['name']} ({process_info['pid']})")
                    print(f"Terminating process...\n")
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
            except Exception as e:
                print(f"Error: {e}", file=sys.stderr)
                

signature_to_check = "30551534c5515afdea5fc76f33935a32c66688f5665ff171686c2b42d8c0b2cf"
check_and_terminate(signature_to_check)