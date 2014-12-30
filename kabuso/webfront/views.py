from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404

from core import api as core_api
from core.views.template import template_view
from webfront import forms


def login(request):
    return auth_views.login(request, template_name='webfront/login.html')


def logout(request):
    return auth_views.logout(request, next_page=reverse('webfront:top'))


@template_view('webfront/top.html')
def top(request):
    return {}


@login_required
@template_view('webfront/read_page.html')
def read_page(request):
    if request.method == 'GET':
        return {'form': forms.ReadPageForm()}

    form = forms.ReadPageForm(request.POST)
    if not form.is_valid():
        return {'form': form}

    url = form.cleaned_data['url']
    resp = core_api.read_page(url, request.user)

    if resp['first_read']:
        # TODO: Leave Congrats message or so
        pass

    if resp['already_read']:
        # TODO: Leave notification message or so
        pass

    page_id = resp['page_id']
    return HttpResponseRedirect(reverse('webfront:page_detail', kwargs={'page_id': page_id}))


@template_view('webfront/page_detail.html')
def page_detail(request, page_id):
    resp = core_api.page_detail(page_id)
    if 'error' in resp:
        raise Http404

    return {'page': resp['page']}
