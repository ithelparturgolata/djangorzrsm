from django.shortcuts import render, get_object_or_404
from .models import Aktualnosci
from .models import Czlonkowie
from django.core.mail import send_mail
from django.http import HttpResponse


def dashboard_rz(request):
    aktualnosci_all = Aktualnosci.objects.all().order_by('tytul')[::-1]
    czlonkowie = Czlonkowie.objects.all().order_by('nazwa')
    latest_news = Aktualnosci.objects.all().order_by('-data_utworzenia')[:1]
    box_news = Aktualnosci.objects.all().order_by('-data_utworzenia')[:3]
    context =\
        {"records_aktualnosci": aktualnosci_all,
         "czlonkowie": czlonkowie,
         'latest_news': latest_news,
         'box_news': box_news
         }

    return render(request, "dashboard.html", context = context)


def aktualnosci_details(request, pk):
    news = get_object_or_404(Aktualnosci, pk=pk)
    return render(request, 'aktualnosci-details.html', {'news': news})


# def dashboard_rz(request):
#     aktualnosci_all= Aktualnosci.objects.all().order_by('-id')[:3]
#     context = {"records_aktualnosci": aktualnosci_all}
#
#     return render(request, "dashboard.html", context=context)


# def aktualnosci(request):
#     aktualnosci_all= Aktualnosci.objects.all().order_by('tytul')[::-1]
#     context = {"records_aktualnosci": aktualnosci_all}
#
#     return render(request, "dashboard.html", context = context)


def czlonkowie_rz(request):
    czlonkowie = Czlonkowie.objects.all().order_by('nazwa')
    context = {"czlonkowie": czlonkowie}

    return render(request, "dashboard.html", context = context)


def czlonkowie_rz_details(request, pk):
    czlonkowie_details = Czlonkowie.objects.get(id=pk)
    context = {"czlonkowie_details": czlonkowie_details}  # Change the key name

    return render(request, "czlonkowie-details.html", context=context)


def send_email(request):
    subject = 'Subject of the email'
    message = 'Body of the email'
    from_email = 'artur.golata@gmail.com'
    recipient_list = ['artur.golata@gmail.com']  # Replace with the recipient's email address

    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse('Dziękujemy za wysłanie wiadomości!')