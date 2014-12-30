from core.models import Page, Read


def read_page(url, user):
    try:
        page = Page.objects.get(page_url=url)
        is_first = False
    except Page.DoesNotExist:
        page = Page.objects.create(page_url=url)
        is_first = True

    if Read.objects.filter(page=page, user=user).exists():
        already_read = True
    else:
        already_read = False
        Read.objects.create(page=page, user=user)

    return {
        'first_read': is_first,
        'already_read': already_read,
        'page': page,
    }


def page_detail(page_id):
    try:
        page = Page.objects.get(id=page_id)
    except Page.DoesNotExist:
        return {'error': {'code': 'not found'}}

    return {
        'page': page,
    }


def list_comments(page, sorted_by='top'):
    comments = page.comments
    if sorted_by == 'newest':
        return comments.order_by('-created_at')
    else:
        return comments.order_by('-point')
