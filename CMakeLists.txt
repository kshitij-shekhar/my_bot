cmake_minimum_required(VERSION 3.5)
project(my_bot)

# Install launch files
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/
)

# Install config files (optional but recommended)
install(DIRECTORY config
  DESTINATION share/${PROJECT_NAME}/
)

# Install map files
install(DIRECTORY map
  DESTINATION share/${PROJECT_NAME}/
)

# Install worlds (if needed for simulation)
install(DIRECTORY worlds
  DESTINATION share/${PROJECT_NAME}/
)
