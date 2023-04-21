import json
import socket


class Message:
    def __init__(self, message_id, text, time):
        self.message_id = message_id
        self.text = text
        self.time = time


class MessageTransmitter:
    def __init__(self, udp_ip, udp_port, Json_file):
        self.udp_ip = udp_ip
        self.udp_port = udp_port
        self.Json_file = Json_file
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def transmit_messages(self):
        with open(self.Json_file, 'r') as file:
            messages_data = json.load(file)

        for message_data in messages_data:
            message = Message(**message_data)
            message_str = json.dumps(message.__dict__)
            self.sock.sendto(message_str.encode(), (self.udp_ip, self.udp_port))
            print(f"Sent message: {message.__dict__}")

    def stop(self):
        self.sock.close()


if __name__ == '__main__':
    transmitter = MessageTransmitter(
        udp_ip="127.0.0.1",
        udp_port=5006,
        Json_file="messages.json"
    )
    transmitter.transmit_messages()




