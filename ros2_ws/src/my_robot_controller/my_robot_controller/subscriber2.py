import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import rosbag2_py
from rclpy.serialization import serialize_message

class subscriberNode(Node):
    def __init__(self):
        super().__init__("My_subscriber2_node")
        self.get_logger().info("Recording has started!")

        self.topic = "/myTopic"

        self.writer = rosbag2_py.SequentialWriter()                         # Initializing bag writer

        storage_options = rosbag2_py._storage.StorageOptions(               # Defining the bag
                                            uri="my_bag",
                                            storage_id='mcap'),
                                            
        converter_options = rosbag2_py._storage.ConverterOptions('', '')

        self.writer.open(storage_options, converter_options)                # Accessing the bag

        topic_info = rosbag2_py._storage.TopicMetadata(                     # Declaring the topics that should be listened
                            name='/myTopic',
                            type='geometry_msgs/msg/Twist',
                            serialization_format='cdr')
        
        self.writer.create_topic(topic_info)

        self.subscriber_ = self.create_subscription(Twist, self.topic, self.printMessage, 10)       # Initializing subscriber object

    def printMessage(self, msg: Twist):
        self.writer.write(                              # Writing inside the bag
            '/myTopic',
            serialize_message(msg),
            self.get_clock().now().nanoseconds)
        
def main(args = None):
    rclpy.init(args = args)

    node = subscriberNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == "__main__":
    main()