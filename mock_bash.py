import os
import getpass
import socket


HOME = os.path.expanduser('~')
print(HOME)
BASE_DIR = '~' + os.path.dirname(__file__).replace(HOME, '').replace('\\', '/')
USER = getpass.getuser()
HOST = socket.gethostname()


while True:
    put = input(f'{USER}@{HOST} {BASE_DIR} $ ')
    try:
        if put == '\\exit':
            break
        exec(put)
    except Exception:
        print(f'bash: {put}: command not found')
