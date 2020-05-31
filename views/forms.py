"""
  @author Victor I. Afolabi
  
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 27 January, 2018 @ 1:54 AM.
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import redirect, url_for, request, flash, jsonify
from views import app, back
from models import classification as clf


@app.route('/_newsletter', methods=['POST'])
def newsletter_form():
    email = request.form['email']
    flash('Email: {}'.format(email))
    return back.redirect()



@app.route('/_classification')
def classification_form():
    # store request form into a Python dictionary.
    data = dict(request.args)
    algorithm = data.pop('algorithm')[0]  # remove 'name' key

    try:
        # prediction result
        payload = clf.process(data=data, algorithm=algorithm)
    except Exception as e:
        payload = {"error": str(e)}

    return jsonify(payload=payload)


