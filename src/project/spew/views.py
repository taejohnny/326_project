from django.shortcuts import render
from spew.models import Student, Class, Professor, Feedback, Subject, Like
from django.views import generic
from django.views import generic
from django.db.models import Count

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import RegistrationForm, EditUserForm, EditStudentForm
from django.contrib.auth.forms import UserChangeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group
from datetime import datetime
from django.utils.formats import get_format
from .forms import RegistrationForm
#from django.contrib.auth.forms import UserCreationForm

import random


# Create your views here.
def index(request):
    '''"""View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact="a").count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()'''
    num_classes = Class.objects.all().count()
    class_list = Class.objects.all()        
    random_index_list = random.sample(range(len(class_list)), 4)
    class_featured = class_list[random_index_list[0]]
    class_featured_1 = class_list[random_index_list[1]]
    class_featured_2 = class_list[random_index_list[2]]
    class_featured_3 = class_list[random_index_list[3]]
    feedback_1 = random.choice(Feedback.objects.filter(course = class_featured_1))
    feedback_2 = random.choice(Feedback.objects.filter(course = class_featured_2))
    feedback_3 = random.choice(Feedback.objects.filter(course = class_featured_3))
    popular_class_list = Class.objects.all().annotate(num_feedback=Count('feedback')).order_by('-num_feedback')

    highest_rated_class_list = Class.objects.all().order_by('-feedback__rating')
    
    popular_feedback_list = {}
    popular_user_list = {}
    for i in range(0, len(popular_class_list) - 1):
        popular_feedback_list[i] = random.choice(Feedback.objects.filter(course=popular_class_list[i]))
        popular_user_list[i] = popular_feedback_list[i].student
        
    highest_rated_feedback_list = {}
    highest_rated_user_list = {}
    for i in range(0, len(highest_rated_class_list) - 1):
        highest_rated_feedback_list[i] = random.choice(Feedback.objects.filter(course=highest_rated_class_list[i]))
        highest_rated_user_list[i] = highest_rated_feedback_list[i].student


    popular_sorted = []
    class_list = Class.objects.all()
    for course in class_list:
       popular_sorted.append((course, 0))
       for course_feedback in Feedback.objects.filter(course=course.class_id):
           popular_sorted[len(popular_sorted)-1] = (popular_sorted[len(popular_sorted)-1][0], popular_sorted[len(popular_sorted)-1][1] + int(course_feedback.rating))
       popular_sorted[len(popular_sorted)-1] = (popular_sorted[len(popular_sorted)-1][0], popular_sorted[len(popular_sorted)-1][1] / len(Feedback.objects.filter(course=course.class_id)))

    popular_sorted.sort(key=lambda x: x[1])
    popular_sorted.reverse()

    popular_class_list = [i[0] for i in popular_sorted]
    popular_rating_list = [range(round(i[1])) for i in popular_sorted]
    popular_rating_half_boolean_list = [(not (round(i[1]*2)/2).is_integer() and (not i[1] % 1 > .5)) for i in popular_sorted]
    

    fav_average_ratings = []
    class_list = Class.objects.all()
    for course in class_list:
       fav_average_ratings.append((course, 0))
       for course_feedback in Feedback.objects.filter(course=course.class_id):
           fav_average_ratings[len(fav_average_ratings)-1] = (fav_average_ratings[len(fav_average_ratings)-1][0], fav_average_ratings[len(fav_average_ratings)-1][1] + int(course_feedback.rating))
       fav_average_ratings[len(fav_average_ratings)-1] = (fav_average_ratings[len(fav_average_ratings)-1][0], fav_average_ratings[len(fav_average_ratings)-1][1] / len(Feedback.objects.filter(course=course.class_id)))

    fav_average_ratings.sort(key=lambda x: x[1])
    fav_average_ratings.reverse()

    highest_rated_class_list = [i[0] for i in fav_average_ratings]
    highest_rated_rating_list = [range(round(i[1])) for i in fav_average_ratings]
    highest_rated_half_boolean_list = [(not (round(i[1]*2)/2).is_integer() and (not i[1] % 1 > .5)) for i in fav_average_ratings]

    context = {
        "num_classes": num_classes,
        "class_featured": class_featured,
        "class_featured_1": class_featured_1,
        "class_featured_2": class_featured_2,
        "class_featured_3": class_featured_3,
        "popular_class_list": popular_class_list,
        "popular_rating_list": popular_rating_list,
        "popular_rating_half_boolean_list": popular_rating_half_boolean_list,
        "highest_rated_feedback_list": highest_rated_feedback_list,
        "highest_rated_half_boolean_list": highest_rated_half_boolean_list,
        "popular_feedback_list": popular_feedback_list,
        "popular_user_list": popular_user_list,
        "highest_rated_user_list": highest_rated_user_list,
        "class_list": class_list,
        "highest_rated_class_list": highest_rated_class_list,
        "highest_rated_rating_list": highest_rated_rating_list,
        "feedback_1": feedback_1,
        "feedback_2": feedback_2,
        "feedback_3": feedback_3,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)


