%Outline: -use IMU acc and gyro readings to get an orientation estimate
%         -use GPS to get location estimate
%         - use speedometer to help correct with GPS estimate (GPS gives
%         groundspeed)


load('data.mat') %, 'GNSS', 'SPEEDOMETER', 'IMU')

%IMU Data- orientation estimate

accReadings = in_data.IMU.acc';
gyroReadings = in_data.IMU.gyro';

%imufilter uses Kalman Filter to track the errors in orientation, gyroscope offset, 
%and linear acceleration to output the final orientation and angular velocity.

fuse = imufilter('SampleRate', 100); 

q = fuse(accReadings, gyroReadings); 
euler = eulerd(q,'ZYX','frame');

%Orientation plot
% time = (0:1:size(accReadings,1)-1)/100;
% plot(time,euler);
% title('Orientation Estimate')
% legend('Z-axis', 'Y-axis', 'X-axis')
% xlabel('Time (s)')
% ylabel('Rotation (degrees)')


%There is probably (defintely) a better way to calculate velocity
% with the given data. Right now, it is found by integrating the IMU
% accerlation
velocity_imu = cumtrapz(in_data.IMU.t, accReadings) ;

%scale IMU data to match time scale of GPS data
scale_vel = velocity_imu(1:100:length(in_data.IMU.t),:);
gps_data = in_data.GNSS.pos_ned';
GPS = gpsSensor;

%GPS model gives position, velocity in local coordinate system,
%magnitude of horizontal velocity in local system, direction of horizontal
%vel in given coordinate system
[position, velocity, groundspeed, course] = GPS(gps_data, scale_vel);

%Position plot
% time = in_data.GNSS.t;
% plot(time,position);
% title('Position Estimate')
% xlabel('Time (s)')
% ylabel('Coordinates')

%Can compare calculated GPS groundspeed to the data from the speedometer
% I believe this can be done with a Kalman filter, but I am not sure how
% that interfaces with the way that MATLAB calculates the groudspeed in the
% GPS model



