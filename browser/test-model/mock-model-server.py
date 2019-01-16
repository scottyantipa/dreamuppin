from flask import Flask, request
import math
import random

app = Flask(__name__)

rand_responses = [
    '<div>hello</div',
    '<div>Test 123</div>',
    '<img src="https://www.w3.org/2008/site/images/logo-w3c-mobile-lg" />'
]

@app.route("/", methods=['GET'])
def string_to_html():
    instructions_str = request.args.get('instructions', '')
    res_index = math.floor(random.random() * len(rand_responses))
    rand_res = rand_responses[res_index]
    return rand_res
