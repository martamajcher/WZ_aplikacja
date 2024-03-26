
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


from datetime import date  # Importuj date z modułu datetime

class Moje_wz(models.Model):
    name = models.CharField(max_length=200)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    Odbiorca = models.CharField(max_length=200, default="")
    Numer_samochodu = models.CharField(max_length=200, default="Transport własny")
    Data_dokumentu = models.DateField(default=date.today)  # Ustawienie domyślnej wartości na aktualną datę
    Nazwa_produktu=models.CharField(max_length=300, default="")
    Numer_produktu=models.CharField(max_length=300,default="")
    Ilosc=models.IntegerField(default=0)

    def __str__(self):
        return (f"{self.Data_dokumentu} - Odbiorca: {self.Odbiorca}, Numer samochodu: {self.Numer_samochodu},Nazwa produktu: {
        self.Nazwa_produktu},Numer_produktu:{self.Numer_produktu},Ilosc:{self.Ilosc}")

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.Data_dokumentu}-{self.Odbiorca}-{self.Numer_samochodu}-{self.Nazwa_produktu}-{self.Numer_produktu}-{self.Ilosc}")
        super().save(*args, **kwargs)


    def __str__(self):
        return self.Data_dokumentu

    def learn_url(self):
        return reverse("wz-learn", args=[self.slug])

class UserWzOwnership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    w = models.ForeignKey(Moje_wz, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} -> {self.w.Data_dokumentu}"



