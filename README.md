# MessageSecureRSA

Este projeto é uma implementação de um sistema de comunicação seguro utilizando WebSocket e criptografia RSA em Python. O sistema permite que os clientes se conectem a um servidor WebSocket central, enviem mensagens criptografadas entre si. Foi desenvolvido no âmbito da UC Criptografia e Segurança de Sistemas Informáticos, no Mestrado em Engenharia Informática na UTAD. <br />

# Funcionalidades Principais:
Conexão WebSocket: O servidor WebSocket é inicializado para permitir conexões de clientes. Os clientes podem enviar e receber mensagens através desta conexão em tempo real. <br />
Criptografia RSA: Utiliza o algoritmo de criptografia RSA para garantir a confidencialidade das mensagens trocadas entre os clientes. Cada mensagem é encriptada com a chave pública do destinatário, garantindo que apenas o destinatário possa desencriptá-la. <br />

# Como Usar:
Configuração do Ambiente de Desenvolvimento: <br />
- Clonar o repositório para o ambiente de desenvolvimento. <br />
- Criar e ativar um ambiente virtual (venv). <br />
- Instalar as dependências do projeto usando: pip install -r requirements.txt <br />

Execução do Projeto: <br />
- Iniciar o servidor WebSocket executando python server.py. <br />
- Executar o cliente WebSocket para conectar ao servidor e trocar mensagens. <br />

# Requisitos do Sistema:
- Python 3.12.2 (versão mais recente) <br />
- Bibliotecas: websockets, cryptography <br />