def class_page(request):


    context = {

    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, "class_page.html", context=context) ##THIS IS HWERE HTE PAGE GOES

def profile(request):

    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "profile.html", context=context) ##THIS IS HWERE HTE PAGE GOES

def professor(request):
    
    context = {
    }
    
    return render(request, "professor_page.html", context=context)

def search_results(request):

    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "search_results.html", context=context) ##THIS IS HWERE HTE PAGE GOES

def submissions_page(request):

    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "submissions_page.html", context=context) ##THIS IS HWERE HTE PAGE GOES

def advanced_search(request):

    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "advanced_search.html", context=context) ##THIS IS HWERE HTE PAGE GOES

def ClassListView(request):

    classes = []
    professors = []
    for lecture in Class.objects.all():
        prof = random.choice(Professor.objects.all())
        classes.append(lecture)
        professors.append(prof)

    context = {
        'list': zip(classes, professors)
    }

    return render(request, "class_list.html", context=context) ##THIS IS HWERE HTE PAGE GOES

def SearchResults(request):

    classes = []
    professors = []
    for lecture in Class.objects.all():
        prof = random.choice(Professor.objects.all())
        classes.append(lecture)
        professors.append(prof)

    context = {
        'list': zip(classes, professors)
    }

    return render(request, "search_results.html", context=context) ##THIS IS HWERE HTE PAGE GOES
    

class ClassDetailView(generic.DetailView):
    model = Class
    template_name = "class_page.html"

    def get_context_data(self, **kwargs):

        pk = self.kwargs.get(self.pk_url_kwarg, None)
        logged_student = self.request.user.student

        num_likes_zip = []
        like_bool_zip = []
        for class_feedback in Feedback.objects.filter(course=pk):
            num_likes = Like.objects.filter(review=class_feedback, liked=True).count()

            num_likes_zip.append(num_likes)
            if self.request.user.username != 'admin' and self.request.user.is_authenticated:
                like_bool = Like.objects.filter(review=class_feedback, student=logged_student)[0]
                like_bool_zip.append(like_bool.liked)

        popular_sorted = []
        class_list = Class.objects.filter(class_id=pk)
        for course in class_list:
           popular_sorted.append((course, 0))
           for course_feedback in Feedback.objects.filter(course=course.class_id):
               popular_sorted[len(popular_sorted)-1] = (popular_sorted[len(popular_sorted)-1][0], popular_sorted[len(popular_sorted)-1][1] + int(course_feedback.rating))
           popular_sorted[len(popular_sorted)-1] = (popular_sorted[len(popular_sorted)-1][0], popular_sorted[len(popular_sorted)-1][1] / len(Feedback.objects.filter(course=course.class_id)))

        popular_sorted.sort(key=lambda x: x[1])
        popular_sorted.reverse()

        popular_class_list = [i[0] for i in popular_sorted]
        popular_rating_list = [range(round(i[1])) for i in popular_sorted]
        popular_rating_half_boolean_list = [(not (round(i[1]*2)/2).is_integer() and (not i[1] % 1 > .5)) for i in popular_sorted]
        


        context = super(ClassDetailView, self).get_context_data(**kwargs)
        context['class_feedback'] = zip(Feedback.objects.filter(course=pk), num_likes_zip, like_bool_zip)
        context['professor'] = Professor.objects.filter(course=pk).all()
        context['popular_rating_list'] = popular_rating_list
        context['popular_rating_half_boolean_list'] = popular_rating_half_boolean_list

        return context

    def post(self, request, *args, **kwargs):

        if self.request.user.username == 'admin' or not self.request.user.is_authenticated:
            return redirect('/accounts/login')


        logged_student = Student.objects.filter(user=request.user)[0]
        liked_student_id = request.POST.get("liked_student_id", "")
        liked_course_code = request.POST.get("liked_course_id", "").rsplit(' ', 1)[1]
        liked_course_subject = request.POST.get("liked_course_id", "").rsplit(' ', 1)[0]
        liked_course_subject_object = Subject.objects.filter(subject_name=liked_course_subject)[0]
        f_course = Class.objects.filter(subject=liked_course_subject_object, code=liked_course_code)[0]
        f_student = Student.objects.filter(student_id=liked_student_id)[0]
        f_feedback = Feedback.objects.filter(course=f_course, student=f_student)
        like = Like.objects.filter(student=logged_student, review=f_feedback[0])[0]

        if like.liked == True:
            like.liked = False
        else:
            like.liked = True

        like.save()

        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class UserListView(generic.ListView):
    model = Student
    template_name = "user_list.html"

    def get_context_data(self, **kwargs):

        context = super(UserListView, self).get_context_data(**kwargs)
        context['student_user'] = Student.objects.all()

        return context

