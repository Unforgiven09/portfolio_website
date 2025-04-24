from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pc_builder_index'),
    path('part-info-update/<int:product_id>', views.part_info_update, name='part_info_update'),
]