import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid

class MapPublisher(Node):
    def __init__(self):
        super().__init__('map_publisher')
        self.publisher = self.create_publisher(OccupancyGrid, 'map', 10)
        self.timer = self.create_timer(1.0, self.publish_map)

    def publish_map(self):
        msg = OccupancyGrid()
        msg.header.frame_id = "map"
        msg.info.resolution = 0.1
        msg.info.width = 100
        msg.info.height = 100
        msg.info.origin.position.x = 0.0
        msg.info.origin.position.y = 0.0
        msg.info.origin.position.z = 0.0
        msg.info.origin.orientation.w = 1.0
        msg.data = [0] * (100 * 100)  # Initialize with free space

        # Add obstacles to msg.data as needed
        # For example:
        # msg.data[50*100 + 50] = 100  # Set a cell as occupied

        self.publisher.publish(msg)
        self.get_logger().info('Publishing map')

def main(args=None):
    rclpy.init(args=args)
    node = MapPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