class UserDetailView(generic.DetailView):

    model = Student
    template_name = "profile.html"

    def myView(request):    
        user = request.user
        if user.username == 'admin':
            return redirect('/')
    
    def get_context_data(self, **kwargs):


        pk = self.kwargs.get(self.pk_url_kwarg, None)

        fav_average_ratings = []
        fav_list = Student.objects.get(student_id=pk).fav_courses.all()
        for course in fav_list:
           fav_average_ratings.append((course, 0))
           for course_feedback in Feedback.objects.filter(course=course.class_id):
               fav_average_ratings[len(fav_average_ratings)-1] = (fav_average_ratings[len(fav_average_ratings)-1][0], fav_average_ratings[len(fav_average_ratings)-1][1] + int(course_feedback.rating))
           fav_average_ratings[len(fav_average_ratings)-1] = (fav_average_ratings[len(fav_average_ratings)-1][0], fav_average_ratings[len(fav_average_ratings)-1][1] / len(Feedback.objects.filter(course=course.class_id)))

        fav_average_ratings = [round(i[1], 1) for i in fav_average_ratings]



        current_average_ratings = []
        current_list = Student.objects.get(student_id=pk).current_courses.all()
        for course in current_list:
           current_average_ratings.append((course, 0))
           for course_feedback in Feedback.objects.filter(course=course.class_id):
               current_average_ratings[len(current_average_ratings)-1] = (current_average_ratings[len(current_average_ratings)-1][0], current_average_ratings[len(current_average_ratings)-1][1] + int(course_feedback.rating))
           current_average_ratings[len(current_average_ratings)-1] = (current_average_ratings[len(current_average_ratings)-1][0], current_average_ratings[len(current_average_ratings)-1][1] / len(Feedback.objects.filter(course=course.class_id)))

        current_average_ratings = [round(i[1], 1) for i in current_average_ratings]


        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['user_feedback'] = Feedback.objects.filter(student=pk).all()
        context['feedback_count'] = Feedback.objects.filter(student=pk).count()
        context['favorite_courses'] = zip(fav_list, fav_average_ratings)
        context['current_courses'] = zip(current_list, current_average_ratings)
        context['student_id1'] = 1
        context['student_id2'] = 2

        if self.request.user.username != 'admin' and self.request.user.is_authenticated:
            context['student_id1'] = pk
            context['student_id2'] = Student.objects.filter(user=self.request.user)[0].student_id

        return context

class ProfessorListView(generic.ListView):
    model = Professor
    template_name = "professor_list.html"



