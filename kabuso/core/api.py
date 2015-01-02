from django.db import transaction

from core.models import Page, Read, Comment
from core.page import request_page


def read_page_url(url, user):
    try:
        page = Page.objects.get(page_url=url)
        is_first = False
    except Page.DoesNotExist:
        page_info = request_page(url)
        page = Page.objects.create(
            page_url=url,
            title=page_info['title'],
            summary_image_url=page_info['summary_image_url'],
            description=page_info['description'],
        )
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


def is_read_page(user, page):
    return {
        'is_read': Read.objects.filter(page=page, user=user).exists(),
    }


def detail_page(page_id):
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


def detail_comment(user, page):
    try:
        comment = Comment.objects.get(user=user, page=page)
    except Comment.DoesNotExist:
        return {'error': {'code': 'not found'}}

    return {
        'comment': comment
    }


@transaction.atomic()
def comment_page(user, page_id, body):
    comment = Comment.objects.create(
        user=user,
        page_id=page_id,
        body=body,
    )

    if not Read.objects.filter(user=user, page_id=page_id):
        Read.objects.create(user=user, page_id=page_id)

    return {
        'comment': comment,
    }


def read_page(user, page_id):
    if Read.objects.filter(user=user, page_id=page_id).exists():
        return {'error': {'code': 'existed'}}
    read = Read.objects.create(user=user, page_id=page_id)
    return {'read': read}
