from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField('Наименование', max_length=255)
    description = models.TextField('Описание', blank=True, null=True)
    price = models.FloatField('Цена',)
    image = models.ImageField('Изображение', upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField('Продано', default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField('Размер', max_length=4)
    item = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return self.name


class Payment(models.Model):
    type = models.CharField('Тип', max_length=255)

    class Meta:
        ordering = ('type',)
        verbose_name_plural = 'Вид оплаты'

    def __str__(self):
        return self.type


class Order(models.Model):
    item = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    size = models.ForeignKey(Size, verbose_name='Размер', on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=255)
    email = models.EmailField()
    payment = models.ForeignKey(Payment, verbose_name='Вид оплаты', on_delete=models.CASCADE)
    address = models.CharField('Адрес доставки', max_length=255)

    class Meta:
        ordering = ('item',)
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.name
