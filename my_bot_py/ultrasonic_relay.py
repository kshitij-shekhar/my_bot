#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range

class UltrasonicRelay(Node):
    def __init__(self):
        super().__init__('ultrasonic_relay')
        self.sub = self.create_subscription(
            Range,
            '/ultrasonic_front_left/out',
            self.callback,
            10
        )
        self.pub = self.create_publisher(Range, '/ultrasonic_front_left', 10)

    def callback(self, msg):
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = UltrasonicRelay()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
