import proxy
import re
import _thread
import urllib.parse
import sys
import os

from proxy.http.proxy import HttpProxyBasePlugin
from proxy.http.codes import httpStatusCodes
from proxy.common.utils import text_
from proxy.http.exception import HttpRequestRejected

from http.server import HTTPServer, BaseHTTPRequestHandler


class BlockPageServer(BaseHTTPRequestHandler):
    # noinspection PyByteLiteral
    BLOCK_PAGE_HEADER = b'''
        <head>
            <title>PYCM Block</title>
            <style>
                html,body {
                    width: 100%;
                    height: 100%;
                    margin: 0;
                    padding: 0;
                }
                .content {
                    width: 60%;
                    text-align: center;
                    margin: 0 auto;
                    position: relative;
                    top: 50%;
                    margin-top: -150px;
                }
                .container{
                    border: 2px dashed black;
                    border-radius: 15px;
                    padding-left: 10px;
                    padding-right: 10px;
                }
            </style>
        </head>
    '''
    BLOCK_PAGE_CONTENT = '''
        <body>
            <div class="content">
                <div class="container">
                    <h1>您访问的网站已被拦截</h1>
                    <h1>The website you browsed is blocked</h1>
                    <p>Website: {website}</p>
                    <p>Blocked by {blocker}</p>
                </div>
            </div>
        </body>
    '''

    def do_GET(self):
        if '?' in self.path:
            query_string = urllib.parse.unquote(self.path.split('?', 1)[1])
            params = urllib.parse.parse_qs(query_string)
            if ('url' in params.keys()) and ('from' in params.keys()):
                self.send_response(200)
                self.send_header('Content-type', 'text/html;charset=utf-8')
                self.end_headers()
                self.wfile.write(b'<html>' + self.BLOCK_PAGE_HEADER +
                                 self.BLOCK_PAGE_CONTENT.format(website=params['url'][0], blocker=params['from'][0]).encode(
                                     'utf-8') + b'</html>')
                return
        self.send_response(404)
        self.end_headers()

    def log_message(self, format, *args, **argv):
        return


class URLBlockPlugin(HttpProxyBasePlugin):
    HOST_BLACK_LIST = []
    HOST_IGNORE_LIST = [b'127.0.0.1', b'localhost']

    def __init__(self, *args, **argv):
        with open('URLBlockList.txt', 'r', encoding='utf8') as file:
            filter_list = list(map(lambda x: str(x.strip()), file.readlines()))
            self.HOST_BLACK_LIST = filter_list

    def before_upstream_connection(self, request):
        return request

    def handle_client_request(self, request):
        request_host = None
        if request.host:
            request_host = request.host
        else:
            if b'host' in request.headers:
                request_host = request.header(b'host')
        if request_host:
            if request_host in self.HOST_IGNORE_LIST:
                return request
            block = False
            for filter_host in self.HOST_BLACK_LIST:
                if re.search(filter_host, text_(request_host)):
                    block = True
                    break
            if block:
                raise HttpRequestRejected(
                    status_code=httpStatusCodes.PERMANENT_REDIRECT,
                    headers={b'Location': b'http://127.0.0.1:8898/?url=' +
                             request_host + b'&from=PYCM%20Class%20Management%20System'},
                    reason=b'Blocked',
                )
        return request

    def handle_upstream_chunk(self, chunk):
        return chunk

    def on_upstream_connection_close(self):
        pass


if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 8898), BlockPageServer)
    _thread.start_new_thread(lambda: server.serve_forever(), ())
    proxy.main([], plugins=[
        URLBlockPlugin,
    ])
