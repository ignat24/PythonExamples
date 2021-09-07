import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from users import Users, UserExistError, UserNotFoundError
from jsonschema import ValidationError


NOT_FOUND_USER_RESPONSE = {"error": "User not found"}
NOT_VALID_REQUEST_DATA = {"error": "not valid request data"}

users = Users()


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200, body=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}).encode('utf-8'))

    def _pars_body(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        return json.loads(self.rfile.read(content_length).decode('utf-8'))  # <--- Gets the data itself

    @staticmethod
    def _create_error_response(error_message):
        return {"error": error_message}

    def do_Get(self):
        if self.path == "/reset":
            users.reset_user()
            self._set_response(200, {})
        elif self.path == "/users":
            status = 200
            body = users.get_users()
            self._set_response(status, body)
        elif "/user/" in self.path:
            username = self.path.replace("/user/", '')
            user = users.get_user_by_username(username)

            self._set_response(200, user) if user else self._set_response(400, NOT_FOUND_USER_RESPONSE)
        else:
            self._set_response(418)

    def do_Post(self):
        if "createFromList" in self.path:
            new_user_data = self._pars_body()
            try:
                new_user = [users.add_user(user_data) for user_data in new_user_data]
            except(ValidationError, UserExistError):
                self._set_response(400, {})
        elif "/user" in self.path:
            user_data = self._pars_body()
            try:
                new_user = users.add_user(user_data)
                self._set_response(201, new_user)
            except(ValidationError, UserExistError):
                self._set_response(400, {})

        else:
            self._set_response(418)

    def do_PUT(self):
        if "/user/" in self.path:
            str_id = self.path.replace("/user/", '')
            user_id = int(str_id) if str_id.isdigit() else None
            body = self._pars_body()

            try:
                user = users.update_user(user_id, body)
                self._set_response(200, user)
            except ValidationError:
                self._set_response(400, NOT_VALID_REQUEST_DATA)
            except UserNotFoundError as e:
                self._set_response(404, self._create_error_response(e.__str__()))
        else:
            self._set_response(418)

    def do_DELETE(self):
        if "/user/" in self.path:
            user_id = self.path.replace("/user/", '')

            try:
                users.remove_user(user_id)
                self._set_response(200, {})

            except UserNotFoundError as e:
                self._set_response(404, self._create_error_response(e.__str__()))

        else:
            self._set_response(418)


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host='localhost', port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()


