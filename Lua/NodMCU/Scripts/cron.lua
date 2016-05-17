function pinset()

    for pin = 0,8 do gpio.mode(pin, gpio.OUTPUT) end
    for pin = 0,6 do gpio.write(pin, gpio.HIGH) end
    for pin = 7,8 do gpio.write(pin, gpio.HIGH) end

end

-- array with numbers in binary, 0 to 9

numbers = {63, 6, 91, 79, 102, 109, 125, 7, 127, 111}

la = 7
lb = 8

function blink()
    tmr.alarm(1, 200, 1, function()
        gpio.write(la, 0)
        gpio.write(lb, 1)
        lc = la
        la = lb
        lb = lc
    end)
end
-- function high led -----------------------------------------------------------

function hight(n)
    for i = 1,7 do
        if (bit.isset(numbers[n], i-1)) then
            gpio.write(i-1, 0)
        else
            gpio.write(i-1, 1)
        -- blink()
        end
    end
end
--------------------------------------------------------------------------------
pinset()
a = 0

     
-- loop -- 

ax = 0 
a = 1
b = 1

-- 

tmr.alarm(0, 1000, 1, function()

    tmr.alarm(1, 5, 1, function()
            
        gpio.write(la, 0)
        hight(b)
        gpio.write(lb, 1)
        hight(a)
        gpio.write(lb, 0)
        gpio.write(la, 1)
        ax = ax + 5
        if ax == 1000 then
            tmr.stop(1)
        end   
    end)
    b = (b + 1) % 10
    if b == 9 then
	a = (a + 1) % 10
    end

end)
