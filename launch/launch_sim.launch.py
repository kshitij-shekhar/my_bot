


import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription,TimerAction
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node


def generate_launch_description():
    package_name = 'my_bot'  # Replace with your actual package name

    # Robot State Publisher launch (loads your URDF/Xacro)
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(package_name), 'launch', 'rsp.launch.py')
        ]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Gazebo (default world with ground plane)
    gazebo = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([
        os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
    ]),
    launch_arguments={'world': os.path.join(get_package_share_directory(package_name), 'worlds', 'empty.world')}.items()
)


    static_transform_publisher = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_tf_pub_map_odom',
        arguments=['0', '0', '0', '0', '0', '0', 'map', 'odom'],
        output='screen'
    )


    # Spawn robot on the ground plane
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'my_bot',
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.1'  # Just above ground plane
        ],
        output='screen'
    )


    nav2 = TimerAction(
        period=8.0,  # ⏱️ Wait 8 seconds before launching Nav2
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([
                    os.path.join(get_package_share_directory(package_name), 'launch', 'nav2.launch.py')
                ])
            )
        ]
    )






    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        static_transform_publisher,
        nav2
    ])

