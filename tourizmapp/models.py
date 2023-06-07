from django.db import models


class Citys(models.Model):
    name = models.CharField('Қала аты', max_length=100, blank=True)
    text = models.CharField('Текс', max_length=500, blank=True)
    text_ru = models.CharField('Текс', max_length=500, blank=True,null=True)
    text_en = models.CharField('Текс', max_length=500, blank=True,null=True)
    img = models.CharField('Суреті', max_length=300, blank=True)
    descriptions = models.TextField('Толық текст', blank=True, default='text')
    descriptions_ru = models.TextField('Толық текст', blank=True, default='text')
    descriptions_en = models.TextField('Толық текст', blank=True, default='text')
    img_1 = models.CharField('Суреті_1', max_length=300, blank=True, default='text')
    descriptions_1 = models.TextField('Тур текст', blank=True, default='text')
    descriptions_1_ru = models.TextField('Тур текст', blank=True, default='text')
    descriptions_1_en = models.TextField('Тур текст', blank=True, default='text')
    map = models.CharField('Карта', max_length=500, blank=True, default='text')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Қала'
        verbose_name_plural = 'Қалалар'


class Hotel(models.Model):
    name = models.CharField('Отель аты', max_length=100, blank=True)
    city = models.CharField('Қала аты', max_length=100, blank=True)
    text = models.CharField('Текс', max_length=500, blank=True)
    img = models.CharField('Суреті', max_length=300, blank=True)
    price = models.CharField('Бағасы теңгемен', max_length=100, blank=True)
    price_usd = models.CharField('Бағасы доллармен', max_length=100, blank=True)
    price_rus = models.CharField('Бағасы рубльмен', max_length=100, blank=True)
    price_eur = models.CharField('Бағасы евромен', max_length=100, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Қонақ үй'
        verbose_name_plural = 'Қонақ үйлер'


class Requests(models.Model):
    name = models.CharField('Аты-жөні', max_length=100)
    phone_number = models.CharField('Номер', max_length=100)
    hotel = models.CharField('Қонақ үй', max_length=100)
    child = models.IntegerField('Балалар саны')
    adult = models.IntegerField('Ересек саны')
    date1 = models.DateField('Алу куны')
    date2 = models.DateField('Откізу күні')

    def __str__(self):
        return f"{self.name}"

    cardholder_name = models.CharField('Карта иесі', max_length=100, blank=True, default='Admin test')
    card_number = models.CharField('Карта номері', max_length=100, blank=True, default='456789654321')
    expiration_date = models.CharField('Жарамдылық мерзімі', max_length=100, blank=True, default='12/24')
    cvc = models.CharField('CVC код', max_length=100, blank=True, default='456')

    class Meta:
        verbose_name = 'Сұраныс'
        verbose_name_plural = 'Сұраныстар'


class Message(models.Model):
    name = models.CharField('Аты', max_length=100)
    email = models.CharField('Email', max_length=100)
    text = models.CharField('Текс', max_length=100)
    subject = models.CharField('Тақырыбы', max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Хабарлама'
        verbose_name_plural = 'Хабарламалар'


class TourObjects(models.Model):
    name = models.CharField('Аты', max_length=150)
    image = models.ImageField(upload_to='imageshots/', null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Туробъекті'
        verbose_name_plural = 'Туробъектілер'


class ObjectsDetail(models.Model):
    name = models.CharField('Аты', max_length=150)
    name_ru = models.CharField('Аты', max_length=150,null=True)
    name_en = models.CharField('Аты', max_length=150,null=True)
    tourobjects = models.ForeignKey(TourObjects, verbose_name='Туробъекті', on_delete=models.CASCADE)
    description = models.TextField('Сипаттама')
    description_ru = models.TextField('Сипаттама',null=True)
    description_en = models.TextField('Сипаттама',null=True)
    map = models.CharField('Орналасқан жері', max_length=150)
    map_in_google = models.TextField('Картада', null=True)
    image = models.ImageField(upload_to='imageshots/', null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Туробъекті туралы'
        verbose_name_plural = 'Туробъектілер туралы'


class Guide(models.Model):
    first_name = models.CharField('Есімі', max_length=150)
    last_name = models.CharField('Тегі', max_length=150)
    city = models.CharField('Қала', max_length=150)
    language = models.CharField('Тіл', max_length=150)
    image = models.ImageField(upload_to='guides/')
    experience = models.IntegerField('Тәжірибе')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Гид'
        verbose_name_plural = 'Гидтер'
