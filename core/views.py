from django.shortcuts import render
from core.models import Teacher, School


def home(request):
    try:
        school = School.objects.get(pk=1)
    except School.DoesNotExist:
        school = None

    try:
        teacher_count = Teacher.objects.count()
    except Teacher.DoesNotExist:
        teacher_count = 20

    # headmaster = Teacher.objects.filter(designation="Headmaster").values()[0]
    headmaster = Teacher.objects.get(designation="Headmaster")
    # asst_headmaster = Teacher.objects.get(designation="Headmaster")
    asst_headmaster = Teacher.get_asst_headmaster()
    print(asst_headmaster)

    context = {
        "test": "TEST",
        "school": school,
        "teacher_count": teacher_count,
        "headmaster": headmaster,
        "asst_headmaster": asst_headmaster,
    }
    return render(request, "core/home.html", context=context)


def home_static(request):
    description_title = "Viqarunnisa Noon School & College"
    description = "Viqarunnisa Noon School & College is an all-girls educational institute in Baily Road, Dhaka, Bangladesh. It has 4 campuses and around 25,000 students. Viqarunnisa Noon School & College is one of the renowned educational institutes in Bangladesh. We consider every child as unique and so we maintain inclusive learning-teaching environment at every step in our great set-up. It is a fact now that our results are getting better in the public examinations every time. It has been made possible through our extensive and effective care stretched out to every individual student. Our students conglomerate here from multifarious backgrounds; various strata of the society. They enter the threshold of our strong and fortified home of learning and come out bearing an all-round personality."

    context = {
        "test": "TEST",
        "school_name": "Viqarunnisa Noon School & College",
        "thana": "Basundhara R/A",
        "zilla": "Dhaka",
        "description_title": description_title,
        "description": description,
        "student_count": 549,
        "teacher_count": 15,
        "class_count": 13,
    }
    return render(request, "core/home.html", context=context)


def teachers(request):
    school = School.get_school()
    teachers_queary_set = Teacher.objects.all()
    context = {
        "test": "TEST",
        "teachers": teachers_queary_set,
        "school": school,
    }
    return render(request, "core/teachers.html", context=context)


def single_teacher(request, pk):
    school = School.get_school()
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        teacher = None
    context = {
        "test": "TEST",
        "teacher": teacher,
        "school": school,
    }
    return render(request, "core/single_teacher.html", context=context)


def notice(request):
    school = School.get_school()
    context = {
        "test": "TESTnotice",
        "school": school,
    }
    return render(request, "core/notice.html", context=context)


def say_hello(request):
    context = {
        "test": "TEST",
    }
    return render(request, "test/hlw.html", context=context)


def test(request):
    context = {
        "test": "TEST",
    }
    return render(request, "test/test.html", context=context)
