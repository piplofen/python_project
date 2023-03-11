from pprint import pprint
import json, helpF as hf, utils as u, crest, ikek, kek, myapputils as mu, settings as s, requests, jinja2, newFile, redis33 as red, datetime

import database

# redis33 as red, newFile

# import gunicorn
# s=gunicorn.SERVER_SOFTWARE

# source venv/bin/activate
# gunicorn -b 0.0.0.0:8080 myapp:app --reload

i = 0

HTML = """

<html lang="ru">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">
    <title>Узнать Ваш IP адрес</title>
    <script>
function altr(){
    var obj=document.getElementById("iframeid");
    var n1=obj.contentWindow.document.getElementById("inp").value;
    alert(n1);
}
</script>
  </head>
  <body class="bg-info">
    <div class="container">
      <h1 class="text-white text-center mx-auto p-2 mt-4 mb-3">Ваш IP-адрес</h1>
      <div class="bg-light card-block mx-auto text-center">
        <h1 class="display-3 p-2">{ip_address} {zz}</h1>
      </div>
    </div>
  </body>
</html>
"""

head = """
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>ЖОПА</title>
    <script>
    $('#myForm').submit(function() { // Отслеживаем событие отправки 
        var string = $(this).serialize(); // Сериализуем все данные формы чтоб не пришлось явно указывать каждое её поле
        var method = $(this).attr('method'); // Достаем метод отправки
        var action = $(this).attr('action'); // И урл экшена
        $.ajax({ // Отправляем данные при помощи метода библиотеки 
            type: method,
            url: action,
            data: string,
            dataType: "json", // Указываем в каком формате ожидаем получить ответ
            success: function(request) { // Описываем сценарий при получении ответа
                alert(request.message);
            },
            error: function() { // Описываем сценарий при ошибке отправки
                alert('error');
            }
        });
    });
    </script>
    
    <script>
    function display() {
    myString = "Hello, world!";
    document.write("<h1>Ой что то поломалось</h1>");
    alert(myString);
    n1=document.getElementById("inp");
    console.log(n1);
    
    }
    
    </script>    
    <script>
    function altr(){
    var n1=document.getElementById("inp");
    alert(n1.value);
    }
    </script>
    <style>
        @import url(https://fonts.googleapis.com/css?family=Roboto:300);

.login-page {
    width: 50%;
    padding: 8% 0 0;
    margin: auto;
}
.form {
    position: relative;
    z-index: 1;
    background: #FFFFFF;
    border-radius: 1.5vh;
    max-width: auto;
    margin: 0 auto 100px;
    padding: 45px;
    text-align: center;
    box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}
.form input {
    font-family: "Roboto", sans-serif;
    outline: 0;
    background: #f2f2f2;
    width: 100%;
    border: 0;
    margin: 0 0 15px;
    padding: 15px;
    box-sizing: border-box;
    font-size: 20px;
}

h1 {
font-family: "Roboto", sans-serif;
font-size: 26px;
}
.form button {
    font-family: "Roboto", sans-serif;
    text-transform: uppercase;
    outline: 0;
    background: #4CAF50;
    width: 100%;
    border: 0;
    padding: 15px;
    color: #FFFFFF;
    font-size: 14px;
    -webkit-transition: all 0.3 ease;
    transition: all 0.3 ease;
    cursor: pointer;
}
.form button:hover,.form button:active,.form button:focus {
    background: #43A047;
}
.form .message {
    margin: 15px 0 0;
    color: #b3b3b3;
    font-size: 12px;
}
.form .message a {
    color: #4CAF50;
    text-decoration: none;
}
.form .register-form {
    display: none;
}
.container {
    position: relative;
    z-index: 1;
    max-width: 300px;
    margin: 0 auto;
}
.container:before, .container:after {
    content: "";
    display: block;
    clear: both;
}
.container .info {
    margin: 50px auto;
    text-align: center;
}
.container .info h1 {
    margin: 0 0 15px;
    padding: 0;
    font-size: 36px;
    font-weight: 300;
    color: #1a1a1a;
}
.container .info span {
    color: #4d4d4d;
    font-size: 12px;
}
.container .info span a {
    color: #000000;
    text-decoration: none;
}
.container .info span .fa {
    color: #EF3B3A;
}
body {
<!--    background: #76b852; /* fallback for old browsers */-->
<!--    background: rgb(141,194,111);-->
<!--    background: linear-gradient(90deg, rgba(141,194,111,1) 0%, rgba(118,184,82,1) 50%);-->
    font-family: "Roboto", sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
    </style>
</head>
"""

