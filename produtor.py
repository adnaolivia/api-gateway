import pika

def publicar_mensagem(mensagem):
    conexao = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    canal = conexao.channel()

    canal.queue_declare(queue='minha_fila') # fila

    # Publicar a mensagem
    canal.basic_publish(exchange='', routing_key='minha_fila', body=mensagem)
    print(f"Mensagem publicada: {mensagem}")
    conexao.close()

publicar_mensagem('teste')
