from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title
class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    price = models.IntegerField()

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

