import subprocess

ip = '127.0.0.1'

ping_reply = subprocess.call('ping %s /n 2' % (ip), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)

print(ping_reply)