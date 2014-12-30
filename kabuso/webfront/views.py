from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from core import api as core_api
from core.views.template import template_view
from webfront import forms


@template_view('webfront/read_page.html')
def read_page(request):
    if request.method == 'GET':
        return {'form': forms.ReadPageForm()}

    form = forms.ReadPageForm(request.POST)
    if not form.is_valid():
        return {'form': form}

    url = form.cleaned_data['url']
    resp = core_api.read_page(url)

    if resp['first_read']:
        # TODO: Leave Congrats message or so
        pass

    page_id = resp['page_id']
    return HttpResponseRedirect(reverse('webfront:page_detail', kwargs={'page_id': page_id}))


@template_view('webfront/page_detail.html')
def page_detail(request, page_id):
    resp = core_api.page_detail(page_id)
    return {'page': resp['page']}
