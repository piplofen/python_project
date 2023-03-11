import json, pprint
import urllib.parse, settings as s, requests


def tstst(data):
    data = data.split("&")
    params = {}
    paramsTrue = {}
    for i in range(len(data)):
        data[i] = data[i].split("=")
        params[data[i][0]] = urllib.parse.unquote(data[i][1])
    for item in params.keys():
        itemFalse = params[item]
        item = item.replace("%5B", "[")
        item = item.replace("%5D", "]")
        paramsTrue[item] = itemFalse
    pprint.pprint(paramsTrue)
    return paramsTrue


def splitParams(environ):
    x = environ["QUERY_STRING"]
    print(x, "QUERY_STRING")

    if x == "":
        print("PUSTO")
    else:
        x = x.split("&")
        params = {}
        for i in range(len(x)):
            x[i] = x[i].split("=")
            params[x[i][0]] = urllib.parse.unquote(x[i][1])
        return params


def splitHeaders(environ):
    body = environ['wsgi.input']
    data = body.read()
    newData = data.decode("UTF-8")

    if len(newData) == 0:
        print("ПУСТО")
    else:
        newData = newData.split("&")
        headers = {}
        for i in range(len(newData)):
            newData[i] = newData[i].split("=")
            headers[newData[i][0]] = urllib.parse.unquote(newData[i][1])
        return headers


# 'access_token' : str(params["AUTH_ID"]),
# 'expires_in' : str(params["AUTH_EXPIRES"]),
# 'application_token' : str(params['APP_SID']),
# 'refresh_token' : str(params['REFRESH_ID']),
# 'domain' : str(params['DOMAIN']),
# 'client_endpoint' : f"https://{str(params['DOMAIN'])}/rest/"

def allParams(environ):
    headers = splitHeaders(environ)
    params = splitParams(environ)

    all = {}

    if params == None:
        print("PARAMS ПУСТО")
    else:
        all = params.copy()

    if headers == None:
        print("HEADERS ПУСТО")
    else:
        all.update(headers)

    return all


def returnb(start_response, environ):
    print('-----------------------start---------------------------------')
    # pprint.pprint(start_response)
    body = environ['wsgi.input']
    print('-----------------------body---------------------------------')
    data = body.read()
    data = data.decode("utf-8")
    # da = json.dumps(data)

    print(data)
    # print(tstst(data))
    # tstst(data)
    # splitHeaders(data)
    # print(splitHeaders(data.decode("utf-8")))
    print('--------------------------------------------------------')
    pprint.pprint(environ)
    print('------------------------END--------------------------------')




def getBody(environ):
    data = None
    try:
        body = environ['wsgi.input']
        print('-----------------------body---------------------------------')
        data = body.read()
        data = data.decode("utf-8")
        return data
    except:
        print("except")
        return data


def convertJson(data):
    dict = {}
    data = data[1:]
    data = data[:-1]

    data = data.replace('"', "")
    data = data.replace(' ', '')
    data = data.split(",")
    for item in data:
        item = item.split(":")
        dict[item[0]] = item[1]
    return dict

def getCookies(environ):
    dict = {}
    try:
        cookie = environ["HTTP_COOKIE"]
        cookie = cookie.split(";")
        for item in cookie:
            item = item.split("=")
            dict[item[0]] = item[1]
        return dict
    except:
        return False
    # print(cookie, type(cookie))


def getProfile(environ):
    inParams = allParams(environ)
    auth = inParams["AUTH_ID"]
    url = f"{s.urlForAuth}profile.json?auth={auth}"
    r = requests.get(url)
    res = r.json()
    return res
