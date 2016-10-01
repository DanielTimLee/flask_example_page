from flask import Flask, render_template, request, make_response
from random import randrange as rr
import sys
app=Flask(__name__)

@app.route('/')
def cookie():
    i = request.cookies.get('count')
    color = ['red','orange','yellow','green','teal','blue','purple','pink']
    size = ['mini','tiny','small','','large','huge']
    icon = ['frown','heart','meh','smile','star half','star']
    style = color[rr(0,8)] + ' '+ size[rr(0,6)]
    if not i:
        i = 1
    else:
        i = int(i)
        i += 1
    resp = make_response(render_template('index.html',icon=icon[rr(0,6)],style=style))
    resp.set_cookie('count',str(i))
    return resp

app.run(port=int(sys.argv[1]),host='0.0.0.0',debug=True)
