import django_tables2 as tables
from .models import Person

class MyTable(tables.Table):
    class Meta:
        model = Person
        # Exclude the last column
        exclude = ('history',)
        template_name = 'django_tables2/bootstrap.html'