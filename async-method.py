import socketio
import asyncio
import time

sio = socketio.AsyncSimpleClient()


class Socket:
    def __init__(self):
        self.sio = socketio.AsyncSimpleClient()

    async def connect(self):
        await self.sio.connect('http://localhost:3000')

    @   
    async def sent(self, i):
        await self.sio.emit('hello', {'foo': f'bar {i}'})

    async def disconnect(self):
        time.sleep(5)
        await self.sio.disconnect()

async def main():
    s = Socket()
    await s.connect()
    for i in range(1, 100000):
        print(i)
        await s.sent(i)
    # await s.disconnect()



async def say_hello():
    await sio.connect('http://localhost:3000')
    for i in range(1, 1000000):
        await sio.emit('hello', {'foo': f'bar {i}'})
        # time.sleep(.01)
    # await sio.disconnect()

asyncio.run(main())