wifi.setmode(wifi.STATION)
wifi.sta.config("ssid","senha")
wifi.sta.connect()

tmr.alarm(2,4000,1,function()
  if wifi.sta.getip() == nil then
    print("Connecting to WIFI...\n")
  else
    ip,mask,gw = wifi.sta.getip()
    print(ip)
    local c1=string.sub(ip,-2,-2)
    local c2=string.sub(ip,-1)
    if tonumber(c2) ~= nil then
      ind2=tonumber(c2)
    else
      tmr.stop(2)
    end
    if tonumber(c1) ~= nil then
      ind1=tonumber(c1)
    else
      tmr.stop(2)
    end
    tmr.stop(2)
  end
end)

dofile("web.lua") 
