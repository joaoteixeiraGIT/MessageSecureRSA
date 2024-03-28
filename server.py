import asyncio
import websockets

# Dicionário para ver clientes conectados
clients = set()

async def handle_client(websocket, path):
    # Adiciona o cliente à lista de clientes conectados
    clients.add(websocket)
    try:
        async for message in websocket:
            # Encaminha a mensagem recebida para todos os clientes conectados
            for client in clients:
                if client != websocket:
                    await client.send(message)
    finally:
        # Remove o cliente da lista de clientes conectados quando ele se desconectar
        clients.remove(websocket)

#Função para iniciar o servidor
async def start_server():
    async with websockets.serve(handle_client, "localhost", 8765):
        print("Server iniciado!");
        await asyncio.Future()  # Mantém o servidor rodando indefinidamente

# Inicia o servidor WebSocket e pode ser desligado usando ctrl+c
try:
    asyncio.run(start_server())
except KeyboardInterrupt:
    print("Server interrompido.")
