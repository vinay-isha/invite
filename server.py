import os, sys, mimetypes, re
from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# Ensure all mime types
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('application/javascript', '.mjs')
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('image/webp', '.webp')
mimetypes.add_type('video/webm', '.webm')
mimetypes.add_type('video/mp4', '.mp4')
mimetypes.add_type('audio/mpeg', '.mp3')
mimetypes.add_type('font/ttf', '.ttf')
mimetypes.add_type('font/woff2', '.woff2')
mimetypes.add_type('application/json', '.json')

class RangeFileWrapper:
    def __init__(self, f, length):
        self.f = f
        self.bytes_remaining = length

    def read(self, size=-1):
        if self.bytes_remaining <= 0:
            return b''
        if size < 0 or size > self.bytes_remaining:
            size = self.bytes_remaining
        data = self.f.read(size)
        self.bytes_remaining -= len(data)
        return data

    def close(self):
        self.f.close()

class SPAHandler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT_DIR, **kwargs)

    def address_string(self):
        # Disable slow reverse DNS lookup on Windows
        return self.client_address[0]

    def log_message(self, format, *args):
        # Keep server quiet and fast
        pass

    def send_head(self):
        clean_path = self.path.split('?')[0].split('#')[0].lstrip('/')
        local_path = os.path.join(ROOT_DIR, clean_path.replace('/', os.sep))

        # Check if local file exists
        if os.path.isdir(local_path):
            index_path = os.path.join(local_path, 'index.html')
            if os.path.isfile(index_path):
                local_path = index_path
            else:
                local_path = os.path.join(ROOT_DIR, 'index.html')
        elif not os.path.isfile(local_path):
            # Fallback to index.html for SPA
            local_path = os.path.join(ROOT_DIR, 'index.html')

        try:
            f = open(local_path, 'rb')
        except OSError:
            self.send_error(404, "File not found")
            return None

        fs = os.fstat(f.fileno())
        total_length = fs[6]
        ctype = self.guess_type(local_path)

        range_header = self.headers.get('Range')
        if range_header:
            m = re.match(r'bytes=(\d+)-(\d*)', range_header)
            if m:
                first_byte = int(m.group(1))
                last_byte = int(m.group(2)) if m.group(2) else total_length - 1
                if first_byte >= total_length:
                    self.send_error(416, "Requested Range Not Satisfiable")
                    f.close()
                    return None
                last_byte = min(last_byte, total_length - 1)
                length = last_byte - first_byte + 1

                self.send_response(206, "Partial Content")
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Range", f"bytes {first_byte}-{last_byte}/{total_length}")
                self.send_header("Content-Length", str(length))
                self.send_header("Accept-Ranges", "bytes")
                self.send_header("Cache-Control", "no-cache")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                f.seek(first_byte)
                return RangeFileWrapper(f, length)

        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(total_length))
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        return f

    def do_GET(self):
        f = self.send_head()
        if f:
            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

def run(port=8080):
    server_address = ('', port)
    httpd = ThreadedHTTPServer(server_address, SPAHandler)
    print(f'Server running at http://localhost:{port}/', flush=True)
    httpd.serve_forever()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    run(port)
