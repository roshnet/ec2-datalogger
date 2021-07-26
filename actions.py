import json
import logging

from models import Reading

logger = logging.getLogger(__name__)


def on_message(client, userdata, message):
    """Callback when message is received on any topic."""
    try:
        insert_payload(json.loads(message.payload.decode("utf-8")))
    except Exception as e:
        logger.warning("Payload structure has possibly changed.")
        logger.error(str(e))


def insert_payload(payload):
    """Parse readings from MQTT payload and store in database."""

    device_id = payload["deviceId"]
    sensors = payload["data"]

    for sensor in sensors:
        sensor_id = f"{device_id}-{sensor['sensorId']}"
        Reading.create(
            sensor_id=sensor_id, sensor_type=sensor["type"], value=sensor["value"]
        )
