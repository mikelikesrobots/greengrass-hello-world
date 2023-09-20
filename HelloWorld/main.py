import click
import logging
import sys
from src.iot_publisher import IoTPublisher
import src.greeter as greeter
import time


@click.command()
@click.argument("message", type=str, default="World")
@click.option("-p", "--period", type=float, default=1.0)
def main(message, period):
    logging.basicConfig()
    publisher = IoTPublisher()
    while True:
        greeter.print_greeting(message)
        publisher.send_message(message)
        logging.debug("Messages transmitted, sleeping...")
        time.sleep(period)


if __name__ == "__main__":
    main()
