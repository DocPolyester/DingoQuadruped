import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/seek/DingoQuadruped_ROS2/dingo_ws/src/install/dingo_utilities'
