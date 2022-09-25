from flask import Flask, request

app = Flask(__name__)
list_of_messages = []


@app.route('/')
def hello():
    return 'Messanger Flask Server is running! ' \
            '<br> <a href="/status">Check status</a>'


@app.route('/status')
def check_status():
    return {
        'messages_count': len(list_of_messages)
    }


@app.route('/api/Messanger', methods=['POST'])
def send_message():
    msg = request.json
    print(msg)
    #
    list_of_messages.append(msg)
    print(msg)
    msg_text = f'{msg["UserName"]} <{msg["TimeStamp"]}>: {msg["MessageText"]}'
    print(f'Всего сообщений: {len(list_of_messages)} Посланное сообщение: {msg_text}')
    return f'Сообщение успешно отправлено. Всего сообщений: {len(list_of_messages)}', 200


@app.route('/api/Messanger/<int:id>')
def get_message(id):
    print(id)
    if id >= 0 and id < len(list_of_messages):
        print(list_of_messages[id])
        return list_of_messages[id], 200
    else:
        return 'Not Found', 400

if __name__ == '__main__':
    app.run()