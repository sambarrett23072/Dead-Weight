def handle_response(message):
    p_message = message.lower()
    if p_message == '$hello':
        return 'Hey there!'