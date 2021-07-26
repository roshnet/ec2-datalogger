import os

from dotenv import load_dotenv
from paho.mqtt.client import Client

from actions import on_message

load_dotenv()

BROKER_IP = os.environ.get("BROKER_IP")
BROKER_USERNAME = os.environ.get("BROKER_USERNAME")
BROKER_PASSWORD = os.environ.get("BROKER_PASSWORD")

# Configure & establish connection to the broker
mqtt_client = Client("Default Sensor")
mqtt_client.username_pw_set(BROKER_USERNAME, BROKER_PASSWORD)


def on_connect(self, client, userdata, message):
    mqtt_client.subscribe("#")


mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(BROKER_IP)

try:
    mqtt_client.loop_forever()
except Exception as e:
    exit(0)
