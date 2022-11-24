import rclpy 
from rclpy.node import Node 
from std_msgs.msg import Int16

def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

rclpy.int()
node = Node("listener")
pub = node,create_subscription(Init16,"countup", cb, 10)
rclpy.spin(node)
