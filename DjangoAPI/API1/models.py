from django.db import models



class Company(models.Model):
    name = models.CharField(max_length=200, null=False)
    location = models.CharField(max_length=150, null=False)
    about = models.TextField(max_length=255, null=False)
    type = models.CharField(max_length=100, choices=(('IT', 'IT'),
                                                     ('Non IT', 'NON IT'),
                                                     ('Electronics', 'ETC')))
    add_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' %(self.name, self.location)
