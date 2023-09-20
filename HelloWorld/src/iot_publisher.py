import awsiot.greengrasscoreipc
import awsiot.greengrasscoreipc.model as model
import json
import logging

TOPIC = "test/topic"


class IoTPublisher:
    def __init__(self):
        self.logger = logging.getLogger("IoTPublisher")
        self.logger.info("Connecting to Greengrass Core")
        self.ipc_client = awsiot.greengrasscoreipc.connect()
        self.logger.info("Connection complete!")

    def send_message(self, message: str):
        payload = {"greeting": "Hello", "subject": message}
        op = self.ipc_client.new_publish_to_iot_core()
        op.activate(model.PublishToIoTCoreRequest(
            topic_name=TOPIC,
            qos=model.QOS.AT_LEAST_ONCE,
            payload=json.dumps(payload).encode(),
        ))

        try:
            result = op.get_response().result(timeout=5.0)
            self.logger.info("successfully published message:", result)
        except Exception as e:
            self.logger.error("failed to publish message:", e)
