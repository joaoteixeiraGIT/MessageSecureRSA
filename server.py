import asyncio
import websockets
import uuid

# Dicionário para ver clientes conectados
clients = {}

async def handle_client(websocket, path):
    # Adiciona o cliente à lista de clientes conectados
    # When a new client connects, store their WebSocket in the connections dictionary
    # For simplicity, we'll use the client's IP as the key
    #client_ip = websocket.remote_address[0]

    # Gera um ID único para o cliente
    client_id = str(uuid.uuid4())
    #clients.add(client_ip)
    clients[client_id] = websocket
    await websocket.send(f"Seu ID é: {client_id}")
    try:
        async for message in websocket:
            print(f"Received message from {client_id}: {message}")  # Log received message
             # Parse the recipient IP and the actual message
            recipient_ip, message = message.split(' ', 1)
            # Look up the recipient's WebSocket in the connections dictionary
            recipient_websocket = clients.get(recipient_ip)
            print(f"Recipient ID: {clients}")
            print(f"Recipient ID: {recipient_websocket}")
            # If the recipient is connected, forward the message
            if recipient_websocket:
                try:
                    await recipient_websocket.send(message)
                    print(f"Sent message to {recipient_ip}: {message}")  # Log sent message
                except websockets.exceptions.ConnectionClosed:
                    print(f"Connection to {recipient_ip} closed while trying to send message")      
                except Exception as e:
                    print(f"Failed to send message to {recipient_ip}: {e}")
                
            # Encaminha a mensagem recebida para todos os clientes conectados
            #for client in clients.values():
            #    if client != websocket:
            #        await client.send(message)
    finally:
        # Remove o cliente da lista de clientes conectados quando ele se desconectar
        if client_id in clients:
            del clients[client_id]
   

#Função para iniciar o servidor
async def start_server():
    async with websockets.serve(handle_client, "localhost", 8765, ping_timeout=60):
        print("Server iniciado!")
        await asyncio.Future()  # Mantém o servidor rodando indefinidamente

# Inicia o servidor WebSocket e pode ser desligado usando ctrl+c
try:
    asyncio.run(start_server())
except KeyboardInterrupt:
    print("Server interrompido.")
