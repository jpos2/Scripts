ind1 = 0
ind2 = 0

numbers={
  [0] = {1,2,3,4,5,6},
  [1] = {3,4},
  [2] = {2,3,0,6,5},
  [3] = {2,3,0,4,5},
  [4] = {1,0,3,4},
  [5] = {2,1,0,4,5},
  [6] = {1,6,5,4,0},
  [7] = {2,3,4},
  [8] = {0,1,2,3,4,5,6},
  [9] = {2,1,0,3,4}
}

for i=0,8,1 do
  gpio.mode(i, gpio.OUTPUT)
end

function callNumber (n)
  zera()
  for i,v in ipairs(numbers[n]) do
    gpio.write(v, gpio.LOW)
  end
end

function zera()
  for i=0,6,1 do
    gpio.write(i, gpio.HIGH)
  end
end

function getNumber(num)
  if num ~= nil then
    local c2=string.sub(num,-1)
    local c1=string.sub(num,-2,-2)
    if tonumber(c2) ~= nil then
      ind2=tonumber(c2)
    end
    if tonumber(c1) ~= nil then
      ind1=tonumber(c1)
    end
  else
    ind1=0
    ind2=0
  end
end

function startCronometro()
  tmr.alarm(0,1000,1,function()
    ind2 = ind2 + 1
    if ind2 == 10 then
      ind2 = 0
      ind1 = ind1 + 1
      if ind1 == 10 then
        ind1 = 0
      end
    end
  end)
end

function startTimer()
  tmr.alarm(3,1000,1,function()
    if ind2 == 0 then
      if ind1 == 0 then
        ind1 = 0
        ind2 = 1
        tmr.stop(3)
      else
        ind2 = 10
        ind1 = ind1 - 1
      end
    end
    ind2 = ind2 - 1
  end)
end

function zeraCronometro()
  tmr.stop(3)
  tmr.stop(0)
  ind1=0
  ind2=0
end

tmr.alarm(1,10,1,function()
  if gpio.read(7) == 0 then
    gpio.write(8, gpio.LOW)
    callNumber(ind1)
    gpio.write(7, gpio.HIGH)
  else
    gpio.write(7, gpio.LOW)
    callNumber(ind2)
    gpio.write(8, gpio.HIGH)
  end
end)

dofile("wifi.lua")
