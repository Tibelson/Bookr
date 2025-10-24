from django.db import models
from django.contrib import auth

class Publisher(models.Model):
    """A company that publishes books"""
    name = models.CharField(max_length=255)
    website = models.URLField(help_text='Website location of publisher')
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    """Information about the book"""
    title = models.CharField(max_length=255)
    publication_date = models.DateField(verbose_name='Date the book was published')
    isbn = models.CharField(max_length=20)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    contributor = models.ManyToManyField('Contributor', through="BookContributor")

    def __str__(self):
        return self.title

class Contributor(models.Model):
    """Info on people relating to the book"""
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField()

    def __str__(self):
        return self.first_name 

class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "Author", "AUTHOR"
        CO_AUTHOR = "Co-Author", "CO-AUTHOR"
        EDITOR = "EDITOR", "Editor"
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor,on_delete=models.CASCADE)
    role = models.CharField(choices=ContributionRole.choices, max_length=20)

class Review(models.Model):
    """Review of the book"""
    content = models.TextField(help_text='Review book')
    rating = models.IntegerField()
    date_created = models.DateField()
    date_edited = models.DateField()
    creator = models.ForeignKey(auth.get_user_model(),on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)









