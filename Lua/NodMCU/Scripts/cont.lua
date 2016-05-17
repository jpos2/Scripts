for pin = 0,8 do gpio.mode(pin, gpio.INPUT) end

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
    -- num 2
    for pin = 0,8 do gpio.write(pin, gpio.HIGH) end
    
    for pin = 0,1 do gpio.write(pin, gpio.LOW) end
    gpio.write(3, 0)
    gpio.write(5, 0)
    for pin = 7,8 do gpio.write(pin, gpio.LOW) end
    
    tmr.delay(1000000)

    -- num 3
    for pin = 0,8 do gpio.write(pin, gpio.HIGH) end

    for pin = 0,3 do gpio.write(pin, gpio.LOW) end
    gpio.write(7, 0)

    tmr.delay(1000000)
    
    -- num 4
    for pin = 0,8 do gpio.write(pin, gpio.HIGH) end

    for pin = 1,2 do gpio.write(pin, gpio.LOW) end
    for pin = 6,7 do gpio.write(pin, gpio.LOW) end

    tmr.delay(1000000)

    -- num 5
    for pin = 0,8 do gpio.write(pin, gpio.HIGH) end

    gpio.write(0, 0)
    for pin = 2,3 do gpio.write(pin, gpio.LOW) end
    for pin = 6,7 do gpio.write(pin, gpio.LOW) end

    tmr.delay(1000000)

    -- num 6
    for pin = 0,8 do gpio.write(pin, gpio.HIGH) end

    gpio.write(0, 0)
    for pin = 2,3 do gpio.write(pin, gpio.LOW) end
    for pin = 5,7 do gpio.write(pin, gpio.LOW) end
    
    tmr.delay(1000000)
    
    -- num 7
    for pin = 0,8 do gpio.write(pin, gpio.HIGH) end

    for pin = 0,2 do gpio.write(pin, gpio.LOW) end
    
    tmr.delay(1000000)

    -- num 8
    for pin = 0,8 do gpio.write(pin, gpio.HIGH) end

    for pin = 0,3 do gpio.write(pin, gpio.LOW) end
    for pin = 5,7 do gpio.write(pin, gpio.LOW) end
    
    tmr.delay(1000000)

    -- num 9
    for pin = 0,8 do gpio.write(pin, gpio.HIGH) end

    for pin = 0,2 do gpio.write(pin, gpio.LOW) end
    for pin = 6,7 do gpio.write(pin, gpio.LOW) end
    tmr.delay(1000000)
    
end