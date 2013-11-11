require 'socket'
require 'pty'

# Without this threads don't exit this process to report exceptions.
Thread::abort_on_exception = true

server = TCPServer.new 9000
loop do
  # Threads are what allow this server to accept multiple connections.
  Thread.start(server.accept) do |client|

    # First read the data that the client has sent
    request = ""
    loop do
      # Read in 1024 chunks
      data = client.recv(1024)
      request = request + data
      # Arbitrary, but use "\r\n" as the signature for the end of data.
      break if data.end_with? "\r\n"
    end

    # Split the data into a list of lines
    lines = request.split("\n")

    # A very crude means of security to stop any old hacker getting through.
    secret = lines.shift
    file = "/tmp/deis/rendevous_secrets/" + secret
    if !File.exist?(file)
      client.puts('Incorrect secret sent.')
      client.close
      break
    else
      File.delete(file)
    end

    # The actual command to run
    payload = lines.first.split(':')

    if payload.first == 'build'
      cmd = "/usr/local/bin/deis-buildstep-hook #{payload[1]} #{payload[2]}"
    else
      client.puts 'Unrecognised command. Aborting.'
      break
    end

    # By using a pseudo terminal we avoid all the output buffering problems.
    # And data can be sent back as and when it is generated, rather than in one big lump when the
    # process finishes.
    begin
      # 2>&1 redirects STDERR and STDOUT to STDOUT
      PTY.spawn(cmd + " 2>&1") do |stdin, stdout, pid|
        begin
          stdin.each { |line| client.puts line }
        rescue Errno::EIO
          # Most likely just means that the process has ended its ouput.
        rescue Errno::EPIPE
          # Pipe broken. Probably keyboard interrupt from client.
          break
        end
      end
    rescue PTY::ChildExited
      client.puts "Process unexpectedly exited!"
    end

    # End the connection
    client.close
  end
end
