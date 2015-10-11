# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request
from collections import OrderedDict
import re


app = Flask(__name__)


answer = OrderedDict([
	(16, 'starvation'),
	(16.99, 'emaciation'),
	(18.49, 'underweight'),
	(24.99, 'correct value (healthy weight)'),
	(29.99, 'overweight'),
	(34.99, 'obesity'),
	(39.99, 'clinical obesity'),
	(40, 'extreme obesity'),
])


def get_answer(bmi):
	n = len(answer)

	if bmi < answer.items()[0][0]:
		return answer.items()[0][1]

	if bmi >= answer.items()[n - 1][0]:
		return answer.items()[n - 1][1]

	for key, value in answer.items()[1:n]:
		if bmi <= key:
			return value


def is_field_number(field):
	return True if re.match('\d+\.?\d*',field) else False


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


@app.route('/bmi', methods=['POST'])
def bmi():
	weight = request.form.get('weight')
	height = request.form.get('height')

	if not weight or not height:
		errors = 'Please enter all the fields.'
	else:
		if not is_field_number(weight) or not is_field_number(height):
			errors = 'Please enter valid weight or height. Example 1.6'
		else:
			bmi = float(weight) / float(height) ** 2
			return jsonify(bmi='{0:.2f}'.format(bmi), answer=get_answer(bmi))
	return jsonify(errors=errors)


@app.errorhandler(404)
def page_not_found(error):
	return 'This page does not exist', 404


@app.errorhandler(500)
def houston_we_have_got_a_problem(error):
	return 'Houston, We\'ve Got a Problem ... Uppps ...!? Sorry :)', 500


if __name__ == "__main__":
	app.run()