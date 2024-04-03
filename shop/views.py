from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .forms import SignupForm, NewProductForm, UsersMessageForm, UsersOrder
from .models import Product, Order, Message
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def login_user(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm

    return render(request, 'signup.html', {
        'form': form
    })


def logout_user(request):
    logout(request)
    return redirect('index')


def products(request):
    items = Product.objects.filter(is_sold=False)[0:6]
    return render(request, 'products.html', {
        'items': items,
    })


@login_required()
def contact(request):
    if request.method == 'POST':
        form = UsersMessageForm(request.POST)

        if form.is_valid():
            messages = form.save(commit=False)
            messages.save()

            return redirect('index')
    else:
        form = UsersMessageForm()

    return render(request, 'contacts.html', {
        'form': form
    })


@login_required()
def create(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('create')
    else:
        form = NewProductForm()

    return render(request, 'create.html', {
        'form': form
    })


@login_required()
def detail(request, pk):
    item = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = UsersOrder(request.POST)

        if form.is_valid():
            orders = form.save(commit=False)
            orders.created_by = request.user
            orders.save()

            return redirect('products')
    else:
        form = UsersOrder()

    return render(request, 'product.html', {
        'item': item,
        'form': form
    })


def order(request):
    orders = Order.objects.all()

    return render(request, 'orders.html', {
        'orders': orders,
    })


def message(request):
    messages = Message.objects.all()

    return render(request, 'message.html', {
        'messages': messages,
    })
