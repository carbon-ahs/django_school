from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Teacher(models.Model):
    """model class"""

    HEAD_OF_INSTITUTION = "Headmaster"
    VICE_HEAD_OF_INSTITUTION = "Asstistant Headmaster"
    TEACHER = "Teacher"
    DESIGNATIONS = [
        (HEAD_OF_INSTITUTION, HEAD_OF_INSTITUTION),
        (VICE_HEAD_OF_INSTITUTION, VICE_HEAD_OF_INSTITUTION),
        (TEACHER, TEACHER),
    ]

    name = models.CharField(_("Name"), max_length=254)
    designation = models.CharField(
        max_length=255,
        default=TEACHER,
    )
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
        upload_to="images/",
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


class School(models.Model):
    """school info"""

    name = models.CharField(_("Name"), max_length=255)
    thana = models.CharField(_("Thana"), max_length=50)
    zilla = models.CharField(_("zilla"), max_length=50)
    description_title = models.CharField(_("Desciption Title"), max_length=50)
    description = models.TextField(_("Description"))
    student_count = models.IntegerField(_("Student Count"))
    teacher_count = models.IntegerField(_("Teacher Count"))
    class_count = models.IntegerField(_("Class Count"))

    class Meta:
        verbose_name = _("School")
        verbose_name_plural = _("Schools")

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("School_detail", kwargs={"pk": self.pk})
