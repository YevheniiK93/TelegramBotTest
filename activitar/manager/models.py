from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class UserSubmit(models.Model):
    mobile_re = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4,9}$', message='Wrong phone number')
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, validators=[mobile_re])
    message = models.TextField(max_length=300)

    is_processed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Neta:
        ordering = ('date',)

    def __str__(self):
        return f"Submit closed: {self.is_processed}! {self.name}: {self.phone}: {self.message[:20]} "
