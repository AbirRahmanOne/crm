import django_filters

from django_filters import DateFilter, CharFilter

from .models import *


class OrderFilter(django_filters.FilterSet):
    startDate = DateFilter(field_name='date_created', lookup_expr='gte')
    endDate = DateFilter(field_name='date_created', lookup_expr='lte')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
