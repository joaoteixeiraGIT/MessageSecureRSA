import asyncio
import websockets
import threading

async def handle_messages(websocket):
    while True:
        try:
            message = await websocket.recv()  # Receive message from server
            print(f"Received message: {message}")  # Print received message
        except websockets.exceptions.ConnectionClosed:
            print("Connection to server closed")
            break

def send_messages_sync(websocket):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_messages(websocket))

async def send_messages(websocket):
    while True:
        recipient_ip = input("Insira o IP do destinatário: ")
        message = input(f"Digite a mensagem para enviar para IP:{recipient_ip} (ou 'exit' para sair): ")
        if message == 'exit':
            await websocket.close()
            print("Conexão encerrada.")
            break
        await websocket.send(f"{recipient_ip} {message}")

async def connect_to_server():
    async with websockets.connect('ws://localhost:8765') as websocket:
        print("Conectado ao servidor.")
        threading.Thread(target=send_messages_sync, args=(websocket,)).start()
        await handle_messages(websocket)

# Inicia o cliente WebSocket
asyncio.run(connect_to_server())
