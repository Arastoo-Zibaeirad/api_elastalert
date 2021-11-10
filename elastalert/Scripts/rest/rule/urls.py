from django.urls import path
from .views import rule_list, rule_detail, rule_save, rule_update, rule_delete
urlpatterns = [
    path("rule_list", rule_list),
    path("rule_detail/<pk>", rule_detail),
    path("rule_save", rule_save),
    path("rule_update/<pk>", rule_update),
    path("rule_delete/<pk>", rule_delete)
]
