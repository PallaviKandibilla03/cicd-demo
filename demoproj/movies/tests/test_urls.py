from django.urls import reverse, resolve

class TestUrls:
    def test_index_url(self):
        path = reverse('movies:index')
        assert resolve(path).view_name == 'movies:index'

    def test_detail_url(self):
        path = reverse('movies:show', kwargs={'movie_id': 1})
        assert resolve(path).view_name == 'movies:show'
