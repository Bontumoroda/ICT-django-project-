from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .form import CustomerSignUpForm,MaintenanceForm
from .models import *

# Create your views here.

class Customer_registration(SuccessMessageMixin,CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name ='main/Customer_registration.html'
    success_url= reverse_lazy('login')
    success_message = 'Customer successful created please login with your username and password'

def loginpage(request):
        
    if request.method == 'POST':
        username =request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'username or password is incorrect ')

    coontext={}
    return render(request,'main/login_page.html',coontext)
class PostView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'main/index.html'
    context_object_name = 'post'

class ServiceList(LoginRequiredMixin,ListView):
    model = Service
    context_object_name = 'service_list'

class OrderLists(LoginRequiredMixin,ListView):
    model = Order
    context_object_name = 'order'
    template_name = 'main/user.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['order']=context['order'].filter(customer=self.request.user.id)
        context['total_order']=context['order'].filter(customer=self.request.user.id).count()
        context['total_pending']=context['order'].filter(status='pending').count()
        context['total_fixed']=context['order'].filter(status='fixed').count()
        context['total_not_fixed']=context['order'].filter(status='not fixed').count()
        return context


class OrderDeteil(LoginRequiredMixin,DetailView):
    model = Order
    context_object_name = 'order'
    template_name= 'main/order_detail.html'


class CreateOrder(LoginRequiredMixin,CreateView):
    model = Order
    fields = ['service','category','discription','quantity','status']
    template_name= 'main/create_order.html'
    success_url= reverse_lazy('OrderLists')
    def form_valid(self, form):
        form.instance.customer =self.request.user.customer
        return super(CreateOrder,self).form_valid(form)

class OrderUpedate(LoginRequiredMixin,UpdateView):
    model= Order
    fields = ['service','category','discription','quantity','status']
    template_name= 'main/create_order.html'
    success_url= reverse_lazy('OrderLists')
class OrderDelete(LoginRequiredMixin,DeleteView):
    model =Order
    context_object_name = 'order'
    template_name= 'main/delete_order.html'
    success_url= reverse_lazy('OrderLists')

class DeleteCustomerOrder(LoginRequiredMixin,DeleteView):
    model =Order
    context_object_name = 'order'
    template_name= 'main/DeleteCustomerOrder.html'
    success_url= reverse_lazy('OrderList')

@login_required(login_url='login')
def customerorder(request):
    order =Order.objects.all()
    total_order =order.count()
    total_pending =order.filter(status='pending').count()
    total_fixed =order.filter(status='fixed').count()
    total_not_fixed =order.filter(status='not fixed').count()


    context={'order':order,'total_order':total_order,
    'total_pending':total_pending,'total_fixed':total_fixed,
    'total_not_fixed':total_not_fixed}

    return render(request,'main/customerorder.html',context)

    


class MainView(ListView):
    model = Post

    template_name = 'main/base.html'


   
class AboutView(ListView):
    model = Post
    template_name = 'main/About.html'

class ReadAboutView(ListView):
    model = Post
    template_name = 'main/about_red.html'
   




