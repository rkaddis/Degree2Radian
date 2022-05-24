# Degree2Radian

Program to convert degrees to radians

  launch/deg2rad_py.launch -> launches program, sets default angle value to 90.5 degrees

  scripts/get_deg.py -> Python file to receive degree data from parameter server and to publish it at 0.2Hz
  
  scripts/deg2rad.py -> Python file to receive angle data from get_deg through /angle, converts to radians and prints to the screen
  
  
