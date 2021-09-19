SensorFusion Matlab code:
  Requires installation of the MATLAB Navigation toolbox
  
  Question 1: With the way I am currently trying to implement my algorithm, if one measurement is delayed, the position and orientation estimates 
  will not be able to update. I could potentially fix this by having redundant ways of calculating these estimates- if the GPS signal is delayed,
  I could maintain a position estimate using the orientation and speed of the car. If the speedometer gives a late measurement, I could estimate the
  speed using the GPS. If the IMU is delayed, I may be able to estimate the orientation using the last known orientation, speed, and changes in the GPS
  position. 
  
  Question 2: My implementation does not deal with this, because it currently only gets the orientation from the IMU.
  I could fix this by implementing a Kalman filter that would take the GPS readings and speed of the vehicle to get a
  position estimate, and then compare position estimates over time to get an estimate of the orientation of the vehicle
  by calculating the angle between location estimates. 
  
  
  Rules Quiz
  
  Question 1: The most important category in terms of points is "Content" for the business plan.
  Question 2: Egress is considered complete when the driver stands next to the car both feet on the ground.
  Question 3: It depends- you can adjust winglet angles, but not the position of the complete aerodynamic device
              in relation to the vehicle
  Question 4: None of the above
  Question 5: Teams must install the standardised data logger piece of hardware provided by the officials on their vehicle.
  Question 6: Only one-way-telemetry for information retrieval is allowed.
