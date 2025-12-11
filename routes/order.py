
from flask import Blueprint, render_template, request, redirect, url_for, abort
from models import Order, User, Product
from datetime import datetime

# Blueprintの作成
order_bp = Blueprint('order', __name__, url_prefix='/orders')

@order_bp.route('/')
def list():
    orders = Order.select()
    return render_template('order_list.html', title='テスト結果表示', items=orders)

@order_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['user_id']
        product_id = request.form['product_id']
        type_value = request.form.get('type', '未設定')
        # 数値変換と範囲チェック
        try:
            test_result_value = int(request.form.get('test_result', '0'))
        except ValueError:
            return "テスト結果は数値で入力してください", 400

        if not (0 <= test_result_value <= 100):
            return "テスト結果は0〜100の範囲で入力してください", 400

        order_date = datetime.now()
        Order.create(
            user=user_id,
            product=product_id,
            order_date=order_date,
            type=type_value,
            test_result=test_result_value
        )
        return redirect(url_for('order.list'))

    users = User.select()
    products = Product.select()
    return render_template('order_add.html', users=users, products=products)

@order_bp.route('/edit/<int:order_id>', methods=['GET', 'POST'])
def edit(order_id):
    order = Order.get_or_none(Order.id == order_id)
    if not order:
        return redirect(url_for('order.list'))

    if request.method == 'POST':
        order.user = request.form['user_id']
        order.product = request.form['product_id']
        order.type = request.form.get('type', '未設定')

        try:
            order.test_result = int(request.form.get('test_result', '0'))
        except ValueError:
            return "テスト結果は数値で入力してください", 400

        if not (0 <= order.test_result <= 100):
            return "テスト結果は0〜100の範囲で入力してください", 400

        order.save()
        return redirect(url_for('order.list'))

    users = User.select()
    products = Product.select()
    return render_template('order_edit.html', order=order, users=users, products=products)