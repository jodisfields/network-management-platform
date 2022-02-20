from django.db import models


# class Tickets(models.Model):
#     id = models.IntegerField
#     title = models.CharField(max_length=100)
#     status = models.CharField(max_length=100)
#     created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)
#     # updated_by = models.ForeignKey("auth.User", models.CASCADE)
#     description = models.TextField(max_length=1000)
#     created_date = models.DateTimeField(auto_now_add=True)
#     last_updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
