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
        'page_id': page.id,
    }


def page_detail(page_id):
    try:
        page = Page.objects.get(id=page_id)
    except Page.DoesNotExist:
        return {'error': {'code': 'not found'}}

    return {
        'page': {
            'page_url': page.page_url,
        }
    }
