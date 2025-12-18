import matplotlib
import japanize_matplotlib
matplotlib.use('Agg')  # ★ Mac + Flask 必須

from flask import Blueprint, render_template, request, Response
from models import Order, User, Product
import matplotlib.pyplot as plt
import io

graph_bp = Blueprint('graph', __name__, url_prefix='/graph')


@graph_bp.route('/')
def list():
    return render_template('graph_list.html', title='グラフ表示')


@graph_bp.route('/histogram')
def histogram():
    grade = request.args.get('grade')       # 学年
    subject = request.args.get('subject')   # 科目

    query = (
        Order
        .select(Order, User, Product)
        .join(User)
        .switch(Order)
        .join(Product)
    )

    if grade:
        query = query.where(User.age == int(grade))

    if subject:
        query = query.where(Product.name == subject)

    scores = [o.test_result for o in query if o.test_result > 0]

    if not scores:
        scores = [0]

    # ヒストグラム作成
    plt.figure(figsize=(8, 5))
    plt.hist(scores, bins=10)
    plt.xlabel('点数')
    plt.ylabel('人数')

    title = '点数分布'
    if grade:
        title += f'（{grade}年）'
    if subject:
        title += f'（{subject}）'

    plt.title(title)

    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)

    return Response(buf.getvalue(), mimetype='image/png')
