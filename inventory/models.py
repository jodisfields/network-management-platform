from django.db import models
import datetime


class Inventory(models.Model):
    class Meta:
        db_table = "inventory"
        verbose_name = "inventory"
        verbose_name_plural = "inventory"

    hostname = models.CharField(
        max_length=50,
        unique=True,
        blank=False,
        null=False,
        verbose_name=("Hostname"),
        help_text=("Hostname"),
        default=None,
    )

    device_type = models.CharField(
        max_length=50,
        unique=False,
        blank=False,
        null=False,
        verbose_name=("Model"),
        help_text=("Device Model"),
        default=None,
    )

    manufacturer = models.CharField(
        max_length=50,
        unique=False,
        blank=False,
        null=False,
        verbose_name=("Manufacturer"),
        help_text=("Device Manufacturer"),
        default=None,
    )

    serial_number = models.CharField(
        max_length=50,
        unique=True,
        blank=False,
        null=False,
        verbose_name=("Serial Number"),
        help_text=("Serial Number"),
        default=None,
    )

    entry_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.hostname
