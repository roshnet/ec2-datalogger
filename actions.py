import json


def on_connect(self, client, userdata, message):
    """Callback when client is connected to the broker."""
    pass


def on_message(client, userdata, message):
    """Callback when message is received on any topic."""
    _ = json.loads(message.payload.decode("utf-8"))
    pass
