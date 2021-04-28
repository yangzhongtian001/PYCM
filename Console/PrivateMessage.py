from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
import socket
import struct
from threading import Thread
from PIL import Image
from PIL.ImageQt import ImageQt
from io import BytesIO
import zlib
import numpy as np
import time
import os
from Packages import NetworkDiscoverFlag, PrivateMessageFlag


class FileMerger(object):
    file_buffer = None
    file_upload_path = None

    def __init__(self, file_upload_path, parent=None):
        self.chuck_count = None
        self.file_buffer = {}
        self.file_upload_path = file_upload_path
        self.parent = parent

    def update_chuck(self, ip, index, amount, buffer):
        if ip not in self.file_buffer.keys():
            self.file_buffer[ip] = {'chuck_count': amount, 'buffers': []}
        self.file_buffer[ip]['buffers'].append((index, buffer))
        if len(self.file_buffer[ip]['buffers']) >= self.file_buffer[ip]['chuck_count']:
            file_buffer_sorted = sorted(self.file_buffer[ip]['buffers'], key=lambda x: x[0])
            file_data = b''.join(map(lambda x: x[1], file_buffer_sorted))
            file_timestamp = time.strftime("%Y%m%d-%H.%M.%S", time.localtime(time.time()))
            file_name = f'[{file_timestamp}] {self.parent.get_client_label_by_ip(ip)}.zip'
            open(os.path.join(self.file_upload_path, file_name), 'wb').write(file_data)
            self.file_buffer.pop(ip)
            return True
        return False


class PrivateMessage(object):
    socket_ip = None
    socket_port = None
    socket_buffer_size = None
    socket_obj = None

    def __init__(self, parent, root_parent, socket_ip, socket_port, socket_buffer_size):
        self.parent = parent
        self.root_parent = root_parent
        self.socket_ip = socket_ip
        self.socket_port = socket_port
        self.socket_buffer_size = socket_buffer_size
        self.__init_socket_obj()

    def __init_socket_obj(self):
        self.socket_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_obj.bind(('', self.socket_port))

    def start(self):
        payload_size = self.socket_buffer_size - struct.calcsize('!2i')
        chuck_size = self.socket_buffer_size - struct.calcsize('!5i')
        file_merger = FileMerger(self.parent.file_upload_path, self.root_parent)
        while True:
            try:
                socket_data, socket_addr = self.socket_obj.recvfrom(self.socket_buffer_size)
                unpacked_flag, unpacked_length, unpacked_data = struct.unpack(f'!2i{payload_size}s', socket_data)
                unpacked_data = unpacked_data[:unpacked_length]
                if unpacked_flag == PrivateMessageFlag.ClientLogin:
                    client_mac = unpacked_data.decode()
                    self.parent.client_login_logout.emit('online', socket_addr[0], client_mac)
                elif unpacked_flag == PrivateMessageFlag.ClientLogout:
                    client_mac = unpacked_data.decode()
                    self.parent.client_login_logout.emit('offline', socket_addr[0], client_mac)
                elif unpacked_flag == PrivateMessageFlag.ClientScreen:
                    unpacked_data = zlib.decompress(unpacked_data)
                    image = Image.open(BytesIO(unpacked_data)).toqpixmap()
                    self.parent.client_desktop_recieved.emit(socket_addr[0], image)
                elif unpacked_flag == PrivateMessageFlag.ClientFile:
                    file_index, file_buffer_length, file_amount, file_buffer = struct.unpack(f'!3i{chuck_size}s',
                                                                                             unpacked_data)
                    status = file_merger.update_chuck(socket_addr[0], file_index, file_amount,
                                                      file_buffer[:file_buffer_length])
                    if status:
                        self.parent.client_file_recieved.emit(socket_addr[0])

            except KeyboardInterrupt:
                self.socket_obj.close()
                return None
            except Exception as e:
                print(e)
