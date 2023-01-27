import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import json

PORT = 8888


def run_server(port):
    """Inspired in this gist:
    https://gist.githubusercontent.com/mscalora/b6f86291353c360cb5550dc978129069/raw/4207a8cf8de31f8ca9fb6727d823e8029937f927/server.py

    Args:
        port (int): port to listen to.
    """

    class Server(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                f"""<html><head><title>GET</title></head>
                    <body style="display: grid; place-items: center;">
                    <form method="POST">
                      <p>Blue: <input name="blue" value="robin's egg"></p>
                      <p>Green: <input name="green" value="sea foam"></p>
                      <p>Red: <input name="red" type="range" min="0" max ="100" step="0.01" value="27.76"></p>
                      <p><button>Submit</button></p>
                      <p><button>Gemme OUT!</button></p>
                    </form>
                    <pre>Auth data: {self.decode_x_auth()} </pre>
                    </body></html>
                """.encode(
                    "utf-8"
                )
            )

        def do_POST(self):
            length = int(self.headers.get("content-length", 0))
            # if length == 0:
            #     self.send_response(200)
            #     self.send_header("Content-type", "text/html")
            #     self.end_headers()
            #     self.wfile.write(
            #         """<html><head><title>POST</title></head>
            #         <body style="display: grid; place-items: center;">
            #         <pre>NO DATA HERE!</pre>
            #         </body></html>
            #       """
            #     )

            field_data = self.rfile.read(length)
            fields = parse.parse_qs(str(field_data, "UTF-8"))

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                (
                    f"""
                    <html><head><title>POST</title></head>
                    <body style="display: grid; place-items: center;">
                    <pre>{json.dumps(fields, indent=2)}</pre>
                    <pre>Auth data: {self.decode_x_auth()} </pre>
                    </body></html>
                  """
                ).encode("UTF-8")
            )

        def decode_auth(self):
            auth_data = self.headers.get("Authorization", "")
            auth_data = auth_data.replace("Basic ", "").strip()
            if auth_data:
                return base64.b64decode(auth_data.encode("ascii").decode("utf-8")).decode("utf-8")
            return "No Auth Data"

        def decode_x_auth(self):
            """Retrieves the 'X-Auth-Request-User' header wich nginx should have set
            based on the logged in user from the Basic Auth header
            """
            return self.headers.get("X-Auth-Request-User", "").strip()


    handler_class = Server
    httpd = HTTPServer(("", port), handler_class)
    print(f"Browse to http://localhost:{PORT}")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server(PORT)
