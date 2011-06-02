# coding: utf-8
from django.contrib import admin
from eventos.models import Evento
from datetime import datetime
from django.conf.urls.defaults import patterns
from django.http import HttpResponse
from eventos.forms import EventoForm


class EventoAdmin(admin.ModelAdmin):
    form = EventoForm
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

    def queryset(self, request):
        _queryset = super(EventoAdmin, self).queryset(request)
        _queryset = _queryset.filter(inicio__year=2010)
        return _queryset

    def get_urls(self):
        urls = super(EventoAdmin, self).get_urls()
        _urls = patterns('',
            (r'hello/$', self.hello)
        )
        return _urls + urls

    def hello(self, request):
        return HttpResponse('hello')

admin.site.register(Evento, EventoAdmin)
