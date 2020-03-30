function setServoPosition(serialPort, servoId, angle, travelTime)
%SETSERVOPOSITION Set the absolute position of a servo

commandId = 1;
commandLength = 7;
angleBytes = uint16(angle*180/pi()*4+512);
travelTimeBytes = uint16(travelTime * 1000);

command = [servoId, commandLength, commandId, mod(angleBytes, 256), bitshift(angleBytes, -8), mod(travelTimeBytes, 256), bitshift(travelTimeBytes, -8)];

checksum = 0;
for byte = command
    checksum = checksum+byte;
end
checksum = 255 - mod(checksum, 256);

toWrite = [0x55, 0x55, command, checksum];

write(serialPort, toWrite, "uint8");
flush(serialPort, "output");

end