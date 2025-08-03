from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Teacher(models.Model):
    """model class"""

    HEAD_OF_INSTITUTION = "Headmaster"
    VICE_HEAD_OF_INSTITUTION = "Assistant Headmaster"
    TEACHER = "Assistant Teacher"
    INSTRUCTOR = "Instructor"
    LAB_ASSISTANT = "Lab Assistant"
    OFFICE_ASSISTANT = "Office Assistant / Computer Operator"
    DEMONSTRATOR = "Demonstrator"
    DESIGNATIONS = [
        ("Headmaster", HEAD_OF_INSTITUTION),
        ("Assistant Headmaster", VICE_HEAD_OF_INSTITUTION),
        ("Assistant Teacher", TEACHER),
        ("Instructor", INSTRUCTOR),
        ("Lab Assistant", LAB_ASSISTANT),
        ("Office Assistant / Computer Operator", OFFICE_ASSISTANT),
        ("Demonstrator", DEMONSTRATOR),
    ]

    name = models.CharField(_("Name"), max_length=254)
    designation = models.CharField(
        max_length=255,
        default=TEACHER,
        choices=DESIGNATIONS,
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
    email = models.EmailField(_("Email"), max_length=254, null=True, blank=True)
    picture = models.ImageField(
        upload_to="images/",
    )

    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Teacher_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_all_teachers():
        return Teacher.objects.all()

    @staticmethod
    def get_teachers_count():
        return Teacher.objects.count()

    @staticmethod
    def get_headmaster():
        try:
            headmaster = Teacher.objects.get(designation=Teacher.HEAD_OF_INSTITUTION)
        except Teacher.DoesNotExist:
            headmaster = None

        return headmaster

    @staticmethod
    def get_asst_headmaster():
        try:
            asst_headmaster = Teacher.objects.get(
                designation=Teacher.VICE_HEAD_OF_INSTITUTION
            )
        except Teacher.DoesNotExist:
            asst_headmaster = None

        return asst_headmaster

    @staticmethod
    def get_single_teacher(pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            teacher = None

        return teacher



class School(models.Model):
    """school info"""

    name = models.CharField(_("Name"), max_length=255)
    thana = models.CharField(_("Thana"), max_length=50)
    zilla = models.CharField(_("zilla"), max_length=50)
    description_title = models.CharField(_("Desciption Title"), max_length=50)
    description = models.TextField(_("Description"))
    headmaster_speech = models.TextField(_("Headmaster Speech"), null=True, blank=True)
    student_count = models.IntegerField(_("Student Count"))
    teacher_count = models.IntegerField(_("Teacher Count"))
    class_count = models.IntegerField(_("Class Count"))
    phone = models.CharField(_("Phone"), max_length=50, null=True, blank=True)
    email = models.EmailField(_("Email"), max_length=254, null=True, blank=True)

    class Meta:
        verbose_name = _("School")
        verbose_name_plural = _("Schools")

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("School_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_school():
        try:
            school = School.objects.get(pk=1)
        except School.DoesNotExist:
            school = None

        return school


class Notice(models.Model):
    """Model definition for Notice."""

    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), null=True, blank=True)
    file = models.FileField(
        _("File"),
        upload_to="notices/%Y/%m/%d",
    )
    publish_date = models.DateTimeField(default=datetime.now(), blank=True)

    class Meta:
        """Meta definition for Notice."""

        verbose_name = "Notice"
        verbose_name_plural = "Notices"

    @staticmethod
    def get_all_notices():
        return Notice.objects.all()

    def __str__(self):
        """Unicode representation of Notice."""
        return str(self.title)


class ClassRoutine(models.Model):
    """Model definition for ClassRoutine."""

    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"), null=True, blank=True)
    file = models.FileField(
        _("File"),
        upload_to="ClassRoutine/%Y/%m/%d",
        null=True,
        blank=True,
    )
    publish_date = models.DateTimeField(default=datetime.now(), blank=True)

    class Meta:
        """Meta definition for Notice."""

        verbose_name = "Class Routine"
        verbose_name_plural = "Class Routines"

    @staticmethod
    def get_all_class_routine():
        return ClassRoutine.objects.all()

    @staticmethod
    def get_recent_class_routine():
        return ClassRoutine.objects.last()

    def __str__(self):
        """Unicode representation of ClassRoutine."""
        return str(self.title)
