#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64
from pynput import keyboard

# TODO: replace Float64 msg to sensor_msgs/JointState
# TODO: Make Add other keyboar handle keys to other joints

class DemoNode():
    def __init__(self):
        self.pub_joint_1 = rospy.Publisher('/rrbot/joint_1/cmd', Float64, queue_size=1)
        # TODO: implement the same idea to other joints as follows
        # self.pub_joint_2 = rospy.Publisher('/rrbot/joint_2/cmd', Float64, queue_size=1)
        # self.pub_joint_3 = rospy.Publisher('/rrbot/joint_3/cmd', Float64, queue_size=1)

        #use same timer callback to handle all publishers
        self.timer = rospy.Timer(rospy.Duration(0.1), self.get_input_CB)
        self.counter = 0

    def demo_callback(self, timer):
        print("entering callback")
        msg = Float64()
        print("Reading the message correctly")
        msg.data = self.counter
        self.counter += 1
        rospy.loginfo("Publishing message {}".format(msg.data))
        self.pub_joint_1.publish(msg)
    def get_input_CB(self, timer):
        with keyboard.Events() as events:
                # TODO: Add exception of 
                event = events.get(0.1)
                if event is None:
                    pass  # print('You did not press a key within one second')
                else:
                    msg = Float64()
                    print('Received Key {}'.format(event.key))
                    try:
                        if event.key.char ==  "v":#keyboard/.#.keyboard.Key.esc:
                            self.counter += 1
                            msg.data = self.counter
                            self.pub_joint_1.publish(msg)
                        elif event.key.char ==  "c":#keyboard/.#.keyboard.Key.esc:
                            self.counter -= 1
                            msg.data = self.counter
                            self.pub_joint_1.publish(msg)
                        else:
                            pass
                    except AttributeError:
                        pass

if __name__ == '__main__':
    rospy.init_node('jointPublisher')
    while not rospy.is_shutdown():
        try:
            DemoNode()
            print("entering Try")
            rospy.spin()
        except rospy.ROSInterruptException:
            print("exception thrown")
            pass