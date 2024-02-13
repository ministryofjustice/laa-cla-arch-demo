"""drf_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from models import Case

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response


# Serializers define the API representation.
class CaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Case
        fields = ('name',)

# ViewSets define the view behavior.
class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    def create(self, request, *kargs, **kwargs):
        # Create a new case object using the request data
        import pdb; pdb.set_trace()
        case = self.queryset.create(request.data)

        # Serialize the newly created case and return it in the response
        serializer = CaseSerializer(case)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    ### equivalent from ClaModelSerializer
    # def create(self, validated_data):
    #     self.create_update_writable_nested_fields_one_to_one(None, validated_data)
    #     model = self.Meta.model
    #     m2m_validated_data = self.filter_validated_data_m2m(validated_data)
    #     instance = model.objects.create(**validated_data)
    #     self.create_writable_nested_fields_many_to_many(instance, m2m_validated_data)
    #     return instance



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'case', CaseViewSet, base_name='case')

# Wire up our API using automatic URL routing.
# Additionally, we include 
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    # login URLs for the browsable API.
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]