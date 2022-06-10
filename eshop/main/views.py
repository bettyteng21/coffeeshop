from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from . import forms
from django.http import JsonResponse
import json

def index(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items=[]
		order = {'get_cart_total':0, 'get_cart_items':0}
		cartItems = order['get_cart_items']


	if request.method == 'POST':
		order = request.POST.get('order')
		if order== "Order by name":
			beans = Beans.objects.all().order_by('name')
		elif order== "Order by roast":
			beans = Beans.objects.all().order_by('roast')
		else:
			beans = Beans.objects.all().order_by('flavor_detail')
	else:
		beans = Beans.objects.all()
		# messages.add_message(request, messages.WARNING, "not received")
	return render(request, "shop/index.html", locals())

def cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items=[]
		order = {'get_cart_total':0, 'get_cart_items':0}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems': cartItems}
	return render(request, 'shop/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items=[]
		order = {'get_cart_total':0, 'get_cart_items':0}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems': cartItems}
	return render(request, 'shop/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Beans.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()
	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def bean_detail(request, beanno=0):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items=[]
		order = {'get_cart_total':0, 'get_cart_items':0}
		cartItems = order['get_cart_items']
	

	if beanno==0:
		return redirect('/')
		
	beans = Beans.objects.get(id=beanno)
	return render(request, "shop/bean_detail.html", locals())


# uses session to send the choosen roast
def roast(request):
	not_last = "/flavor/" #not the last page of the questionnaire 
	if request.method == 'POST':
		form = forms.RoastForm(request.POST)
		if form.is_valid():
			# messages.add_message(request, messages.WARNING, "send roast_form success")
			roast = request.POST['roast']
			selected_beans = Beans.objects.filter(roast=roast)
	else:
		form = forms.RoastForm()

	try:
		# put '#' in session when there's no value in roast, else session==roast
		request.session['roast'] = '#'
		if roast:
			# messages.add_message(request, messages.WARNING, "has roast")
			request.session['roast'] = roast
	except:
		pass
	return render(request, "shop/form.html", locals())


# uses session to send the choosen flavor
def flavor(request):
	not_last = "/flavor_detail/" #not the last page of the questionnaire 
	if request.method == 'POST':
		form = forms.FlavorForm(request.POST)
		if form.is_valid():
			# messages.add_message(request, messages.WARNING, "send roast_form success")
			flavor = request.POST['flavor']
			roast = request.session['roast']
			if roast == '#':
				# there isn't any input from the previous pages
				# messages.add_message(request, messages.WARNING, "no roast")
				selected_beans = Beans.objects.filter(flavor=flavor)
			else:
				# messages.add_message(request, messages.WARNING, "has roast")
				selected_beans = Beans.objects.filter(roast=roast, flavor=flavor)
	else:
		form = forms.FlavorForm()

	try:
		# put '#' in session when there's no value in flavor, else session==flavor
		request.session['flavor'] = '#'
		if flavor:
			request.session['flavor'] = flavor
	except:
		pass
	return render(request, "shop/form.html", locals())


# uses session to send the choosen flavor_detail
def flavor_detail(request):
	not_last = "" #the last page of the questionnaire 
	roast = request.session['roast']
	flavor = request.session['flavor']
	if request.method == 'POST':
		if flavor=='Berry':
			form = forms.FlavorBerryForm(request.POST)
		elif flavor=='Flower':
			form = forms.FlavorFlowerForm(request.POST)
		elif flavor=='Wood':
			form = forms.FlavorWoodForm(request.POST)
		else:
			form = forms.FlavorDetailForm(request.POST)

		if form.is_valid():
			# messages.add_message(request, messages.WARNING, "send roast_form success")
			roast = request.session['roast']
			flavor = request.session['flavor']
			flavor_detail = request.POST['flavor_detail']
			if roast == '#' or flavor=='#':
				# there isn't any input from the previous pages
				# messages.add_message(request, messages.WARNING, "no roast or flavor")
				if roast=='#' and flavor=='#':
					selected_beans = Beans.objects.filter(flavor_detail=flavor_detail)
				elif roast=='#':
					selected_beans = Beans.objects.filter(flavor=flavor, flavor_detail=flavor_detail)
				else:
					selected_beans = Beans.objects.filter(roast=roast, flavor_detail=flavor_detail)
			else:
				# messages.add_message(request, messages.WARNING, "has roast")
				selected_beans = Beans.objects.filter(roast=roast, flavor=flavor, flavor_detail=flavor_detail)
	else:
		if flavor=='Berry':
			form = forms.FlavorBerryForm()
		elif flavor=='Flower':
			form = forms.FlavorFlowerForm()
		elif flavor=='Wood':
			form = forms.FlavorWoodForm()
		else:
			form = forms.FlavorDetailForm()
		messages.add_message(request, messages.INFO, "Checkbox cannot be empty.")

	try:
		# put '#' in session when there's no value in flavor_detail, else session==flavor_detail
		request.session['flavor_detail'] = '#'
		if flavor:
			request.session['flavor_detail'] = flavor_detail
	except:
		pass
	return render(request, "shop/form.html", locals())






