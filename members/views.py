from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Member


class IndexView(generic.ListView):
    template_name = 'members/index.html'
    context_object_name = 'all_active_member_list'

    def get_queryset(self):
        # filter of is_active=True
