from django.db import models
import uuid
import os


# Create your models here.
class Hero(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/hero/', filename)

    hero_name = models.CharField(max_length=50, verbose_name="Name")
    hero_about = models.TextField(max_length=100, verbose_name="About")
    hero_image = models.ImageField(upload_to=get_file_name, verbose_name="Photo")
    hero_access = models.BooleanField(default=True, verbose_name="Acces")


class Feature(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/feature/', filename)

    feature_position = models.SmallIntegerField()
    feature_title = models.CharField(max_length=50, verbose_name="Title")
    feature_about = models.TextField(max_length=200, verbose_name="About")
    feature_image = models.ImageField(upload_to=get_file_name, verbose_name="Photo")

    def __str__(self):
        return f'{self.feature_title} {self.feature_position}'

    class Meta:
        verbose_name = 'Feature'
        ordering = ('feature_position',)


class About(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/about/', filename)

    about_title = models.CharField(max_length=50, verbose_name="Title")
    about_subtitle = models.TextField(max_length=200, verbose_name="Subtitle")
    about_text = models.TextField(max_length=500, verbose_name="Text")
    about_image = models.ImageField(upload_to=get_file_name, verbose_name="Photo")
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.about_title}'

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Classes(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/classes/', filename)

    classes_position = models.SmallIntegerField()
    classes_title = models.CharField(max_length=50, verbose_name="Title")
    classes_about = models.TextField(max_length=250, verbose_name="About")
    classes_image = models.ImageField(upload_to=get_file_name, verbose_name="Image")

    def __str__(self):
        return f'{self.classes_title} {self.classes_position}'

    class Meta:
        verbose_name = 'Classes'
        ordering = ('classes_position',)


class Plan(models.Model):

    plan_position = models.SmallIntegerField()
    plan_title = models.CharField(max_length=50, verbose_name="Title")
    plan_price = models.PositiveIntegerField(verbose_name="Plan price")
    plan_list1 = models.CharField(max_length=100, verbose_name="Lst1")
    plan_list2 = models.CharField(max_length=100, verbose_name="Lst2", blank=True)
    plan_list3 = models.CharField(max_length=100, verbose_name="Lst3", blank=True)
    plan_list4 = models.CharField(max_length=100, verbose_name="Lst4", blank=True)
    plan_list5 = models.CharField(max_length=100, verbose_name="Lst5", blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.plan_title}'

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'
        ordering = ('plan_position',)


class Whyus(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/whyus/', filename)

    why_position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    why_icon = models.ImageField(upload_to=get_file_name, verbose_name="Icon")
    why_title = models.CharField(max_length=50, verbose_name="Title")
    why_about = models.TextField(max_length=250, verbose_name="About")

    def __str__(self):
        return f'{self.why_title}'

    class Meta:
        verbose_name = 'Why us'
        verbose_name_plural = 'Why us'
        ordering = ('why_position',)
