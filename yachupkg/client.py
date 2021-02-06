import asyncio

async def run_client(host : str, port : int):
	reader : asyncio.StreamReader
	writer : asyncio.StreamWriter
	reader, writer = await asyncio.open_connection(host, port)

	print("[C] connected")

	while True:
		line = input("[C] enter message: ")
		if not line:
			break;

		payload = line.encode()
		writer.write(payload)
		await writer.drain()
		print(f"[C] sent: {len(payload)} bytes.\n")

		data = await reader.read(1024)
		print(f"[C] received: {len(data)} bytes")
		print(f"[C] message: {data.decode()}")

	print("[C] closing connection...")
	writer.close()
	await writer.wait_closed()

if __name__ == "__main__":
	run_client("127.0.0.1", 5050)