s=net.createServer(net.TCP)
s:listen(80,function(c)
  c:on("receive",function(client,req)
    local buf=''
    buf=buf..('HTTP/1.1 200 OK\n\n')
    buf=buf..('<!DOCTYPE HTML>\n')
    buf=buf..('<html>')
    buf=buf..('<body>\n')
    buf=buf..('<div align="center" width="100%">\n')
    buf=buf..('<h1 style="font-size:100px;">CRONOMETRO</h1>\n')
    buf=buf..('</div>')
    buf=buf..('<br><br>')
    buf=buf..('<div align="center" width="100%">\n')
    buf=buf..('<form action="" method="POST">\n')
    buf=buf..('<input style="font-size:80px; text-align:center;" align="middle" size="8" maxlength="2" type="text" name="num"/><br><br><br><br><br>\n')
    buf=buf..('<button style="font-size:80px; width:400px;" type="submit" name="status" value="start">Iniciar</button><br><br><br>\n')
    buf=buf..('<button style="font-size:80px; width:400px;" type="submit" name="status" value="stop">Parar</button><br><br><br>\n')
    buf=buf..('<button style="font-size:80px; width:400px;" type="submit" name="status" value="zera">Zerar</button><br><br><br>\n')
    buf=buf..('</form>')
    buf=buf..('</div>\n')
    buf=buf..('</body>')
    buf=buf..('</html>')

    local status=string.match(req,"status=(%w+)")
    local num=string.match(req,"num=(%d+)")
    if status ~= nil then
      if status == "start" then
        getNumber(num)
        startTimer()
      elseif status == "stop" then
        tmr.stop(0)
      elseif status == "zera" then
        zeraCronometro()
      end
    else
      client:send(buf)
    end
    c:on("sent",function(j) j:close() end)
  end)
end)

