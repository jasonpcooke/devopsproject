from django.urls import reverse, resolve
from devopsapp.views import index, ticket_by_id



def test_index_url_is_resolved():
    url = reverse('index')
    assert resolve(url).func.__name__ == index.__name__

def test_ticket_by_id_url_is_resolved():
    url = reverse('ticket_by_id', args=[1])
    assert resolve(url).func.__name__ == ticket_by_id.__name__
