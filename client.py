import asyncio
import websockets

# Função para lidar com mensagens recebidas do servidor
async def handle_messages(websocket):
    # Esta função é executada em um loop infinito, aguardando mensagens do servidor
    async for message in websocket:
        # Imprime a mensagem recebida do servidor
        print(message)

# Função para enviar mensagens para o servidor
async def send_messages(websocket):
    # Este loop é executado indefinidamente até que o usuário digite 'exit' para sair
    while True:
        # Solicita ao usuário que digite uma mensagem para enviar ao servidor
        message = input("Digite a mensagem para enviar (ou 'exit' para sair): ")
        # Se o usuário digitar 'exit', quebra o loop e sai da função
        if message == 'exit':
            await websocket.close()  # Fecha a conexão com o servidor WebSocket
            print("Conexão encerrada.")
            break  # Sai do loop
        # Envia a mensagem para o servidor
        await websocket.send(message)

# Função para conectar ao servidor WebSocket
async def connect_to_server():
    # URI do servidor WebSocket ao qual vamos nos conectar
    uri = "ws://localhost:8765"  # Endereço do servidor WebSocket
    # Conecta-se ao servidor WebSocket
    async with websockets.connect(uri) as websocket:
        # Imprime uma mensagem indicando que o cliente está conectado ao servidor
        print("Conectado ao servidor.")
        
        # Inicia duas tarefas assíncronas para lidar com mensagens recebidas e enviadas
        await asyncio.gather(handle_messages(websocket), send_messages(websocket))

# Inicia o cliente WebSocket
asyncio.run(connect_to_server())
