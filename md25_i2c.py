#for further details check https://robot-electronics.co.uk/htm/md25i2c.htm
import smbus

address = 0x58;
bus = smbus.SMBus(1)


def RESET_ENCODERS():
        bus.write_byte_data(address,16,32)

def SET_MODE(mode):
        bus.write_byte_data(addres,15,mode)

def GET_ENCODER_1():
        block = bus.read_i2c_block_data(address,2,4)
        encoder1 = (block[0] <<24) + (block[1] << 16) + (block[2] << 8) + block[3]
        return encoder1

def GET_ENCODER_2():
        block = bus.read_i2c_block_data(address,6,4)
        encoder1 = (block[0] <<24) + (block[1] << 16) + (block[2] << 8) + block[3]
        return encoder1

def SET_SPEED_1(speed):
        bus.write_byte_data(address,0,speed)

def SET_SPEED_2(speed):
        bus.write_byte_data(address,1,speed)

def BATTERY_VOLTS():
        data = bus.read_byte_data(address,10)
        return data

def MOTOR_1_CURRENT():
        data = bus.read_byte_data(address,11)
        return data

def MOTOR_2_CURRENT():
        data = bus.read_byte_data(address,12)
        return data

def SOFTWARE_REVISION():
        data = bus.read_byte_data(address,13)
        return data


#RESET_ENCODERS()
print BATTERY_VOLTS()
print SOFTWARE_REVISION()
print GET_ENCODER_1()
print GET_ENCODER_2()
SET_SPEED_1(130)
