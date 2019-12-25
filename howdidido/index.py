import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from scipy.stats import norm


bp = Blueprint('index', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        string_avg = request.form['avg']
        string_std = request.form['std']
        string_score = request.form['score']
        try:
            avg = float(string_avg)
            std = float(string_avg)
            score = float(string_score)
        except:
            flash("invalid input")
            render_template("index.html")
        
        perc = norm.ppf(score, loc=avg, scale=std)
        data = {"avg": avg, "std": std, "score": score, "perc": perc}

        render_template("answer.html", data=data)
    else:
        #GET request
        return render_template("index.html")
    