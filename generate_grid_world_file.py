tile_size = 0.3
rows, cols = 10, 10
obstacle_positions = [(0, 1), (2, 2), (4, 3), (7, 8), (5, 1), (8, 4)]  # one next to start at (0, 1)

for i in range(rows):
    for j in range(cols):
        model_name = f"tile_{i}_{j}"
        link_name = f"link_{i}_{j}"
        visual_name = f"visual_{i}_{j}"
        collision_name = f"collision_{i}_{j}"
        x = i * tile_size
        y = j * tile_size

        color = "0.7 0.7 0.7 1"
        if (i, j) == (0, 0):
            color = "0.2 0.2 1 1"  # Start tile blue

        print(f'''
    <model name="{model_name}">
      <static>true</static>
      <link name="{link_name}">
        <pose>{x} {y} 0.05 0 0 0</pose>
        <collision name="{collision_name}">
          <geometry>
            <box><size>{tile_size} {tile_size} 0.1</size></box>
          </geometry>
        </collision>
        <visual name="{visual_name}">
          <geometry>
            <box><size>{tile_size} {tile_size} 0.1</size></box>
          </geometry>
          <material>
            <ambient>{color}</ambient>
          </material>
        </visual>
      </link>
    </model>''')

# Obstacles
for idx, (i, j) in enumerate(obstacle_positions):
    x = i * tile_size + tile_size / 2
    y = j * tile_size + tile_size / 2
    print(f'''
    <model name="obstacle_{idx}">
      <static>true</static>
      <link name="obstacle_link_{idx}">
        <pose>{x} {y} 0.25 0 0 0</pose>
        <collision name="obstacle_collision_{idx}">
          <geometry>
            <box><size>0.2 0.2 0.5</size></box>
          </geometry>
        </collision>
        <visual name="obstacle_visual_{idx}">
          <geometry>
            <box><size>0.2 0.2 0.5</size></box>
          </geometry>
          <material>
            <ambient>1 0 0 1</ambient>
          </material>
        </visual>
      </link>
    </model>''')
