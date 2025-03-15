cmake_minimum_required(VERSION 3.5)
project(dingo_control_msg)


find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(builtin_interfaces REQUIRED)

## Generate messages in the 'msg' folder
 rosidl_generate_interfaces(${PROJECT_NAME}
   "msg/TaskSpace.msg"
   "msg/JointSpace.msg"
   "msg/Angle.msg"
   DEPENDENCIES builtin_interfaces std_msgs geometry_msgs
 )

ament_export_dependencies(rosidl_default_runtime)





#############

