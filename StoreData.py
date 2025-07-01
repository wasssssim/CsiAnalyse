import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)
with open("csi_data_log.txt", "w") as f:
    while True:
        line = ser.readline().decode(errors='ignore').strip()
        print(line)
        f.write(line + "\n")
