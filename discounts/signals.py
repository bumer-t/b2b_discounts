# -*- coding: utf-8 -*-


def set_mark_last_period(instance, **kwargs):
    """
    :type  instance: discounts.models.Period
    """
    period = instance.agreement.period_set.all().order_by('-date_end')[0]
    if period and not period.is_last:
        from discounts.models import Period
        Period.objects.filter(is_last=True, agreement=instance.agreement).update(is_last=False)
        period.is_last = True
        period.save()


#todo if use is_last - need add post_delete
