"""
Library for reading the 24GHz mmWave Sensor - Human Static Presence Module Lite (MR24HPC1) by Seeed.

Created by Heiko Ritter (09.10.2024)

Version Info:
            0.1 basic functionality - reading raw Sensor data. (09.10.2024 - 23:23:00)
            0.1.1 added: data protocoll constants

It should be able to read (TODO: and write) the raw Sensor-Data of the MR24HPC and will be the supporting
base for additional libraries to other mmWave Radars with serial communication via UART.

if you have questions or suggestions, just send me a e-mail to oldboones@github.com or heiko.ritter@gmail.com

================= CONNECTION INFO =================

The MR24HPC1 by Seeed is using a fixed baudrate of 115200
Connection Info according to User Manual:
baudrate: 9600 (TODO: Why is UserManual saying a different baudrate?)
stopbit: 1
databits: 8
parity: None

(circuitpython) busio.UART connection command is:
    
    uart = busio.UART(board.A2, board.A1,cts=None, rts=None, baudrate=115200, stop=1, timeout=0.5)

!!INFO!!: you need to change the PINs according to your board.
!!INFO!!: setting cts, rts, baudrate and stop is necessary, timeout is optional but recommended

Most Boards should have hardware RX/TX Ports but you can also use many other GPIO for soft-serial.
check the wiring, connection-command and/or datasheet of your board if connection(initialization of class) is failing.
Not every GPIO PIN is able to work as serial.

REMEMBER: The Sensors receiving-port goes to your MCU(or Computers) sending-port and other way around

For Reading/Writing serial Data, wire your hardware as following

    sensor.RX <--> board.TX (or any other soft-serial capable pin/io)
    sensor.TX <--> board.RX (or any other soft-serial capable pin/io)
    5V <--> 5V
    GND <--> GND
    
for pin-trigger information you can use the 2 extra-pins (TODO: Write Functions and Doc for those 2 additionals)
#  P1 True=occupied, False=unoccupied
#  P2 True=active, False=stationary
================= CONNECTION INFO =================
            
"""

import busio

#  ====== GLOBAL VARS AND CONSTANTS ====== #  copied from the seeed library for Arduino
MESSAGE_HEAD1 = 0x53  #  Data frame header1
MESSAGE_HEAD2 = 0x59  #  Data frame header2

MESSAGE_END1 = 0x54  #  End1 of data frame
MESSAGE_END2 = 0x43  #  End2 of data frame
HUMANSTATUS = 0x80  #  Human Presence Information
HUMANEXIST = 0x01  #  Presence of the human body
MANMOVE = 0x02  #  Human movement information
HUMANSIGN = 0x03  #  Body Signs Parameters
HUMANDIRECT = 0x0B  #  Human movement trends

SOMEBODY = 0x01  #  Somebody move
NOBODY = 0x00  #  No one here

NONE = 0x00  #  Empty Data
SOMEBODY_STOP = 0x01  #  Somebody stop
SOMEBODY_MOVE = 0x02  #  Somebody move

CA_CLOSE = 0x01  #  Someone approaches
CA_AWAY = 0x02  #  Some people stay away

DETAILSTATUS = 0x08  #  Underlying parameters of the human state
DETAILINFO = 0x01  #  Detailed data on the state of human movement
DETAILDIRECT = 0x06  #  Human movement trends
DETAILSIGN = 0x07  #  Body Signs Parameters

#  Return status, Use in arduino
SOMEONE = 0x01  #  There are people
NOONE = 0x02  #  No one
NOTHING = 0x03  #  No message
SOMEONE_STOP = 0x04  #  Somebody stop
SOMEONE_MOVE = 0x05  #  Somebody move
HUMANPARA = 0x06  #  Body Signs Parameters
SOMEONE_CLOSE = 0x07  #  Someone approaches
SOMEONE_AWAY = 0x08  #  Some people stay away
DETAILMESSAGE = 0x09  #  Underlying parameters of the human state

LEN_RESETFRAME = 10  #  Reset data frame length
LEN_FRAME_HEADER = 2 #  fixed Frame header size
LEN_FRAME_END = 2 # fixed End of frame size
LEN_CONTROL_WORD = 1
LEN_COMMAND_WORD = 1
LEN_LENGTH_IDENTIFIER = 1
LEN_CHECKSUM = 1

"""
!!NOTE!!
Human Movement Parameters: human movement amplitude values.

The Human Movement Parameters is
    - 0 when no one is in the space,
    - 1-5 when someone is present and stationary,
    - and 2-100 when the body is in motion
    
(the greater the motion amplitude the closer the body motion parameter is).
This means that if you feel that the results of the Sensor recognition do not meet your expectations,
you can output information about the presence of the human body
by customising the judgement of the Human Movement Parameters.
"""

class MR24():    
#  Reset data frame
    reset_frame = bytes([0x53, 0x59, 0x01, 0x02, 0x00, 0x01, 0x0F, 0xBF, 0x54, 0x43])

    def __init__(self, uart, maxBufferSize):
        self.uart = uart
        self.maxbuffersize = maxBufferSize
    
    ### reads sensor-data raw from current uart connection
        ### readAllData=False (if readAllData=True this will read the whole buffer if False it will
        ### read just the maxBufferSize
    def readRawData(self, readAllData=False):
        if readAllData:
            return self.uart.read(self.uart.in_waiting)
        else:
            return self.uart.read(self.maxbuffersize)
    
    def printRawData(self):
        ### prints the raw sensor-data to console
        print("sensor raw data: ")
        print(self.readRawData())
        
    def readDataFrame(self, data):
        pass
        #  TODO: read and parse data frame
        
    def readDataFromBuffer(self, maxFrames=1):
        