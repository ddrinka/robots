function [previousControlState, adjustedAny] = setServoPositions(serialPort, controlState, epsilon, previousControlState)
%SETSERVOPOSITIONS Set xArm to provided control state

if length(controlState) ~= 6
  throw(MException('xArm:argumentError', 'Incorrect number of state variables'));
end

isFirstRun = isempty(previousControlState);

controlState(4) = -controlState(4);     % Servo 3 is reversed

adjustedAny = false;
for i = 1:6
  if isFirstRun || abs(previousControlState(i) - controlState(i)) > epsilon
      adjustedAny = true;
      setServoPosition(serialPort, 7-i, controlState(i), .1);
      previousControlState(i) = controlState(i);
  end
end

end

