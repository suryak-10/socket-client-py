import socketio
import time

sio = socketio.SimpleClient()

def say_hello():
    sio.connect('http://localhost:3000')
    for i in range(1, 100):
        sio.emit('hello', {'foo': f'bar {i}'})
        time.sleep(.1)
        
say_hello()
