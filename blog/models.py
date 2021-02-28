from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    amount = models.IntegerField()
    image = models.ImageField(blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# class School(models.Model):
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
#     school_type = models.CharField(max_length=100, null=True, blank=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Group(models.Model):
#     school = models.ForeignKey(School, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     description = models.TextField(max_length=500)
#     profile_group = models.TextField(max_length=500)
#
#     def __str__(self):
#         return self.name
#
#
# class Student(models.Model):
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=500)
#     last_name = models.CharField(max_length=500)
#     age = models.IntegerField()
#     avatar = models.ImageField(null=True, blank=True)
#     description = models.TextField(max_length=100)
#
#     def __str__(self):
#         return str(self.last_name) + ' ' + str(self.first_name)
#
#
# class Work(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     title = models.CharField(max_length=150)
#     subject = models.CharField(max_length=50)
#     description = models.TextField(max_length=500)
#
#     def __str__(self):
#         return 'Project name: ' + str(self.title)
#
#
# class Book(models.Model):
#     student = models.ManyToManyField(Student)
#     title = models.CharField(max_length=150)
#     author = models.CharField(max_length=50)
#     pages = models.IntegerField()
#     # chapters = models.IntegerField()
#
#     def __str__(self):
#         return f'{self.author}: {self.title}'
#
