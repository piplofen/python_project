import base64
import pprint

import newFile
from secrets import token_hex

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


def checkUser(data):
    db = newFile.Database()
    db.cur.execute(f"select password from employees where idbitrix = {int(data)}")
    result = db.cur.fetchall()
    print(result)
    for item in result[0]:
        if item is None or item == "":
            print("Пусто")
            return False
    return True


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


def createToken():
    return token_hex(24)


def viewReg():
    print("Окно регистрации")
    addRegData([ID, LOGIN, PASSWORD])


def addRegData(data):
    userDict = {"id": data["id"], "password": data["password"]}
    pprint.pprint(userDict)
    db = newFile.Database()
    db.cur.execute(f"update employees set password = '{userDict['password']}' where idbitrix = {userDict['id']}")
    db.conn.commit()
