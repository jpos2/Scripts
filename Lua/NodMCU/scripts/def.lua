function def_pin()
    for pin = 0,8 do gpio.mode(pin, gpio.INPUT) end
end

function loop()

    while 1 do

        -- zerando todos pinos
    for pin = 0,8 do gpio.write(pin, gpio.HIGH) end

    -- num 0
    for pin = 0,8 do gpio.write(pin, gpio.HIGH) end

    for pin = 0,3 do gpio.write(pin, gpio.LOW) end
    for pin = 5,6 do gpio.write(pin, gpio.LOW) end
    
    tmr.delay(1000000)
    
    -- num 1
    for pin = 0,8 do gpio.write(pin, gpio.HIGH) end
    
    for pin = 1,2 do gpio.write(pin, gpio.LOW) end
    
    tmr.delay(1000000)    
       
    end
end

def_pin()

loop()