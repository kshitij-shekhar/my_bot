import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SpawnModel, SetModelState
from geometry_msgs.msg import Pose
import time

class ObstacleMover(Node):
    def __init__(self):
        super().__init__('obstacle_mover')
        self.spawn_srv = self.create_client(SpawnModel, 'spawn_entity')
        self.set_state_srv = self.create_client(SetModelState, 'set_entity_state')
        self.timer = self.create_timer(5.0, self.move_obstacle)

    def move_obstacle(self):
        # Define obstacle model and initial pose
        model_name = "obstacle"
        model_xml = '<sdf version="1.6"><model name="obstacle"><pose>0 0 0 0 0 0</pose><link name="link"><visual name="visual"><geometry><box><size>1 1 1</size></box></geometry></visual></link></model></sdf>'
        initial_pose = Pose()
        initial_pose.position.x = 0.0  # Assign float value
        initial_pose.position.y = 0.0  # Assign float value
        initial_pose.position.z = 0.0  # Assign float value

        # Spawn obstacle if not already spawned
        if not self.spawn_srv.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Spawn service not available')
            return

        req = SpawnModel.Request()
        req.model_name = model_name
        req.model_xml = model_xml
        req.initial_pose = initial_pose
        req.reference_frame = "world"
        self.spawn_srv.call_async(req)

        # Move obstacle to new position
        new_pose = Pose()
        new_pose.position.x = 1.0  # Assign float value
        new_pose.position.y = 1.0  # Assign float value
        new_pose.position.z = 0.0  # Assign float value

        if not self.set_state_srv.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Set state service not available')
            return

        req = SetModelState.Request()
        req.model_state.model_name = model_name
        req.model_state.pose = new_pose
        self.set_state_srv.call_async(req)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleMover()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
