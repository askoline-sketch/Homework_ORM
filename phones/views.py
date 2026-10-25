from django.shortcuts import render, get_object_or_404

from phones.models import Phone


def catalog(request):
    sort_param = request.GET.get('sort')
    phones = Phone.objects.all()

    if sort_param == 'name':
        phones = phones.order_by('name')
    elif sort_param == 'min_price':
        phones = phones.order_by('price')
    elif sort_param == 'max_price':
        phones = phones.order_by('-price')

    context = {
        'phones': phones,
        'sort': sort_param,
    }

    return render(request, 'catalog.html', context)


def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)

    context = {
        'phone': phone,
    }

    return render(request, 'phone_detail.html', context)
