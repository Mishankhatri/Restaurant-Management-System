from django.shortcuts import render
from django.db.models import Q
from django.views.generic.base import TemplateView
from .models import Food ,Invoice
from django.contrib import messages
from crispy_forms.helper import FormHelper
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse
from .forms import  InvoiceFormSet
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import (
    ListView,
    TemplateView,
    CreateView,
    FormView,
    UpdateView,
    DeleteView,
)
from .utils import render_to_pdf




def home(request):
    return render(request,"rms_app/home.html")





#FOOD_VIEWS
class FoodListView(ListView):
    model = Food
    template_name = "rms_app/foodlist.html"  # by default - app/model_viewtype.html
    context_object_name = "food_obj"


class FoodImgView(ListView):
    model = Food
    template_name = "rms_app/food.html"  
    context_object_name = "food_obj"


class AddToListView(LoginRequiredMixin, CreateView):
    model = Food
    fields = ["food_item", "per_price","food_img"]
    template_name = "rms_app/addtolist.html"
    success_url = "/dashboard/addtolist"

    def form_valid(self,form,):
        messages.success(self.request, f'Foodlist updated!')
        return super().form_valid(form)

class UpdateListView(LoginRequiredMixin, UpdateView):
    model = Food
    fields = ["food_item", "per_price","food_img"]
    template_name = "rms_app/addtolist.html"
    success_url = "/food"
    
    def form_valid(self,form):
        messages.success(self.request, f'Foodlist updated!')
        return super().form_valid(form)


class DeleteItemListView(LoginRequiredMixin,DeleteView):
    model = Food
    success_url= '/foodlist'



#INVOICE_VIEWS
class CreateInvoiceView(LoginRequiredMixin, CreateView):
    model = Invoice
    fields = ["customer_name"]
    context_object_name = 'invoice_obj'
    template_name = "rms_app/create_invoice.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'CurrentProfile'

    def form_valid(self,form):
        messages.success(self.request, f'Invoice Created!')
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('add_items_on_invoice', kwargs={'pk': self.object.pk})


class DeleteInvoiceView(LoginRequiredMixin,DeleteView):
    model = Invoice
    success_url = '/dashboard/sales'


class AddItemsToInvoiceView(LoginRequiredMixin,SingleObjectMixin,FormView,TemplateView):
    model = Invoice
    context_object_name = 'invoice_obj'
    template_name = 'rms_app/additemsoninvoice.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Invoice.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Invoice.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return InvoiceFormSet(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )
        return HttpResponseRedirect(self.get_success_url())
          
    def get_success_url(self):
        return reverse('add_items_on_invoice', kwargs={'pk': self.object.pk})


class InvoiceDetailView(LoginRequiredMixin,SingleObjectMixin,TemplateView):

    model = Invoice
    context_object_name = 'invoice_obj'
    template_name = 'rms_app/invoicedetails.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Invoice.objects.all())
        return super().get(request, *args, **kwargs)
          
    def get_success_url(self):
        return reverse('invoice_details', kwargs={'pk': self.object.pk})



class SalesView(LoginRequiredMixin, ListView):
    model = Invoice
    context_object_name = 'invoice_obj'
    template_name = "rms_app/sales.html"

    def get_queryset(self):
        query = self.request.GET.get('q',None)
        query2 = self.request.GET.get('d',None)
        if query is not None :
            invoice_obj = self.model.objects.filter( Q(customer_name__icontains = query) | Q(created_by__username__icontains = query)
            )
        elif query2 is not None :
            invoice_obj = self.model.objects.filter( Q(date_created__year = query2) | Q(date_created__month = query2) | Q(date_created__day = query2)
            )
        else:
            invoice_obj = self.model.objects.all()
        return invoice_obj



class GeneratePdf(View,SingleObjectMixin):
    model = Invoice
    context_object_name = 'invoice_obj'

    def get(self, request, pk, *args, **kwargs):
        self.object = self.get_object(queryset=Invoice.objects.all()) 
        total = 0
        for itr in self.object.invoiceitem.all():
            total += itr.accumulated

        params = {
            'invoice_obj': self.object,
            'request': request,
            'total': total
        }
        pdf = render_to_pdf('rms_app/invoice_print.html', params)
        return HttpResponse(pdf, content_type='application/pdf')



