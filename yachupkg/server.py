import asyncio
from random import random

async def run_server():
	server = await asyncio.start_server(handler, host="127.0.0.1", port=5050)
	async with server:
		await server.serve_forever()

async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
	while True:
		data : bytes = await reader.read(1024)
		peername = writer.get_extra_info('peername')
		print(f"[S] received: {len(data)} bytes from {peername}")
		mes = data.decode()
		print(f"[S] message: {mes}")
		res = mes.upper()[::-1]
		await asyncio.sleep(random() * 2)
		writer.write(res.encode())
		await writer.drain()

async def test():
	await asyncio.wait(run_server())

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(test())