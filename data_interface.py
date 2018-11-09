# 修改handlers.py第181行代码write(data)上面加一句： data=data.encode()
from wsgiref.simple_server import make_server
import time
import _thread
from data_fetch import Data_Set
class Data_Interface():
    def STK_BASIC_INFO(self,environ, start_response):
        # 定义文件请求的类型和当前请求成功的code
        start_response('200 OK', [('Content-Type', 'application/json')])
        data_set = Data_Set()
        json_data =data_set.STK_BASIC_INFO()
        return json_data

    def COM_INC_INFO_PRO(self,environ, start_response):
        start_response('200 OK', [('Content-Type', 'application/json')])
        data_set = Data_Set()
        json_data = data_set.COM_INC_INFO_PRO()
        return json_data

    def PUB_INDU_CODE(self,environ, start_response):
        start_response('200 OK', [('Content-Type', 'application/json')])
        data_set = Data_Set()
        json_data = data_set.PUB_INDU_CODE()
        return json_data

    def PUB_COM_INDU_RELA(self,environ, start_response):
        start_response('200 OK', [('Content-Type', 'application/json')])
        data_set = Data_Set()
        json_data = data_set.PUB_COM_INDU_RELA()
        return json_data

    def FIN_BALA_SHORT(self,environ, start_response):
        start_response('200 OK', [('Content-Type', 'application/json')])
        data_set = Data_Set()
        json_data = data_set.FIN_BALA_SHORT()
        return json_data

    def FIN_CASH_SHORT(self,environ, start_response):
        start_response('200 OK', [('Content-Type', 'application/json')])
        data_set = Data_Set()
        json_data = data_set.FIN_CASH_SHORT()
        return json_data

    def FIN_INCO_SHORT(self,environ, start_response):
        start_response('200 OK', [('Content-Type', 'application/json')])
        data_set = Data_Set()
        json_data = data_set.FIN_INCO_SHORT()
        return json_data

def BASIC_INFO():
    data_interface = Data_Interface()
    port = 6001
    httpd = make_server("0.0.0.0", port, data_interface.STK_BASIC_INFO)
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()

def INC_INFO_PRO():
    data_interface = Data_Interface()
    port = 6002
    httpd = make_server("0.0.0.0", port, data_interface.COM_INC_INFO_PRO)
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()

def INDU_CODE():
    data_interface = Data_Interface()
    port = 6003
    httpd = make_server("0.0.0.0", port, data_interface.PUB_INDU_CODE)
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()

def COM_INDU_RELA():
    data_interface = Data_Interface()
    port = 6004
    httpd = make_server("0.0.0.0", port, data_interface.PUB_COM_INDU_RELA)
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()

def BALA_SHORT():
    data_interface = Data_Interface()
    port = 6005
    httpd = make_server("0.0.0.0", port, data_interface.FIN_BALA_SHORT)
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()

def CASH_SHORT():
    data_interface = Data_Interface()
    port = 6006
    httpd = make_server("0.0.0.0", port, data_interface.FIN_CASH_SHORT)
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()

def INCO_SHORT():
    data_interface = Data_Interface()
    port = 6007
    httpd = make_server("0.0.0.0", port, data_interface.FIN_INCO_SHORT)
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()

# 创建线程启动接口
if __name__ == "__main__":
    try:
        _thread.start_new_thread(BASIC_INFO, ())
        _thread.start_new_thread(INC_INFO_PRO, ())
        _thread.start_new_thread(INDU_CODE, ())
        _thread.start_new_thread(COM_INDU_RELA, ())
        _thread.start_new_thread(BALA_SHORT, ())
        _thread.start_new_thread(CASH_SHORT, ())
        _thread.start_new_thread(INCO_SHORT, ())
    except:
        print("Error: 无法启动线程")
    while 1:
        pass

