robot = importrobot('../model/Lewansoul xArm.urdf');

ik = interactiveRigidBodyTree(robot);

if exist('serial', 'var')
  delete(serial);
end

serial = serialport("COM3", 115200);

previousControlState = zeros(0);
while true
    controlState = ik.Configuration;
    controlState(6) = 0;

    [previousControlState, adjustedAny] = setServoPositions(serial, controlState, 0, previousControlState);
    if ~adjustedAny
        pause(.1);
    else
        fprintf('%.2f %.2f %.2f %.2f %.2f %.2f\n', controlState.');
    end

end