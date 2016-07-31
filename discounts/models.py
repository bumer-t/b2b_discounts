# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError

from discounts.consts.status import STATUS_PERIOD
from discounts.signals import set_mark_last_period


class PeriodDate(models.Model):
    date_start  = models.DateField(u'Дата начала')
    date_end    = models.DateField(u'Дата окончания')

    class Meta:
        abstract = True

    def validate_date(self):
        if self.date_start > self.date_end:
            raise ValidationError(u'Дата начала не может быть старше даты окончания')


class DateCreatedChanged(models.Model):
    created = models.DateTimeField(u'Дата создания',  auto_now_add=True)
    changed = models.DateTimeField(u'Дата модификации',  auto_now=True)

    class Meta:
        abstract = True


class Country(DateCreatedChanged):
    code = models.CharField(u'Код iso', max_length=3, db_index=True, unique=True)
    name = models.CharField(u'Название', max_length=80, help_text=u'название страны', unique=True)

    def __unicode__(self):
        return unicode(self.code)

    class Meta:
        verbose_name_plural = 'Country'


class Company(DateCreatedChanged):
    name    = models.CharField(u'Название', max_length=80, help_text=u'название компании')
    country = models.ForeignKey(Country)

    class Meta:
        unique_together     = (('name', 'country'),)
        verbose_name_plural = 'Company'

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

    def __validate_custom(self):
        self.validate_date()

    def clean(self):
        self.__validate_custom()

    def save(self, *args, **kwargs):
        self.__validate_custom()
        super(Agreement, self).save(*args, **kwargs)


class Period(PeriodDate, DateCreatedChanged):
    agreement   = models.ForeignKey(Agreement)
    status      = models.PositiveSmallIntegerField(u'статус', choices=STATUS_PERIOD, help_text=u'состояние периода')
    is_last     = models.BooleanField(default=False, blank=True)

    def __unicode__(self):
        return u'%s:%s|%s__%s' % (self.agreement, self.status, self.date_start, self.date_end)

    def __is_validate_period(self, period):
        if self.date_start > period.date_start and self.date_end > period.date_start and self.date_end > period.date_end:
            return True
        if self.date_start < period.date_start and self.date_end < period.date_start and self.date_end < period.date_end:
            return True
        return False

    def __validate_custom(self):
        self.validate_date()
        if self.agreement.date_start > self.date_start:
            raise ValidationError(u'Дата начала периода старше даты начала соглашения %s' % self.agreement.date_start)
        if  self.date_end > self.agreement.date_end:
            raise ValidationError(u'Дата окончания периода старше даты окончания соглашения %s' % self.agreement.date_end)
        periods = self.agreement.period_set.exclude(id=self.id) if self.id else self.agreement.period_set.all()
        for period in periods:
            if not self.__is_validate_period(period=period):
                raise ValidationError(u'Пересекаются периоды %s' % period)

    def clean(self):
        self.__validate_custom()

    def save(self, *args, **kwargs):
        self.__validate_custom()
        super(Period, self).save(*args, **kwargs)


models.signals.post_save.connect(set_mark_last_period, sender=Period)
