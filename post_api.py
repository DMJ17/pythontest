# 修改handlers.py第181行代码write(data)上面加一句： data=data.encode()
import json
from wsgiref.simple_server import make_server

def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'application/json')])

    # environ是当前请求的所有数据，包括Header和URL，body
    request_body = environ["wsgi.input"].read(int(environ.get("CONTENT_LENGTH", 0)))
    request_body = json.loads(request_body)

    name = request_body["name"]
    no = request_body["no"]

    dic = {'myNameIs': name, 'myNoIs': no}
    return [json.dumps(dic)]

if __name__ == "__main__":
    port = 6088
    httpd = make_server("0.0.0.0", port, application)
    print ("serving http on port {0}...".format(str(port)))

    httpd.serve_forever()