from .forms import SearchForm


def common_text(request):
    context = {}
    context['search_form'] = SearchForm
    return context
