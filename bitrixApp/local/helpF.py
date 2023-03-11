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
