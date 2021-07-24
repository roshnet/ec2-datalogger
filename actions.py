import json

from models import Reading


def on_connect(self, client, userdata, message):
    """Callback when connected to the broker."""
    pass


def on_message(client, userdata, message):
    """Callback when message is received on any topic."""
    insert_payload(json.loads(message.payload.decode("utf-8")))


def insert_payload(payload):
    """Parse readings from MQTT payload and store in database."""

    device_id = payload["deviceId"]
    sensors = payload["data"]

    for sensor in sensors:
        sensor_id = f"{device_id}-{sensor['sensorId']}"
        Reading.create(
            sensor_id=sensor_id, sensor_type=sensor["type"], value=sensor["value"]
        )
