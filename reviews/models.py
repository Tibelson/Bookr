from django.db import models

class Book(models.Model):
    """Information about the book"""
    title = models.CharField(max_length=255)
    publication_date = models.DateField(verbose_name='Date the book was published')
    isbn = models.CharField(max_length=20)

class Contributor(models.Model):
    """Info on people relating to the book"""
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField()


class Publisher(models.Model):
    """A company that publishes books"""
    name = models.CharField(max_length=255)
    website = models.URLField(help_text='Website location of publisher')
    email = models.EmailField()

