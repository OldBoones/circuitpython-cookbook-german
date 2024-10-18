"""
Library for reading the 24GHz mmWave Sensor - Human Static Presence Module Lite (MR24HPC1) by Seeed.

Created by Heiko Ritter (09.10.2024) - current version 0.1.1

Version Info:
            0.1 basic functionality - reading raw Sensor data. (09.10.2024 - 23:23:00)
            0.1.1 added: data protocol constants (12.10.24 - 02:22:00)
            
TODO:
            Build memory optimized version without unnecessary vars and constants for specific models
            (and without comments)

these library should be able to read (TODO: and write) the raw Sensor-Data of the MR24HPC
and will be the supporting base for more libraries, working with other mmWave Radars
with serial communication via UART.

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
check the wiring, connection-command and/or datasheet of your board if connection
(initialization of class) is failing. NOTE: Not every GPIO PIN is able to work as serial.

REMEMBER: The Sensors receiving-port goes to your MCU(or Computers) sending-port and other way around

For Reading/Writing serial Data, wire your hardware as following

    sensor.RX <--> board.TX (or any other soft-serial capable pin/io)
    sensor.TX <--> board.RX (or any other soft-serial capable pin/io)
    5V <--> 5V
    GND <--> GND
    
for pin-trigger information you can use the 2 extra-pins
(TODO: Write Functions and Doc for those 2 additionals)

#  P1 True=occupied, False=unoccupied
#  P2 True=active, False=stationary

================= CONNECTION INFO =================
            
"""\

#  ====== GLOBAL VARS AND CONSTANTS ====== #  copied from the seeed library for Arduino
POSITION_HEAD1 = 0
POSITION_HEAD2 = 1
POSITION_CONTROL_WORD = 2
POSITION_COMMAND_WORD = 3
POSITION_LENGTH1 = 4
POSITION_LENGTH2 = 5
POSITION_DATA = 6
POSITION_CHECKSUM = -3
POSITION_FRAMEEND1 = -2
POSITION_FRAMEEND2 = -1


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
LEN_LENGTH_IDENTIFIER = 1 # is used 2 times (identifier 1, identifier 2)
LEN_CHECKSUM = 1

