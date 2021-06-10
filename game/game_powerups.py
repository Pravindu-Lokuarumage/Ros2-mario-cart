import rclpy
from rclpy.node import Node

from gazebo_msgs.msg import ModelStates
from gazebo_msgs.srv import DeleteEntity

from std_msgs.msg import String
import time


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.player = input("Enter player name:")
        self.get_logger().info('Creating Service client to connect to `/delete_entity`')
        self.client = self.create_client(DeleteEntity, "/delete_entity")
        
        self.get_logger().info("Connecting to `/delete_entity` service...")
        if not self.client.service_is_ready():
            self.client.wait_for_service()
        self.get_logger().info("...connected!")
                
        
        self.checkpoint = '0'
        self.subscription = self.create_subscription(ModelStates,'/world/model_states', self.listener_callback,10)
        self.subscription  # prevent unused variable warning
	
	
    def listener_callback(self, msg):
        models = { msg.name[i] : i for i in range(0, len(msg.name) ) }
        print (models)
        self.publisher = self.create_publisher(String, '/player/%s/checkpoint' % self.player, 10)
        self.publisher_drone = self.create_publisher(String, 'drone/%s' % self.player, 10)
        msg1 = String()
        msg2 = String()
        msg1.data = "0" 
        msg2.data = "0" 
        self.get_logger().info('%s:%s' % (self.player,msg.pose[models["checkpoint1"]].position.x))
        
        try:
            print(models["%s" % self.player])
        except KeyError:
            print("error")  
        try:
            print(models["checkpoint1"])
            if (msg.pose[models["%s" % self.player]].position.x - 0.5 < msg.pose[models["checkpoint1"]].position.x and msg.pose[models["%s" % self.player]].position.x + 0.5 > msg.pose[models["checkpoint1"]].position.x and msg.pose[models["%s" % self.player]].position.y - 0.8 < msg.pose[models["checkpoint1"]].position.y and msg.pose[models["%s" % self.player]].position.y + 0.8 > msg.pose[models["checkpoint1"]].position.y):
                print("1")
                msg1.data = "1" 
        except KeyError:
            print("error") 
        try:
            print(models["checkpoint2"])
            if (msg.pose[models["%s" % self.player]].position.x - 0.8 < msg.pose[models["checkpoint2"]].position.x and msg.pose[models["%s" % self.player]].position.x + 0.8 > msg.pose[models["checkpoint2"]].position.x and msg.pose[models["%s" % self.player]].position.y - 0.5 < msg.pose[models["checkpoint2"]].position.y and msg.pose[models["%s" % self.player]].position.y + 0.5 > msg.pose[models["checkpoint2"]].position.y):
                print("2")
                msg1.data = "2"
        except KeyError:
            print("error") 
        try:
            print(models["checkpoint3"])
            if (msg.pose[models["%s" % self.player]].position.x - 0.8 < msg.pose[models["checkpoint3"]].position.x and msg.pose[models["%s" % self.player]].position.x + 0.8 > msg.pose[models["checkpoint3"]].position.x and msg.pose[models["%s" % self.player]].position.y - 0.5 < msg.pose[models["checkpoint3"]].position.y and msg.pose[models["%s" % self.player]].position.y + 0.5 > msg.pose[models["checkpoint3"]].position.y):
                print("3")
                msg1.data = "3"
        except KeyError:
            print("error") 
        try:
            print(models["power1"])
            if (msg.pose[models["%s" % self.player]].position.x - 0.6 < msg.pose[models["power1"]].position.x and msg.pose[models["%s" % self.player]].position.x + 0.6 > msg.pose[models["power1"]].position.x and msg.pose[models["%s" % self.player]].position.y - 0.6 < msg.pose[models["power1"]].position.y and msg.pose[models["%s" % self.player]].position.y + 0.6 > msg.pose[models["power1"]].position.y and msg.pose[models["%s" % self.player]].position.z - 0.6 < msg.pose[models["power1"]].position.z and msg.pose[models["%s" % self.player]].position.z + 0.6 > msg.pose[models["power1"]].position.z):
                print("p1")
                
                
                request = DeleteEntity.Request()
                request.name = 'power1'

                self.get_logger().info("Sending service request to `/spawn_entity`")
                future = self.client.call_async(request)
                print("ok")
                msg2.data = "POWER:0004"  
                
        except KeyError:
            print("error") 
        try:
            print(models["power2"])
            if (msg.pose[models["%s" % self.player]].position.x - 0.6 < msg.pose[models["power2"]].position.x and msg.pose[models["%s" % self.player]].position.x + 0.6 > msg.pose[models["power2"]].position.x and msg.pose[models["%s" % self.player]].position.y - 0.6 < msg.pose[models["power2"]].position.y and msg.pose[models["%s" % self.player]].position.y + 0.6 > msg.pose[models["power2"]].position.y and msg.pose[models["%s" % self.player]].position.z - 0.6 < msg.pose[models["power2"]].position.z and msg.pose[models["%s" % self.player]].position.z + 0.6 > msg.pose[models["power2"]].position.z):
                print("p2")
                
                
                request = DeleteEntity.Request()
                request.name = 'power2'

                self.get_logger().info("Sending service request to `/spawn_entity`")
                future = self.client.call_async(request)
                print("ok")
                
                msg2.data = "POWER:0004"  
        except KeyError:
            print("error") 
        try:
            print(models["power3"])
            if (msg.pose[models["%s" % self.player]].position.x - 0.6 < msg.pose[models["power3"]].position.x and msg.pose[models["%s" % self.player]].position.x + 0.6 > msg.pose[models["power3"]].position.x and msg.pose[models["%s" % self.player]].position.y - 0.6 < msg.pose[models["power3"]].position.y and msg.pose[models["%s" % self.player]].position.y + 0.6 > msg.pose[models["power3"]].position.y and msg.pose[models["%s" % self.player]].position.z - 0.6 < msg.pose[models["power3"]].position.z and msg.pose[models["%s" % self.player]].position.z + 0.6 > msg.pose[models["power3"]].position.z):
                print("p3")
               
                
                request = DeleteEntity.Request()
                request.name = 'power3'

                self.get_logger().info("Sending service request to `/spawn_entity`")
                future = self.client.call_async(request)
                print("ok")
                    
                msg2.data = "POWER:0004"  
        except KeyError:
            print("error")     
          
        
        self.publisher.publish(msg1)
        if (msg2.data != '0'):
            self.publisher_drone.publish(msg2)
            print("pub to mult")
        
        
	

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
