import asyncio
from django.utils.decorators import classonlymethod
from django.views.generic import View


class AsyncView(View):

    @classonlymethod
    def as_view(cls, **kwargs):
        view = super().as_view(**kwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view
