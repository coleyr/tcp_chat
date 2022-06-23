import threading
import socket
from playsound import playsound

nickname = input("Choose a nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8001))
mute = False

def recieve():
    global mute
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'Nickname':
                client.send(nickname.encode('ascii'))
            else:
                if not mute:
                    playsound('ring.wav')
                print(message)
        except Exception as e:
            print(f"An error occured \n {e}")
            client.close()
            break
def write():
    global mute
    while True:
        message = input('')
        if message.lower() == 'mute':
            mute = True
        elif message.lower() == 'unmute':
            mute = False
        else:
            fmt_mesg = f"{nickname}: {message}"
            client.send(fmt_mesg.encode('ascii'))
        
recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()