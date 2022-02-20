from django.db import models


class Tickets(models.Model):
    class Meta:
        db_table = "tickets"
        verbose_name = "tickets"
        verbose_name_plural = "tickets"

    title = models.CharField(
        max_length=50,
        unique=False,
        blank=False,
        null=False,
        verbose_name=("Title"),
        help_text=("Ticket Title"),
        default=None,
    )

    id = models.IntegerField(
        primary_key=True,
        unique=True,
        verbose_name=("Ticket ID"),
        help_text=("Ticket ID"),
    )

    status = models.CharField(
        max_length=100,
        unique=False,
        verbose_name=("Status"),
        help_text=("Ticket Status"),
    )

    created_by = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        unique=False,
        verbose_name=("Created By"),
        help_text=("Created By"),
    )

    description = models.TextField(
        max_length=1000,
        unique=False,
        verbose_name=("Description"),
        help_text=("Ticket Description"),
    )

    last_updated = models.DateTimeField(
        auto_now=True,
        unique=False,
        verbose_name=("Last Updated"),
        help_text=("Last Updated"),
    )

    def __str__(self):
        return self.title
