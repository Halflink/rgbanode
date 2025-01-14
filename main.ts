let analog_value = 0
let analog_value2 = 0
function read_analog_p0(): number {
    
    analog_value = pins.analogReadPin(AnalogPin.P0)
    return Math.floor(analog_value / 128)
}

function set_pins(value: number) {
    basic.showNumber(value)
    pins.digitalWritePin(DigitalPin.P5, value & 0x01)
    pins.digitalWritePin(DigitalPin.P6, value >> 1 & 0x01)
    pins.digitalWritePin(DigitalPin.P7, value >> 2 & 0x01)
}

basic.forever(function on_forever() {
    
    //  Read analog value from P0 and map it to 0-7 range
    analog_value2 = read_analog_p0()
    set_pins(analog_value2)
    basic.pause(500)
})
