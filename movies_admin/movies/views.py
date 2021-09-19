# Review Response (TODO: delete afterwards)
# Традиционным местом размещения views является корень приложения, это именно
# то место, где ожидаешь его увидеть. При необходимости можно сделать из views.py
# пакет views, а подкатегории в виде отдельных файлов: api.py, base.py и т.д.
# Вынос views во вложенные структуры не представляется целесообразным.
from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from movies.models import Movies
from movies.api.v1.serializers import MoviesSerializer


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'prev': self.page.previous_page_number() if self.page.number > 1
            else None,
            'next': self.page.next_page_number()
            if self.page.number < self.page.paginator.num_pages else None,
            'result': data,
        })


class MoviesViewSet(ReadOnlyModelViewSet):
    queryset = Movies.objects.prefetch_related('movie_genres')
    # Review response (TODO: delete afterwards)
    # В сериализаторе не указано больше связанных полей, чем описано в
    # prefetch_related, поскольку поля 'writers', 'directors', 'actors'
    # не являются связанными полями. Эти поля вычисляемые и prefetch_relates с
    # ними не работает.
    serializer_class = MoviesSerializer
    pagination_class = CustomPagination
# Review response (TODO: delete afterwards)
# Вероятно используются некорректные тесты, предоставленные изначально к проекту.
# Найдены следующие ошибки: а) отсутствие округления при делении страниц, поэтому
# в тесте, например, ожидается по полю 19.98 страниц; б) схема теста не соответствует
# техническому заданию из openAPI, например, затребуется results вместо result;
# в) в тесте на вторую страницу ожидается значение null как номер предыдущей
# страницы, что очевидно неверно; г) некорректное использование экранирование
# в функции задания переменной окружения movieUuid. В корне проекта размещены
# корректный вариант теста postman_tests.json. В представленном виде проект
# проходит все тесты, если они составлены корректно.
