import rclpy
from rclpy.node import Node

from game_interfaces.srv import PlayerList
from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.player = input("Enter player name:")
        self.checkpoint = '0'
        self.subscription = self.create_subscription(String,'/player/%s/checkpoint' % self.player, self.listener_callback,10)
        self.publisher_ = self.create_publisher(String, '/checkpoint', 10)
        self.srv = self.create_service(PlayerList, '%s_list' % self.player, self.checkpoint_callback) 
        self.subscription  # prevent unused variable warning
	
	
    def checkpoint_callback(self, request, response):
        self.get_logger().info('Incoming request: Land')
        command = "forward %s" % request.player
        print(command)
        response.checkpoint = self.checkpoint
        print(response)
        return response
    
    def listener_callback(self, msg):
        self.get_logger().info('%s:%s' % (self.player,msg))
        if (self.checkpoint == '0' and msg.data == '1'):
            self.checkpoint = '1'
            msgpub1 = String()
            self.publisher_drone = self.create_publisher(String, 'drone/%s' % self.player, 10)
            msgpub1.data = "POWER:0002"
            self.get_logger().info('Publishing: "%s"' % msgpub1.data)
            self.publisher_drone.publish(msgpub1)
        if (self.checkpoint == '1' and msg.data == '2'):
            self.checkpoint = '2'
            msgpub1 = String()
            self.publisher_drone = self.create_publisher(String, 'drone/%s' % self.player, 10)
            msgpub1.data = "POWER:0002"
            self.get_logger().info('Publishing: "%s"' % msgpub1.data)
            self.publisher_drone.publish(msgpub1)
        if (self.checkpoint == '2' and msg.data == '3'):
            self.checkpoint = '3'
            msgpub1 = String()
            self.publisher_drone = self.create_publisher(String, 'drone/%s' % self.player, 10)
            msgpub1.data = "POWER:0002"
            self.get_logger().info('Publishing: "%s"' % msgpub1.data)
            self.publisher_drone.publish(msgpub1)
        
        msgpub = String()
        msgpub.data = '%s:%s' % (self.player,self.checkpoint)
        self.publisher_.publish(msgpub)
        self.get_logger().info('Publishing: "%s"' % msgpub.data)
	

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
