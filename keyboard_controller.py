import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from pynput import keyboard
import pygame
import getpass

class KeyboardController(Node):

    def on_release(self,key):
        msg = String()

        if key == keyboard.Key.up:
            print("Up")
            msg.data = "MOVEF:1000"
            self.publisher.publish(msg)
        if key == keyboard.Key.down:
            print("Down")
            msg.data = "MOVEB:1000"
            self.publisher.publish(msg)
        if key == keyboard.Key.left:
            print("Left")
            msg.data = "MOVEL:1000"
            self.publisher.publish(msg)
        if key == keyboard.Key.right:
            print("Right")
            msg.data = "MOVER:1000"
            self.publisher.publish(msg)
        if key == keyboard.Key.f1:
            print("Up")
            msg.data = "MOVEU:1000"
            self.publisher.publish(msg)
        if key == keyboard.Key.f2:
            print("down")
            msg.data = "MOVED:1000"
            self.publisher.publish(msg)
        if key == keyboard.Key.f3:
            print("takeoff")
            msg.data = "START:0000"
            self.publisher.publish(msg)
        if key == keyboard.Key.f4:
            print("land")
            msg.data = "LANDS:0000"
            self.publisher.publish(msg)
        if key == keyboard.Key.f5:
            print("turn right")
            msg.data = "TURNR:0100"
            self.publisher.publish(msg)
        if key == keyboard.Key.f6:
            print("turn left")
            msg.data = "TURNL:0100"
            self.publisher.publish(msg)
        if key == keyboard.Key.esc:
            return False
        

    def __init__(self):
        super().__init__('KeyboardController')
        self.player = input("Enter player name:")
        self.publisher = self.create_publisher(String, 'drone/%s' % self.player, 10)
        #timer_period = 0.5  # seconds
        #self.timer = self.create_timer(timer_period, self.timer_callback)

        # Collect events until released
        #with keyboard.Listener(
         #   on_release=self.on_release) as listener:
          #      listener.join()
        #listener.start()
        pygame.init()
        finished = False
        isKeyPressed = False
        isForward = False
        isBack = False
        isLeft = False
        isRight = False
        isUp = False
        isDown = False
        isTakeOff = False
        isLand = False
        isTurnRight = False
        isTurnLeft = False
        msg = String()
        screen = pygame.display.set_mode((640, 480))
        clock = pygame.time.Clock()
        while not finished:
            for event in pygame.event.get():
                if isForward:
                    print("front")
                    msg.data = "MOVEF:1000"
                    self.publisher.publish(msg)
                if isBack:
                    print("back")
                    msg.data = "MOVEB:1000"
                    self.publisher.publish(msg)
                if isLeft:
                    print("Left")
                    msg.data = "MOVEL:1000"
                    self.publisher.publish(msg)
                if isRight:
                    print("Right")
                    msg.data = "MOVER:1000"
                    self.publisher.publish(msg)
                if isUp:
                    print("Up")
                    msg.data = "MOVEU:1000"
                    self.publisher.publish(msg)
                if isDown:
                    print("down")
                    msg.data = "MOVED:1000"
                    self.publisher.publish(msg)
                if isTakeOff:
                    print("takeoff")
                    msg.data = "START:0000"
                    self.publisher.publish(msg)
                if isLand:
                    print("land")
                    msg.data = "LANDS:0000"
                    self.publisher.publish(msg)
                if isTurnRight:
                    print("turn right")
                    msg.data = "TURNR:0100"
                    self.publisher.publish(msg)
                if isTurnLeft:
                    print("turn left")
                    msg.data = "TURNL:0100"
                    self.publisher.publish(msg)
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        isForward = True
                    if event.key == pygame.K_s:
                        isBack = True
                    if event.key == pygame.K_d:
                        isTurnRight = True
                    if event.key == pygame.K_a:
                        isTurnLeft = True
                    if event.key == pygame.K_q:
                        isLeft = True
                    if event.key == pygame.K_e:
                        isRight = True
                    if event.key == pygame.K_x:
                        isLand = True
                    if event.key == pygame.K_c:
                        isTakeOff = True
                    if event.key == pygame.K_r:
                        isUp = True
                    if event.key == pygame.K_f:
                        isDown = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        isForward = False
                    if event.key == pygame.K_s:
                        isBack = False
                    if event.key == pygame.K_d:
                        isTurnRight = False
                    if event.key == pygame.K_a:
                        isTurnLeft = False
                    if event.key == pygame.K_q:
                        isLeft = False
                    if event.key == pygame.K_e:
                        isRight = False
                    if event.key == pygame.K_x:
                        isLand = False
                    if event.key == pygame.K_c:
                        isTakeOff = False
                    if event.key == pygame.K_r:
                        isUp = False
                    if event.key == pygame.K_f:
                        isDown = False
                pygame.display.flip()
                clock.tick(60)
        pygame.quit()




def main(args=None):
    
    
    rclpy.init(args=args)

    controller = KeyboardController()
    rclpy.spin(controller)

    controller.destroy_node()
    rclpy.shutdown()
    
    

if __name__ == '__main__':
    main() 
