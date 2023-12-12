from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Teacher(models.Model):
    """model class"""

    name = models.CharField(_("Name"), max_length=254)
    designation = models.CharField(_("Designation"), max_length=50)
    fb_link = models.CharField(
        _("Facebook"),
        max_length=255,
        null=True,
        blank=True,
        default="#",
    )
    linkedIn_link = models.CharField(
        _("LinkedIn"),
        max_length=255,
        null=True,
        blank=True,
        default="#",
    )
    phone_number = models.CharField(_("Phone"), max_length=255, null=True, blank=True)
    picture_url = models.ImageField(
        upload_to="upload_image/",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Teacher_detail", kwargs={"pk": self.pk})
