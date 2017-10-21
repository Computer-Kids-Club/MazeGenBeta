
import asyncio
import datetime
import random
import websockets
import json
from TnakServer import *

async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        ##await websocket.send(now)
        
        await websocket.send(json.dumps({'verWall': verWallList}))
        await websocket.send(json.dumps({'horWall': horWallList}))

        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
