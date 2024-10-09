import pika
from pika.adapters.blocking_connection import BlockingChannel
from typing import Optional, Iterator
from contextlib import contextmanager
from app.core.settings import settings


class RabbitMQManager:
    def __init__(self) -> None:
        """Initializes the manager with no connection or credentials."""
        self.rabbit_credentials: Optional[pika.PlainCredentials] = None
        self.rabbit_connection: Optional[pika.BlockingConnection] = None

    def init(self, host: str = settings.RABBIT_URL,
             username: str = settings.RABBITMQ_USER,
             password: str = settings.RABBITMQ_PASS) -> None:
        """
        Initializes the RabbitMQ connection if not already connected.
        
        Args:
            host (str): RabbitMQ host URL.
            username (str): RabbitMQ username.
            password (str): RabbitMQ password.
        """
        credentials = pika.PlainCredentials(username, password)
        if not self.rabbit_connection or self.rabbit_connection.is_closed:
            self.rabbit_connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=host, credentials=credentials, heartbeat=30)
            )
            print("RabbitMQ connection established.")

    def close_connection(self) -> None:
        """Closes the RabbitMQ connection if it is open."""
        if self.rabbit_connection and not self.rabbit_connection.is_closed:
            self.rabbit_connection.close()
            self.rabbit_connection = None
            print("RabbitMQ connection closed.")

    @contextmanager
    def get_rabbitmq_channel(self) -> Iterator[BlockingChannel]:
        """
        Context manager that yields a RabbitMQ channel, ensuring the connection is open.
        If the connection is closed, it is reopened.
        """
        if not self.rabbit_connection or self.rabbit_connection.is_closed:
            print("Inactive connection. Reopening...")
            self.init()

        channel = self.rabbit_connection.channel() # type: ignore
        try:
            yield channel
        finally:
            channel.close()


    # async def publish_message(self, object_name: str, queue_message: QueueMessage):
    #     try:
    #         self.rabbit_channel.basic_publish(
    #             exchange=settings.UPLOAD_EXCHANGE,
    #             routing_key=settings.UPLOAD_ROUTING_KEY,
    #             body=queue_message.model_dump_json(),
    #             properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE),
    #         )
    #     except Exception as _:
    #         await self.remove_video_file(object_name)
    #         raise BadRequestError(detail="Error while trying to convert the file")



rabbit_manager = RabbitMQManager()

def get_rabbit_channel() -> Iterator[BlockingChannel]:
    """Provides a channel using the RabbitMQManager's context manager."""
    with rabbit_manager.get_rabbitmq_channel() as channel:
        yield channel
