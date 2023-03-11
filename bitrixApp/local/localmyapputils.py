import base64
import pprint

import newFile

HTML1 = """<!DOCTYPE html>
<html lang="en">
<head>

    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <link rel="stylesheet" href="main.css" type="text/css"/>
<!--    <script>-->
<!--        $('.message a').click(function(){-->
<!--            $('form').animate({height: "toggle", opacity: "toggle"}, "slow");-->
<!--        });-->
<!--    </script>-->
    <title>Title</title>
</head>
<body>
<div class="login-page">
    <div class="form">
        <form class="register-form">
            <input type="text" placeholder="name"/>
            <input type="password" placeholder="password"/>
            <input type="text" placeholder="email address"/>
            <button>Привязать</button>
            <p class="message">Already registered? <a href="#">Войти</a></p>
        </form>
        <form class="login-form">
            <input type="text" placeholder="Пользовательe"/>
            <input type="password" placeholder="Пароль"/>
            <button>Войти</button>
            <p class="message">Ещё не связанн акунт? <a href="#">Привязать акаунт</a></p>
        </form>
    </div>
</div>
</body>
</html>"""



def checkLoginUser(data):
    id_membr = base64.b64decode(data['id'])
    password_membr = base64.b64decode(data['password'])

    try:
        db = newFile.Database()
        db.cur.execute(f"select password from employees where idbitrix = {int(id_membr)}")
        res = db.cur.fetchall()

        if str(res[0][0]) == str(password_membr.decode("utf8")):
            print("такой чел есть в базе")
            return True
        else:
            print("чела нет в базе")
            return False
    except:
        print("kal")