robot = importrobot('../model/Lewansoul xArm.urdf');

ik = inverseKinematics('RigidBodyTree', robot);
homeConfig = homeConfiguration(robot);
endEffector = 'Gripper';

taskInit = getTransform(robot, homeConfig, endEffector);

if exist('serial', 'var')
  delete(serial);
end

serial = serialport("COM3", 115200);
