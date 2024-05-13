from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingFormField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField

class Aktualnosci(models.Model):
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    tytul = models.CharField(max_length=255)
    opis = RichTextUploadingField(max_length=90000)
    grafika = models.ImageField(upload_to='news/', blank=True, null=True)
    # obraz = RichTextUploadingField(blank=True, null=True)

    
    def __str__(self):
        return self.tytul
    

class Czlonkowie(models.Model):
    nazwa = models.CharField(max_length=255)
    miasto = models.CharField(max_length=255)
    ulica = models.CharField(max_length=255)
    kod = models.CharField(max_length=10, blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    strona = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    poniedzialek = models.CharField(max_length=100, blank=True, null=True)
    wtorek = models.CharField(max_length=100, blank=True, null=True)
    sroda = models.CharField(max_length=100, blank=True, null=True)
    czwartek = models.CharField(max_length=100, blank=True, null=True)
    piatek = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to='logo_www/', blank=True, null=True)
    baner = models.ImageField(upload_to='logo_www/', blank=True, null=True)
    
    def __str__(self):
        return self.nazwa
    
    