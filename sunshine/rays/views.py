# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint('rays', __name__, url_prefix='/rays', static_folder='../static')


@blueprint.route('/')
@login_required
def stations():
    """List stations."""
    return render_template('rays/stations.html')

@blueprint.route('/observations')
@login_required
def observations():
    """List stations."""
    return render_template('rays/observations.html')
