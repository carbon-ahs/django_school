from django.shortcuts import render
from django.conf import settings
from core.models import Teacher, School, ClassRoutine, Notice


def home(request):
    school = School.get_school()
    teacher_count = Teacher.get_teachers_count()
    headmaster = Teacher.get_headmaster()
    asst_headmaster = Teacher.get_asst_headmaster()
    third_teacher = Teacher.get_single_teacher(7)
    marquee_flag = settings.DEBUG

    context = {
        "test": "TEST",
        "school": school,
        "teacher_count": teacher_count,
        "headmaster": headmaster,
        "asst_headmaster": asst_headmaster,
        "third_teacher": third_teacher,
        "marquee_flag": marquee_flag,
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


def headmaster_speech(request):
    school = School.get_school()

    context = {
        "test": "TEST",
        "school": school,
    }
    return render(request, "core/headmaster_speech.html", context=context)


def teachers(request):
    school = School.get_school()
    teachers_queary_set = Teacher.objects.all()
    context = {
        "test": "TEST",
        "teachers": teachers_queary_set,
        "school": school,
    }
    return render(request, "core/teachers.html", context=context)

def teachers_vocational(request):
    school = School.get_school()
    teachers_queary_set = Teacher.objects.all()
    context = {
        "test": "TEST",
        "teachers": teachers_queary_set,
        "school": school,
    }
    return render(request, "core/teachers_vocational.html", context=context)

def single_teacher(request, pk):
    school = School.get_school()
    teacher = Teacher.get_single_teacher(pk)

    context = {
        "test": "TEST",
        "teacher": teacher,
        "school": school,
    }
    return render(request, "core/single_teacher.html", context=context)


def about_us(request):
    school = School.get_school()
    context = {
        "test": "TEST",
        "school": school,
    }
    return render(request, "core/about_us.html", context=context)


def management_committee(request):
    school = School.get_school()
    context = {
        "test": "management_committee",
        "school": school,
    }
    return render(request, "core/management_committee.html", context=context)


def staff_members(request):
    school = School.get_school()
    context = {
        "test": "staff_members",
        "school": school,
    }
    return render(request, "core/staff_members.html", context=context)


def notice(request):
    school = School.get_school()
    notice_query_set = Notice.get_all_notices()
    context = {
        "test": "TESTnotice",
        "school": school,
        "notices": notice_query_set,
    }
    return render(request, "core/notice.html", context=context)


def class_routine(request):
    school = School.get_school()
    class_routine = ClassRoutine.get_recent_class_routine()
    context = {
        "test": "class_routine",
        "school": school,
        "class_routine": class_routine,
    }
    return render(request, "core/class_routine.html", context=context)


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


def under_construction(request):
    context = {
        "test": "TEST",
    }
    return render(request, "core/under_construction.html", context=context)


def page_not_found(request, exception):
    print("Page not found view called")
    return render(request, 'core/404.html', status=404)