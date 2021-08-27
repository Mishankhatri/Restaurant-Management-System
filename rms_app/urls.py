from django.urls import path
from . import views
from .views import ( 
    FoodListView,
    AddToListView,
    UpdateListView,
    DeleteItemListView,
    FoodImgView,
    CreateInvoiceView,
    DeleteInvoiceView,
    SalesView,
    AddItemsToInvoiceView,
    InvoiceDetailView,
    GeneratePdf,
    )



urlpatterns = [
    
    #URLS FOR HOME AND FOODITEMS
    path("", views.home, name="rms-home"),
    path("food/", FoodImgView.as_view(), name="rms-food"),
    path("foodlist/", FoodListView.as_view(), name="rms-foodlist"),
    path('dashboard/addtolist',AddToListView.as_view(),name="rms-addtolist"),
    path('foodlist/<int:pk>/delete/',DeleteItemListView.as_view(),name="food_confirm_delete"),
    path('dashboard/addtolist/<int:pk>/update/',UpdateListView.as_view(),name="rms-updatetolist"),

    #URLS FOR INVOICES
    path('dashboard/createinvoice', CreateInvoiceView.as_view(), name='createinvoice'),
    path("dashboard/sales", SalesView.as_view(), name="sales"),
    path("invoices/<int:pk>", AddItemsToInvoiceView.as_view(), name="add_items_on_invoice"),
    path("invoices/<int:pk>/details", InvoiceDetailView.as_view(), name="invoice_details"),
    path('dashboard/sales/<int:pk>/delete/',DeleteInvoiceView.as_view(),name="invoice_confirm_delete"),
    path('invoices/<int:pk>/details/print', GeneratePdf.as_view(), name="invoice_print"),

]