BODY = """
<body>
<div class="login-page">
    <div class="form">
        <form id="myForm" action="reg.php" method="post" class="login-form">
            <h1>Ваш аккаунт<br> не привязан к рабочему месту</h1>
            <input type="hidden" value={id} readonly name="id"/>
            <input id="229" type="text" value={ss} readonly name="emp"/>
            
            <input id="228" name="password" type="password" target="rabs" placeholder="Пароль"/>
            <input type="hidden" value={token} readonly name="token"/>
            <button type="submit">Привязать аккаунт </button>
        </form>
    </div>
</div>
</body>
</html>
"""

regOk = """
<body>
<div class="login-page">
    <div class="form">
        <form id="myForm" action="reg.php" method="post" class="login-form">
            <h1>{mes}</h1>
        </form>
    </div>
</div>
</body>
</html>
"""


def app(environ, start_response):
    global i
    if environ["PATH_INFO"] == "/api/token/api":
        text = hf.splitParams(environ)
        if u.checkToken(text):
            i += 1
            status = '200 OK'
            data = b'200 OK'
            response_headers = [
                # Set - Cookie: cookieName = cookieValue;
                ('Content-type', 'text/html; charset=utf-8'),
                ('Content-Length', str(len(data)))  # ; SameSite=None; Secure; HttpOnly
            ]
            # image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
            start_response(status, response_headers)
            # html = HTML.format(ip_address=environ["REMOTE_ADDR"], zz=i)
            # html_as_bytes = html.encode('utf-8')


            pprint(text)

            # print("=====================NEW=====================")
            #
            # print(returnb(start_response, environ))
            #
            # print("=====================END=====================")

            with open("output.json", "w") as file:
                json.dump(text, file, indent=1)

            return iter([data])
        else:

            data = b'401 Unauthorized'
            status = '401'
            response_headers = [
                ('Content-type', 'text/plain'),
                ('Content-Length', str(len(data)))
            ]
            start_response(status, response_headers)
            return iter([data])

    elif environ["PATH_INFO"] == "/":
        data = b'200 BK OK'
        status = '200'
        response_headers = [
            ("Set-Cookie", "member_id=main"),
            ('Content-type', 'text/plain'),
            ('Content-Length', str(len(data)))
        ]
        start_response(status, response_headers)
        print(hf.returnb(start_response, environ))

        return iter([data])

    elif environ["PATH_INFO"] == "/ikek.php":

        # headers = hf.splitHeaders(environ)
        # params = hf.splitParams(environ)
        # print(type(hf.allParams(environ)))

        # data = b'200 BK OK'
        # status = '200'
        # response_headers = [
        #     ('Content-type', 'text/plain'),
        #     ('Content-Length', str(len(data)))
        # ]
        # start_response(status, response_headers)

        print("Я пришел с bk.fa39.ru/ikek.php")

        # pprint(hf.allParams(environ))

        # print(returnb(start_response, environ))
        # print("===================== HEADERS =====================")
        # pprint(headers)
        # print("===================== PARAMS =====================")
        # pprint(params)

        # print(testHTML.test(environ, start_response))

        return ikek.ikek(environ, start_response)

    elif environ["PATH_INFO"] == "/kek.php":
        print("хыхыхыхы")
        # hf.allParams(environ)
        cookie = hf.getCookies(environ)
        try:
            # cookie = True
            if cookie:
                print("кук есть")
                # print(cookie['member_id'])
                r = kek.kek(environ, start_response)
                return iter([r])
            else:
                print("кук нет")
                inParams = hf.allParams(environ)
                auth = inParams["AUTH_ID"]
                url = f"{s.urlForAuth}profile.json?auth={auth}"
                r = requests.get(url)
                res = r.json()
                if mu.checkUser(res["result"]["ID"]):
                    print('Вы уже зарегистрированы. Иду за токеном.', 'utf-8')
                    data = b'reg true'
                    status = '200'
                    response_headers = [
                        ('Content-type', 'text/html; charset=utf-8')
                    ]
                    start_response(status, response_headers)
                    html_as_bytes = head.encode('utf-8')
                    html = regOk.format(mes="Вы уже зарегистрированы в рабочем месте")
                    html_as_bytes += html.encode('utf-8')
                    return iter([html_as_bytes])
                else:
                    print("Вы еще не зарегитстрированы.")
                    token = mu.createToken()
                    status = '200'
                    response_headers = [
                        ('Content-type', 'text/html; charset=utf-8')
                    ]
                    start_response(status, response_headers)
                    html_as_bytes = head.encode('utf-8')
                    res1 = f"{res['result']['LAST_NAME']}&nbsp{res['result']['NAME']}"
                    html = BODY.format(ss=res1, token=token, id=res['result']['ID'])
                    html_as_bytes += html.encode('utf-8')
                    re = red.Redis1()
                    re.insertData(token ,res['result']['ID'])
                    print(inParams)

                    pprint(hf.returnb(start_response, environ))
                    return iter([html_as_bytes])
        except:
            print("error")

        # data = b'200 BK OK'
        # status = '200'
        # response_headers = [
        #     ('Content-type', 'text/plain'),
        #     ('Content-Length', str(len(data)))
        # ]
        #
        # return iter([data])

    elif environ["PATH_INFO"] == "/test.php":
        data = b'200 OK'
        status = '200'
        response_headers = [
            ('Content-type', 'text/plain'),
            ('Content-Length', str(len(data)))
        ]
        start_response(status, response_headers)
        print(hf.returnb(start_response, environ))

        return iter([data])

    elif environ["PATH_INFO"] == "/handler.php":
        data = b'200 OK'
        status = '200'
        response_headers = [
            ('Content-type', 'text/plain'),
            ('Content-Length', str(len(data)))
        ]
        start_response(status, response_headers)
        print(hf.returnb(start_response, environ))

        return iter([data])

    elif environ["PATH_INFO"] == "/reg.php":
        print("Я пришел с bk.fa39.ru/reg.php")
        # data = b'200 OK'
        # status = '200'
        # response_headers = [
        #     ('Content-type', 'text/plain'),
        #     ('Content-Length', str(len(data)))
        # ]
        # start_response(status, response_headers)
        # # print(hf.returnb(start_response, environ))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        inParams = hf.allParams(environ)

        re = red.Redis1()
        flag = re.checkKey(inParams['token'])

        if flag:
            mu.addRegData(inParams)
            status = '200'
            now = datetime.datetime.now()
            year1 = datetime.timedelta(365)
            now = now + year1
            token = u.createToken()

            try:
                re1 = red.Redis2()
                re1.insertData(token, inParams['id'])
                db = newFile.Database()
                db.cur.execute(f"insert into const(id_membr, token, type, ip, date) values({inParams['id']}, '{token}',"
                               f" '{environ['HTTP_USER_AGENT']}', '{environ['HTTP_X_REAL_IP']}', '{datetime.datetime.now()}')")
                db.conn.commit()

            except:
                pass

            response_headers = [
                ("Set-Cookie", f"token={token}; SameSite=None; Secure; expires={now}"),
                ('Content-type', 'text/html; charset=utf-8')
            ]
            start_response(status, response_headers)
            html_as_bytes = head.encode('utf-8')
            html = regOk.format(mes="Вы успешно зарегестрированы на локальном рабочем месте.")
            html_as_bytes += html.encode('utf-8')
            return iter([html_as_bytes])
        else:
            status = '200'
            response_headers = [
                ('Content-type', 'text/html; charset=utf-8')
            ]
            start_response(status, response_headers)
            html_as_bytes = head.encode('utf-8')
            html = regOk.format(mes="Что-то пошло не так... Или ваш токен просрочился")
            html_as_bytes += html.encode('utf-8')
            return iter([html_as_bytes])

    else:
        # text = splitParams(environ)
        # flag = checkToken(text)

        data = b'404 Unauthorized'
        status = '404'
        response_headers = [
            ('Content-type', 'text/plain'),
            ('Content-Length', str(len(data)))
        ]
        start_response(status, response_headers)

        print("===================== NEW None =====================")

        # print(returnb(start_response, environ))

        # print(text["token"], " получил")
        # print(token, " мой")

        print("===================== END None =====================")

        return iter([data])
