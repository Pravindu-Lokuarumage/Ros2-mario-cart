#import os
#import sys
import rclpy
from rclpy.node import Node
#from ament_index_python.packages import get_package_share_directory
from gazebo_msgs.srv import SpawnEntity
from gazebo_msgs.srv import DeleteEntity
from gazebo_msgs.srv import SetEntityState
from gazebo_msgs.msg import EntityState
import time
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from game_interfaces.srv import PlayerList
from std_msgs.msg import String


import math

class RobotVisualiser(Node):


    def listener_callback(self, msg):
        
        self.get_logger().info('Getting: "%s"' % msg.data)
	
    
    def __init__(self):
        super().__init__('robot_visualiser')
        
        topic_list = self.get_topic_names_and_types()
        print(topic_list)

        #first spawn
        self.get_logger().info(
            'Creating Service client to connect to `/spawn_entity`')
        client = self.create_client(SpawnEntity, "/spawn_entity")
        
        self.get_logger().info("Connecting to `/spawn_entity` service...")
        if not client.service_is_ready():
            client.wait_for_service()
            self.get_logger().info("...connected!")
        
        # Set data for request
        request = SpawnEntity.Request()
        request.name = 'checkpoint1'
        request.xml = "<?xml version='1.0'?><sdf version='1.4'><model name='my_check1'><pose>3 0 0 0 0 0</pose><static>true</static><link name='link1'><collision name='collisionc1'><geometry><box><size>0.05 1 0.05</size></box></geometry></collision><visual name='visualc1'><geometry><box><size>0.05 1 0.05</size></box></geometry></visual></link></model></sdf>"        
        request.robot_namespace = "demo"

        self.get_logger().info("Sending service request to `/spawn_entity`")
        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            print('response: %r' % future.result())
        else:
            raise RuntimeError(
                'exception while calling service: %r' % future.exception())
                
        
        # Set data for request
        request = SpawnEntity.Request()
        request.name = 'checkpoint2'
        request.xml = "<?xml version='1.0'?><sdf version='1.4'><model name='my_check2'><pose>6 4 0 0 0 0</pose><static>true</static><link name='link2'><collision name='collisionc2'><geometry><box><size>1 0.05 0.05</size></box></geometry></collision><visual name='visualc2'><geometry><box><size>1 0.05 0.05</size></box></geometry></visual></link></model></sdf>"        
        request.robot_namespace = "demo"

        self.get_logger().info("Sending service request to `/spawn_entity`")
        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            print('response: %r' % future.result())
        else:
            raise RuntimeError(
                'exception while calling service: %r' % future.exception())
                
        # Set data for request
        request = SpawnEntity.Request()
        request.name = 'checkpoint3'
        request.xml = "<?xml version='1.0'?><sdf version='1.4'><model name='my_check3'><pose>1 10 0 0 0 0</pose><static>true</static><link name='link2'><collision name='collisionc2'><geometry><box><size>0.05 1 0.05</size></box></geometry></collision><visual name='visualc2'><geometry><box><size>1 0.05 0.05</size></box></geometry></visual></link></model></sdf>"        
        request.robot_namespace = "demo"

        self.get_logger().info("Sending service request to `/spawn_entity`")
        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            print('response: %r' % future.result())
        else:
            raise RuntimeError(
                'exception while calling service: %r' % future.exception())
        
        # Set data for request
        request = SpawnEntity.Request()
        request.name = 'power1'
        request.xml = "<?xml version='1.0'?><sdf version='1.4'><model name='power1'><pose>1 2 2 0 0 0</pose><static>true</static><link name='link2'><collision name='collisionc2'><geometry><sphere><radius>0.2</radius></sphere></geometry></collision><visual name='visualc2'><geometry><sphere><radius>0.2</radius></sphere></geometry></visual></link></model></sdf>"        
        request.robot_namespace = "demo"

        self.get_logger().info("Sending service request to `/spawn_entity`")
        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            print('response: %r' % future.result())
        else:
            raise RuntimeError(
                'exception while calling service: %r' % future.exception())
                                   
        # Set data for request
        request = SpawnEntity.Request()
        request.name = 'power2'
        request.xml = "<?xml version='1.0'?><sdf version='1.4'><model name='power2'><pose>7 1 3 0 0 0</pose><static>true</static><link name='link2'><collision name='collisionc2'><geometry><sphere><radius>0.2</radius></sphere></geometry></collision><visual name='visualc2'><geometry><sphere><radius>0.2</radius></sphere></geometry></visual></link></model></sdf>"        
        request.robot_namespace = "demo"

        self.get_logger().info("Sending service request to `/spawn_entity`")
        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            print('response: %r' % future.result())
        else:
            raise RuntimeError(
                'exception while calling service: %r' % future.exception())
                
        # Set data for request
        request = SpawnEntity.Request()
        request.name = 'power3'
        request.xml = "<?xml version='1.0'?><sdf version='1.4'><model name='power3'><pose>7 10 1 0 0 0</pose><static>true</static><link name='link2'><collision name='collisionc2'><geometry><sphere><radius>0.2</radius></sphere></geometry></collision><visual name='visualc2'><geometry><sphere><radius>0.2</radius></sphere></geometry></visual></link></model></sdf>"        
        request.robot_namespace = "demo"

        self.get_logger().info("Sending service request to `/spawn_entity`")
        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            print('response: %r' % future.result())
        else:
            raise RuntimeError(
                'exception while calling service: %r' % future.exception())
                
        self.subscription = self.create_subscription(String,'/checkpoint', self.listener_callback,10)
        self.subscription 
        for topic in topic_list:
            print(topic[0][:7])
            if topic[0][:1] == '/player': 
                self.subtopic = topic[0]
                print(self.subtopic)
        

def main(args=None):
    rclpy.init(args=args)

    visualiser = RobotVisualiser()
    rclpy.spin(visualiser)
    
    visualiser.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
