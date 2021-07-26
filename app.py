import logging
import os

from dotenv import load_dotenv
from paho.mqtt.client import Client

from actions import on_message

load_dotenv()

BROKER_IP = os.environ.get("BROKER_IP")
BROKER_USERNAME = os.environ.get("BROKER_USERNAME")
BROKER_PASSWORD = os.environ.get("BROKER_PASSWORD")
CLIENT_ID = os.environ.get("CLIENT_ID", "localhost")

LOG_FORMAT = "[%(levelname)s %(asctime)s] : %(message)s"
logging.basicConfig(filename="event.log", level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)

logger.info("Daemon has started.")

# Configure & establish connection to the broker
mqtt_client = Client(CLIENT_ID)
mqtt_client.username_pw_set(BROKER_USERNAME, BROKER_PASSWORD)


def on_connect(client, userdata, flags, rc):
    if rc != 0:
        logger.info("Bad connection. Retrying.")
    mqtt_client.subscribe("#")
    logger.info("Connected & subscribed to #.")


def on_disconnect(client, userdata, rc):
    logger.warning("Disconnected. Retrying.")


mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.on_disconnect = on_disconnect

mqtt_client.connect(BROKER_IP)

try:
    mqtt_client.loop_forever()
except Exception as e:
    logger.error(str(e))
    exit(0)
