import pika

def callback(ch, method, properties, body):
    print(f"Mensagem recebida: {body}")

def consumir_mensagens():
    conexao = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    canal = conexao.channel()

    canal.queue_declare(queue='minha_fila') # chamada da fila criada no produtor

    # consumo das mensagens
    canal.basic_consume(queue='minha_fila', on_message_callback=callback, auto_ack=True)

    print('Aguardando mensagens... Pressione Ctrl+C para sair.')
    canal.start_consuming()

# Exemplo de uso
consumir_mensagens()
