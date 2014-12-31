from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.views.decorators.http import require_POST

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

    page = resp['page']
    return HttpResponseRedirect(reverse('webfront:page_detail', kwargs={'page_id': page.id}))


@template_view('webfront/page_detail.html')
def page_detail(request, page_id):
    resp = core_api.detail_page(page_id)
    if 'error' in resp:
        raise Http404

    # Getting way to sort for comment list
    form = forms.PageDetailForm(request.GET)
    if not form.is_valid():
        sorted_by = 'top'
    else:
        sorted_by = form.cleaned_data['sorted_by']

    page = resp['page']
    comments = core_api.list_comments(page, sorted_by=sorted_by)

    if request.user.is_authenticated():
        resp = core_api.detail_comment(request.user, page)
        if 'error' in resp:
            user_comment = None
            comment_form = forms.CommentPageForm()
        else:
            user_comment = resp['comment']
            comment_form = None
    else:
        user_comment = None
        comment_form = forms.CommentPageForm()

    return {'page': page,
            'comments': comments,
            'user_comment': user_comment,
            'comment_form': comment_form}


@login_required
@require_POST
def comment_page(request, page_id):
    form = forms.CommentPageForm(request.POST)
    if not form.is_valid():
        # TODO: Leave errors as messages
        return HttpResponseRedirect(reverse('webfront:page_detail', kwargs={'page_id': page_id}))

    core_api.comment_page(
        request.user,
        page_id,
        form.cleaned_data['body'],
    )
    return HttpResponseRedirect(
        '{}?sorted_by=newest'.format(reverse('webfront:page_detail', kwargs={'page_id': page_id}))
    )
