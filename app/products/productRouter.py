from app import app
from flask import render_template, request
from flask_login import login_required
from app.products.productController import ProductController
from app.products.productForm import ProductForm
from app.products.productModel import ProductModel


@app.route('/products')
@login_required
def products():
    page = request.args.get('page', type=int, default=1)
    controller = ProductController()
    product = controller.records(page)
    return render_template('views/products/index.html', title='Productos', data=product)

@app.route('/products/create', methods=['GET', 'POST'])
@login_required
def products_create():
    form = ProductForm()
    if form.validate_on_submit():
        controller = ProductController()
        return controller.create(form)
    return render_template('views/products/forms/create.html', title='Productes - Crear', form=form)

@app.route('/products/update/<int:id>', methods=['GET', 'POST'])
@login_required
def products_update(id):
    product = ProductModel.query.get_or_404(id)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        controller = ProductController()
        return controller.update(form, id)
    return render_template('views/products/forms/update.html', 
                        title='Productes - Actualizar', form=form, product_id=product.id)

@app.route('/products/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def products_delete(id):
    controller = ProductController()
    return controller.delete(id)
