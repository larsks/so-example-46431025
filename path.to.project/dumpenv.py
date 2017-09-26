import http.server
import os


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        content = []

        for k, v in os.environ.items():
            content.append('{:20} {}'.format(k, v))

        self.wfile.write(bytes('\n'.join(content), 'utf-8'))
        return

server = http.server.HTTPServer(('0.0.0.0', 8080), Handler)
server.serve_forever()
