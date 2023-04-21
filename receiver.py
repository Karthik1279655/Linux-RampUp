import json
import socket


class Message:
    def __init__(self, message_id, text, time):
        self.message_id = message_id
        self.text = text
        self.time = time
        self.udp_ip = udp_ip
        self.udp_port = udp_port

        
class MessageReceiver():
	def __init__(self, udp_ip, udp_port):
		super().__init__(udp_ip, udp_port, Json_file=None)
		self.sock.bind((self.udp_ip, self.udp_port))

	def receive_messages(self):
		while True:
			data, addr = self.sock.recvfrom(1024)
			message_dict = json.loads(data.decode())
			message = Message(**message_dict)
			print(f"Received message: {message.__dict__}")

	def stop(self):
		super().stop()


if __name__ == '__main__':
    receiver = MessageReceiver(udp_ip="127.0.0.1",
                               udp_port=5050)
    receiver.receive_messages()
    receiver.stop()

