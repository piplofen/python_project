from pprint import pprint
import helpF as hf, utils as u, settings as s, requests, datetime
from urllib.request import urlopen

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Рабочее место сотрудника</title>
</head>
<body>
	<div id="name">
		{ss}
	</div>
	
</body>
</html>"""

# <div class="ui-entity-editor-block-title"><label class="ui-entity-editor-block-title-text" for="name_text">Имя</label></div>
#         <div class="ui-entity-editor-content-block">
#             <div class="ui-entity-editor-content-block-text">{name}</div>
#         </div>
def kek(environ, start_response):
    inParams = hf.allParams(environ)
    u.writeFile("inParams", "json", "w", inParams)
    pprint(inParams)
    try:
        auth = inParams["AUTH_ID"]
        url = f"{s.urlForAuth}profile.json?auth={auth}"
        r = requests.get(url)
        res = r.json()
        # print(res, 'aksfbasasbfakbfkb')
        ss = f"🤝{res['result']['NAME']}🤝<br>"
    except:
        ss = "💩 Ошибка, что-то случилось 💩"
    now = datetime.datetime.now()
    year1 = datetime.timedelta(365)
    now = now + year1
    status = '200 OK'
    response_headers = [
        ("Set-Cookie", f"member_id={inParams['member_id']}; SameSite=None; Secure; expires={now}"),
        ('Content-type', 'text/html; charset=utf-8')
    ]
    start_response(status, response_headers)
    html = HTML.format(ss=ss)
    html_as_bytes = html.encode('utf-8')
    # print(inParams)

    return html_as_bytes
