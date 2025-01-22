import sys, socket

size = 1924

def sendMessage(smtpServer, port, fromAddress,
		toAddress, message):
	IP = smtpServer
	PORT = int(port)
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((IP, PORT)) # opening a socket on a port
	print(s.recv(size).decode()) # response display
	s.send(b'HELO '+ fromAddress.split('@')[1].encode() +b'\n') # we impersonate our computer as a mail server associated with the sender's address
	print(s.recv(size).decode()) # output of the response received from the server
	
	# sending the sender's address
	s.send(b'MAIL FROM:<' + fromAddress.encode() + b'>\n')
	print(s.recv(size).decode())
	
	# sending the recipient's address
	s.send(b'RCPT TO:<' + toAddress.encode() + b'>\n')
	print(s.recv(size).decode())
	
	s.send(b"DATA\n") # sending data
	print(s.recv(size).decode())
	s.send(message.encode() + b'\n')
	s.send(b'\r\n.\r\n') # message completion <CR><LF>.<CR><LF>
	print(s.recv(size).decode()) # response display
	s.send(b'QUIT\n') # message completion
	print(s.recv(size).decode()) # respose display
	s.close()
	
	def main(args):
		smtpServer = args[1]
		port = args[2]
		fromAddress = args[3]
		toAddress = args[4]
		message = args[5]
		sendMessage(smtpServer, port, fromAddress,
				to Address, message)
	
	if __name__ == "__main__":
		main(sys.argv)