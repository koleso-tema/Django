from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter, CharFilter
from .models import Post


# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class NewsFilter(FilterSet):
    dateCreate = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gte',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        )
    )

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'title': ['icontains'],

            'categoryType': ['exact'],
            'author': ['exact'],
            'postCategory': ['exact'],

        }
