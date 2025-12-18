from flask import Blueprint, render_template, request, redirect, url_for
from models import Order, User, Product
from datetime import datetime

# Blueprintの作成
graph_bp = Blueprint('graph', __name__, url_prefix='/graph')

@graph_bp.route('/')
def list():
    return render_template('graph_list.html', title='グラフ表示')
