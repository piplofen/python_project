import crest, helpF as hf
#>{

JS = """<script>
                    BX24.init(function(){
                        BX24.installFinish();
                    });
                </script>"""

HTML = """<head>
            <script src="//api.bitrix24.com/api/v1/"></script> # ссылка на джава скрипт апи
                {RJS}
            <?php endif;?>
        </head>
        <body>
            {resultas}
        </body>"""

def ikek(environ, start_response):
    global RJS

    data = hf.allParams(environ)

    if "event" in data.keys():
        print(True)
    else:
        event = {
            "event": None,
        }
        data.update(event)

    if "auth" in data.keys():
        print(True)
    else:
        auth = {
            "auth": None,
        }
        data.update(auth)

    cr = crest.Crest().installApp(data)

    if cr['rest_only'] == False:

        if cr['install'] == True:
            RJS = JS

    if cr['install'] == True:
        rrr = "installation has been finished"

    else:
        rrr = "ERROR"

    status = '200 OK'
    response_headers = [
        # Set - Cookie: cookieName = cookieValue;
        ('Content-type', 'text/html; charset=utf-8')
    ]

    start_response(status, response_headers)
    html = HTML.format(RJS=RJS, resultas=rrr)
    html_as_bytes = html.encode('utf-8')

        # print('-----------------------start---------------------------------')
        # pprint(start_response)
        # body = environ['wsgi.input']
        # data = body.read()
        # print(data)
        # print(s)
        # print ('--------------------------------------------------------')
        # pprint(environ)
        # print('------------------------END--------------------------------')
    return [html_as_bytes]