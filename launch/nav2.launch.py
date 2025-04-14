


import os
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    bringup_dir = get_package_share_directory('nav2_bringup')
    my_bot_dir = get_package_share_directory('my_bot')

    map_file = os.path.join(my_bot_dir, 'map', 'grid_map.yaml')
    nav2_params = os.path.join(my_bot_dir, 'config', 'nav2_params.yaml')  # Adjust path if needed

    amcl_node = Node(
        package='nav2_amcl',
        executable='amcl',
        name='amcl',
        output='screen',
        parameters=[{
            'use_sim_time': True,
            'yaml_filename': nav2_params
        }]
    )

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(bringup_dir, 'launch', 'bringup_launch.py')
            ),
            launch_arguments={
                'map': map_file,
                'use_sim_time': 'true',
                'params_file': nav2_params
            }.items()
        ),
        amcl_node  # <-- This is what was missing
    ])

