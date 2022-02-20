from django.db import models


class Documentation(models.Model):
    class Meta:
        db_table = "documentation"
        verbose_name = "Documentation"
        verbose_name_plural = "Documentation"

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        default=None,
        verbose_name="Title",
        help_text="Document Title.",
    )

    category = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        default="",
        verbose_name="Category",
        help_text="Documentation Category.",
    )

    obj_url = models.URLField(
        max_length=255,
        blank=False,
        null=False,
        default="",
        verbose_name="URL",
        help_text="Objective Reference.",
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="Documentation Description.",
    )

    def __str__(self):
        return self.title
