from django.db import models

# Create your models here.


class FibbonaciNumbers(models.Model):
    n = models.IntegerField(db_index=True)
    value = models.CharField(max_length=10485760)