class ProfessorDetailView(generic.DetailView):
    model = Professor
    template_name = "professor_page.html"

    
    def get_context_data(self, **kwargs):

        pk = self.kwargs.get(self.pk_url_kwarg, None)

        taught_course_ratings = []
        course_list = Professor.objects.get(prof_id=pk).course.all()
        for course in course_list:
           taught_course_ratings.append((course, 0))
           for course_feedback in Feedback.objects.filter(course=course.class_id):
               taught_course_ratings[len(taught_course_ratings)-1] = (taught_course_ratings[len(taught_course_ratings)-1][0], taught_course_ratings[len(taught_course_ratings)-1][1] + int(course_feedback.rating))
           taught_course_ratings[len(taught_course_ratings)-1] = (taught_course_ratings[len(taught_course_ratings)-1][0], taught_course_ratings[len(taught_course_ratings)-1][1] / len(Feedback.objects.filter(course=course.class_id)))

        taught_course_ratings = [round(i[1], 1) for i in taught_course_ratings]


        context = super(ProfessorDetailView, self).get_context_data(**kwargs)
        context['courses_taught'] = zip(course_list, taught_course_ratings)
        return context

def Registration(request):

    stu_group, created = Group.objects.get_or_create(name='Student')
    ct = ContentType.objects.get_for_model(Feedback)
    permission = Permission.objects.get(codename="can_add_feedback", name="Can add feedback", content_type=ct)
    if request.method == 'POST':
        print('POSTING REG \n')
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.user_permissions.add(permission)
            user.groups.add(stu_group)
            user.save()
            student = Student()
            student.user = user
            student.save()
            login(request, user)
            return redirect('/user/' + str(user.student.student_id))

    else:
        form = RegistrationForm()
        # form2 = StudentForm()
    context = {'form': form}
    return render(request, "registration/register.html", context) ##THIS IS HWERE HTE PAGE GOES

    '''if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/classes')

    else:
        form = UserCreationForm()
    args = {'form': form}
    return render(request, 'register.html', args)'''


def EditProfile(request):

    if not request.user.is_authenticated:
        return redirect('/')
    elif request.user.username == 'admin':
        return redirect('/')

    user = request.user
    if request.method == 'POST':
        user_form = EditUserForm(user, request.POST)
        student_form = EditStudentForm(user, request.POST)
        # student = request.user.student
        if user_form.is_valid() and student_form.is_valid():
            #form.save()
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            email = user_form.cleaned_data['email']


            bio = student_form.cleaned_data['bio']
            major = student_form.cleaned_data['major']
            concentration = student_form.cleaned_data['concentration']
            grad_year = student_form.cleaned_data['grad_year']
            fav_courses = student_form.cleaned_data['fav_courses']
            current_courses = student_form.cleaned_data['current_courses']

            print('\n')
            student = Student.objects.filter(user=request.user)[0]

            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            student.bio = bio
            student.major = major
            student.concentration = concentration
            student.grad_year = grad_year
            student.fav_courses.set(fav_courses)
            student.current_courses.set(current_courses)
            student.save()

            return redirect('/user/' + str(user.student.student_id))

    else:
        user_form = EditUserForm(user)
        student_form = EditStudentForm(user)
    context = {'user_form': user_form, 'student_form': student_form}
    return render(request, "edit_profile.html", context) ##THIS IS HWERE HTE PAGE GOES


class FeedbackCreate(PermissionRequiredMixin, CreateView):
    model = Feedback
    permission_required = "spew.can_add_feedback"
    template_name = "feedback_form.html"
    fields = ('comment', 'course', 'professor', 'rating')
    def form_valid(self, form):
        curr_user = self.request.user
        f_student = Student.objects.get(user=curr_user)
        form.instance.student = curr_user.student
        form.save()
        form.instance.date = datetime.date(datetime.now())
        form.save()
        new_feedback = Feedback.objects.last()
        like = Like(student=f_student, review=new_feedback, liked=False)
        like.save()
        return super(FeedbackCreate, self).form_valid(form)
    success_url = reverse_lazy('classes')
