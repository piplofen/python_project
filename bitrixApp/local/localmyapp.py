import base64

import helpF as hf
import localmyapputils as lmu
import redis33
import utils as u
import newFile

# gunicorn -b 0.0.0.0:8081 localmyapp:localapp --reload

local = "/black"

db = newFile.Database()

def localapp(environ, start_response):
    if environ["PATH_INFO"] == f"{local}/echo":
        data = b'200 OK local'
        status = '200'
        response_headers = [
            ('Content-type', 'text/plain'),
            ('Content-Length', str(len(data)))
        ]
        start_response(status, response_headers)

        return iter([data])

    # elif smgsg:

    elif environ["PATH_INFO"] == f"{local}/log.php":
        body = hf.getBody(environ)
        d1 = hf.convertJson(body)
        print(d1)
        if d1['type'] == "0":
            print("Простой вход")
            if lmu.checkLoginUser(d1):
                data = b'OK'
                status = '200'
                response_headers = [
                    ('Content-type', 'text/plain'),
                    ('Content-Length', str(len(data)))
                ]
                start_response(status, response_headers)

                return iter([data])
            else:
                noAuth(start_response)
        elif d1['type'] == "1":
            print("Вход с галочкой")
            print(d1['id'])
            print(d1['token'])
            if lmu.checkLoginUser(d1):
                db.cur.execute(f"insert into auth(id, token) values({int(base64.b64decode(d1['id']))}, '{d1['token']}')")
                db.conn.commit()
                data = b'OK'
                status = '200'
                response_headers = [
                    ('Content-type', 'text/plain'),
                    ('Content-Length', str(len(data)))
                ]
                start_response(status, response_headers)

                return iter([data])
            else:
                noAuth(start_response)

        # print(d1, 1)
        # red = redis33.Redis1(3)
        # # print(d1["id"], d1["token"], 232322)
        # # red.checkToken(u.decoding(d1["id"]), u.decoding(d1["token"]))
        # # red.insertDataList(u.decoding(d1["id"]), u.decoding(d1["token"])) записывает токены в список
        # if lmu.checkLoginUser(d1):
        #     try:
        #         u.newToken(u.decoding(d1["id"]), u.decoding(d1["mac"]), u.decoding(d1["serial"]))
        #     except Exception as e:
        #         data = b'ERROR'
        #     data = b'OK'
        #     status = '200'
        #     response_headers = [
        #         ('Content-type', 'text/plain'),
        #         ('Content-Length', str(len(data)))
        #     ]
        #     start_response(status, response_headers)
        #
        #     return iter([data])
        # else:
        #     return noAuth(start_response)



    elif environ["PATH_INFO"] == f"{local}/login.php":s
        body = hf.getBody(environ)
        d1 = hf.convertJson(body)
        if lmu.checkLoginUser(d1):
            data = b'OK'
            status = '200'
            response_headers = [
                ('Content-type', 'text/plain'),
                ('Content-Length', str(len(data)))
            ]
            start_response(status, response_headers)

            return iter([data])
        else:
            return noAuth(start_response)
    else:
        noAuth(start_response)

def noAuth(start_response):
    data = b'404 Unauthorized'
    status = '404'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)

    return iter([data])