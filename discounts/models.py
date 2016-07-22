# -*- coding: utf-8 -*-
import datetime as dt

from django.contrib.auth.models import User
from django.db import models

from discounts.consts.status import STATUS_PERIOD


class PeriodDate(models.Model):
    date_start  = models.DateField(u'Дата начала')
    date_end    = models.DateField(u'Дата окончания')

    class Meta:
        abstract = True


class DateCreatedChanged(models.Model):
    created = models.DateTimeField(u'Дата создания', auto_now_add=True, null=True, default=dt.datetime.now())
    changed = models.DateTimeField(u'Дата модификации', auto_now=True, null=True)

    class Meta:
        abstract = True


class Country(DateCreatedChanged):
    id   = models.CharField(u'Код iso', max_length=3, primary_key=True, db_index=True, unique=True)
    name = models.CharField(u'Название', max_length=80, help_text=u'название страны')

    def __unicode__(self):
        return unicode(self.id)


class Company(DateCreatedChanged):
    name    = models.CharField(u'Название', max_length=80, help_text=u'название компании')
    country = models.ForeignKey(Country)

    class Meta:
        unique_together = (('name', 'country'),)

    def __unicode__(self):
        return unicode(self.name)


class Negotiator(User):
    comment = models.TextField(u'Комментарий', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Negotiator'


class Agreement(PeriodDate, DateCreatedChanged):
    company         = models.ForeignKey(Company)
    negotiator      = models.ForeignKey(Negotiator)
    export_turnover = models.FloatField(u'Экспорт', default=0, blank=True, help_text=u'Оборот по кредиту')
    import_turnover = models.FloatField(u'Импорт', default=0, blank=True, help_text=u'Оборот по дебиту')

    class Meta:
        unique_together = (('company', 'date_start', 'date_end'),)

    def __unicode__(self):
        return u'%s|%s__%s' % (self.company, self.date_start, self.date_end)


class Period(PeriodDate, DateCreatedChanged):
    agreement   = models.ForeignKey(Agreement)
    status      = models.CharField(u'Провайдер', max_length=10, choices=STATUS_PERIOD)
