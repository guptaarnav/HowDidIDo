import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from scipy.stats import norm

from .forms import TestInfoForm

bp = Blueprint('index', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    form = TestInfoForm()
    if form.validate_on_submit():
        avg = float(form.avg.data)
        std = float(form.std.data)
        score = float(form.score.data)
        
        perc = norm.ppf(score, loc=avg, scale=std)
        data = {"avg": avg, "std": std, "score": score, "perc": perc}

        return render_template("answer.html", data=data)
    else:
        #GET request
        return render_template("index.html", form=form)
    
def answer():
    return render_template('answer.html')