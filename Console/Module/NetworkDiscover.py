import socket
import time
import struct
import logging
from Module.Packages import NetworkDiscoverFlag


class NetworkDiscover(object):
    current_ip = None
    socket_ip = None
    socket_port = None
    socket_obj = None
    discover_interval = None

    def __init__(self, current_ip, socket_ip, socket_port, discover_interval=5):
        self.current_ip = current_ip
        self.socket_ip = socket_ip
        self.socket_port = socket_port
        self.discover_interval = discover_interval
        self.__init_socket_obj()

    def __init_socket_obj(self):
        self.socket_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket_obj.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
        self.socket_obj.setsockopt(
            socket.IPPROTO_IP,
            socket.IP_ADD_MEMBERSHIP,
            socket.inet_aton(self.socket_ip) + socket.inet_aton(self.current_ip)
        )

    def start(self):
        socket_packet = struct.pack('!i', NetworkDiscoverFlag.ConsoleFlag)
        while True:
            try:
                self.socket_obj.sendto(socket_packet, (self.socket_ip, self.socket_port))
                time.sleep(self.discover_interval)
            except Exception as e:
                logging.warning(f'Failed to send net discover pack: {e}')
