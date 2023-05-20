from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import json

from app.db import get_db

bp = Blueprint('events', __name__)

@bp.get('/')
def index():
    db = get_db()
    rows = db.execute(
        'SELECT * FROM events'
    ).fetchall()
    db.close()
    posts = [dict(row) for row in rows]
    return posts


@bp.post('/events')
def create():
    if request.method == 'POST':
        params = request.get_json()
        events = params.get('events')
        error = None

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO events (data)'
                ' VALUES (?)',
                (events,)
            )
            db.commit()
            db.close()
    return "event post successfully"