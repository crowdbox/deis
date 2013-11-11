require 'socket'

server = TCPServer.new 9000
loop do
  Thread.start(server.accept) do |client|
    while line = client.gets
      puts line
      break
    end
    puts "doing..."
    client.puts `/usr/local/bin/sleepy.sh`
    client.close
  end
end
