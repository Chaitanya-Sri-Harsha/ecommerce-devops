from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
cart = []

products = [
    {"id": 1, "name": "T-Shirt", "price": 15},
    {"id": 2, "name": "Sneakers", "price": 55},
    {"id": 3, "name": "Backpack", "price": 40},
]

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return render_template('product.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart.append(product_id)
    return redirect(url_for('cart_view'))

@app.route('/cart')
def cart_view():
    cart_items = [p for p in products if p["id"] in cart]
    return render_template('cart.html', cart=cart_items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