"""
!!DEFINITION OF FRAME STRUCTURE!! (for byte sizes (len of parts) check constants
frame header|control word|command word|length identifier1|length identifier2|data(variable size)|checksum|end of frame

check the dictionaries in __init__ for human readable translations of constants like command_word etc.

checksum calculation method:
“frame header + control word + command word + length identifier + data” summed to the lower eight bits

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

from DataFrame import DataFrame

class MR24():
    
    ###  Reset data frame
    reset_frame = bytes([0x53, 0x59, 0x01, 0x02, 0x00, 0x01, 0x0F, 0xBF, 0x54, 0x43])

    def __init__(self, uart, maxBufferSize=None, verbose=True):
        #  DEBUG MODE
        self.debugMode = verbose
        
        self.uart = uart
        self.maxbuffersize = maxBufferSize
        
        ### Initialize Control-Word Dictionary (TODO: Necessary?)
        self.control_words = {0x01:"Heartbeat",
                     0x02:"product information",
                     0x03:"UART upgrade",
                     0x05:"settings and operation",
                     0x08:"underlying open function",
                     0x80:"human presence information"}
        
        self.command_words = {0x01:"presence information",
                             0x02:"motion information",
                             0x03:"body movement information"}
        
    
    ### reads sensor-data raw from current uart connection
        ### readAllData=False (if readAllData=True this will read the whole buffer if False it will
        ### read just the maxBufferSize
    def readRawData(self):
        if maxBufferSize is None:
            return self.uart.read(self.uart_in_waiting)
        else:
            return self.uart.read(self.maxbuffersize)
    
    def calculateChecksum(self, frame_header, control_word, command_word, length_identifier, data):
        # TODO: Calculate that fucking checksum for fucks sake
        
        print(frame_header, control_word, command_word, length_identifier, data)
        # Summe aller Bytes
        total_sum = frame_header + control_word + command_word + length_identifier + sum(data)
    
        # Extrahieren der unteren 8 Bits (1 Byte) aus der Summe
        checksum = total_sum & 0xFF  # 0xFF ist eine Maske, um die unteren 8 Bits zu erhalten
    
        print(checksum)
    
        return checksum
    
    ### prints sensor raw data to console
    def printRawData(self):
        ### prints the raw sensor-data to console
        print("sensor raw data: ")
        print(self.readRawData())
    
    ### reads human presence data, is called if control_word is 0x80
    def humanPresenceInformation(self, commandWord, commandData):
        self.IsOccupied = False
        self.IsMoving = None
        self.BodyMovementParam = 0
        
        #  body movement information
        if commandWord == 0x03:
            self.BodyMovementParam = int.from_bytes(commandData, 'little')
            if self.BodyMovementParam == 0:
                pass
            if 0 < self.BodyMovementParam <=5:
                self.IsOccupied = True
                self.IsMoving = "Motionless"
            elif self.BodyMovementParam > 5:
                self.IsOccupied = True
                self.IsMoving = "Moving"
        #  motion information
        elif commandWord == 0x02:
            if commandData == 0x00:
                self.Moving = "Noone"
            elif commandData == 0x01:
                self.Moving = "Motionless"
            elif commandData == 0x02:
                self.Moving = "Active"
        #  presence information
        elif commandWord == 0x01:
            self.IsOccupied = int.from_bytes(commandData,'little') > 0
        
        return (self.IsOccupied, self.IsMoving, self.BodyMovementParam)
    
    ### Read data frames from buffer
    def readFrames(self, maxFrames=100):
        
        frames = []
        frame = []
        
        if self.uart.in_waiting == 0:
            return None
        
        data = readRawData()
        
        for pos in range(len(data)):
            if data[pos] == 0x53 and data[pos + POSITION_HEAD2] == 0x59:
                frame = [data[pos], data[pos+1]]
                pos += 1
                continue
            
                # found frame start
                
    
    ### reads data from buffer of serial device (mmWave Sensor), maxlen determined by buffer
    def readDataFromBuffer(self, maxFrames=1):
        
        if self.uart.in_waiting == 0:
            return None 
        
        data = bytes(self.uart.read(self.uart.in_waiting))
        
        if self.debugMode:
            print("readDataFromBuffer: ", data)
        
        # TODO: check if we need to limit buffersize
        for pos in range(len(data)):
            #  for information about the data frame structure, check text on top
            if data[pos] == MESSAGE_HEAD1 and data[pos+1] == MESSAGE_HEAD2:
                #  Frame starts here
                self.frameHeader = (data[pos],data[pos+1])
                pos += LEN_FRAME_HEADER #  setting current position beyond header
                self.controlWord = data[pos] #  setting controlWord
                pos += LEN_CONTROL_WORD  #  setting current position beyond control word
                self.commandWord = data[pos] #  setting command word
                pos += LEN_COMMAND_WORD  #  pos beyond command word
                self.lengthIdentifier1 = data[pos] # setting length
                pos += LEN_LENGTH_IDENTIFIER # move forward
                self.lengthIdentifier2 = data[pos] #  setting length 2
                pos += LEN_LENGTH_IDENTIFIER # move forward
                # frame data is next, the length of the data is determined by
                # lengthIdentifier2 (which is byte #6)
                self.frameData = data[pos:pos+self.lengthIdentifier2]
                pos += self.lengthIdentifier2 # setting currentPos beyond data
                # we ignore checksum, end of frame 1 and 2... cause i'm too dumb to calculate first and too lazy to check the latter
                pos += 3
                
                # todo: whats with the next frames?!
                
                #  check for control-word and react
                #  TODO: Put in extra function
                #  TODO: Check if class separation is better (classes for each controlWord/commandWord?)
                if self.debugMode:
                    print(f"\t...controlWord: {self.controlWord}({self.control_words[self.controlWord]})")
                if self.controlWord == 0x80:
                    if self.debugMode:
                        print(f"\t...humanPresenceInformation: {self.commandWord}({self.command_words[self.commandWord]}) - data: {self.frameData}")
                    return self.humanPresenceInformation(self.commandWord, self.frameData)