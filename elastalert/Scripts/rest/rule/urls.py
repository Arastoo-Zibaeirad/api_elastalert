from django.db import router
from django.urls import path
from django.urls.conf import include
from .views import query_total, query_total_detail #RuleList
# , rule_list, rule_detail, rule_save, rule_update, rule_delete

# from rest_framework.routers import DefaultRouter
# from .views import RuleViewSets


# router = DefaultRouter()
# router.register(r'rule', RuleViewSets, basename='rule')
# urlpatterns = router.urls

urlpatterns = [
    # path("rule_list", rule_list),
    # path("rule_detail/<pk>", rule_detail),
    # path("rule_save", rule_save),
    # path("rule_update/<pk>", rule_update),
    # path("rule_delete/<pk>", rule_delete),




    # path("rulelist/", RuleList.as_view()),
      
    # path("", include(router.urls)),




    path("query/", query_total),
    path("detail/<int:pk>/", query_total_detail),
    




]
