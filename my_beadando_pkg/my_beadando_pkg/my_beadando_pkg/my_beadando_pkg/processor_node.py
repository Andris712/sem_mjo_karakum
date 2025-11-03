import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class Processor(Node):
    def __init__(self):
        super().__init__('random_processor')
        self.sub = self.create_subscription(Float32, 'random_value', self._cb, 10)
        self.pub = self.create_publisher(Float32, 'processed_value', 10)
        self.get_logger().info('Processor: /random_value -> /processed_value (x2 + 5)')

    def _cb(self, msg: Float32):
        out = Float32()
        out.data = msg.data * 2.0 + 5.0
        self.pub.publish(out)
        self.get_logger().debug(f'{msg.data:.2f} -> {out.data:.2f}')


def main(args=None):
    rclpy.init(args=args)
    node = Processor()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()
