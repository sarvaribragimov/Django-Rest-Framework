from django.urls import path,include
from .views import AuthorListCreateview,AuthorListview,AuthorDestroyview,AuthorCreateview,AuthorRetrievedestroyview
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r"authors",Authorview)

# urlpatterns = [
#     path('',include(router.urls))
# ]
urlpatterns = [
    path('authors/<pk>/',AuthorRetrievedestroyview.as_view(),name="Authorretrievedestroyview"),
    # path('authors/',AuthorCreateview.as_view(),name="AuthorCreateview"),
    # path('',AuthorListview.as_view(),name="AuthorListview"),
    # path('',AuthorDestroyview.as_view(),name="AuthorDestroyview"),
    path('',AuthorListCreateview.as_view(),name="AuthorListCreateview"),
]
