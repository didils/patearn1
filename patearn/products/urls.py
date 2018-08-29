from django.conf.urls import url
from . import views

app_name = "products"

urlpatterns = [
    url(
        regex=r'^$',
        view=views.UploadProducts.as_view(),
        name='upload_products'
    )
]
