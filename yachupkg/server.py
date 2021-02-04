import asyncio

async def run_server():
	server = await asyncio.start_server(handler, host="127.0.0.1", port=_port)
	async with server:
		await server.serve_forever()