analog_value = 0
analog_value2 = 0
def read_analog_p0():
    global analog_value
    analog_value = pins.analog_read_pin(AnalogPin.P0)
    return Math.floor(analog_value / 128)
def set_pins(value: number):
    basic.show_number(value)
    pins.digital_write_pin(DigitalPin.P5, value & 0x01)
    pins.digital_write_pin(DigitalPin.P6, value >> 1 & 0x01)
    pins.digital_write_pin(DigitalPin.P7, value >> 2 & 0x01)

def on_forever():
    global analog_value2
    # Read analog value from P0 and map it to 0-7 range
    analog_value2 = read_analog_p0()
    set_pins(analog_value2)
    basic.pause(500)
basic.forever(on_forever)
