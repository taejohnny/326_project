from django.shortcuts import render
from spew.models import User, Class, Professor, Feedback, Subject
from django.views import generic
import random
from django.views import generic
from django.db.models import Count

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

    highest_rated_class_list = Class.objects.all()
    
    popular_feedback_list = {}
    popular_user_list = {}
    for i in range(0, len(popular_class_list) - 1):
        popular_feedback_list[i] = random.choice(Feedback.objects.filter(course=popular_class_list[i]))
        popular_user_list[i] = popular_feedback_list[i].user
        
    highest_rated_feedback_list = {}
    highest_rated_user_list = {}
    for i in range(0, len(highest_rated_class_list) - 1):
        highest_rated_feedback_list[i] = random.choice(Feedback.objects.filter(course=highest_rated_class_list[i]))
        highest_rated_user_list[i] = highest_rated_feedback_list[i].user


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


class ClassListView(generic.ListView):
    model = Class
    template_name = "class_list.html"


class ClassDetailView(generic.DetailView):
    model = Class
    template_name = "class_page.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        context = super(ClassDetailView, self).get_context_data(**kwargs)
        context['class_feedback'] = Feedback.objects.filter(course=pk)
        return context


class SearchResults(generic.ListView):
   model = Class
   template_name = "search_results.html"

class UserListView(generic.ListView):
    model = User
    template_name = "user_list.html"

class UserDetailView(generic.DetailView):
    model = User
    template_name = "profile.html"

    
    def get_context_data(self, **kwargs):

        pk = self.kwargs.get(self.pk_url_kwarg, None)

        fav_average_ratings = []
        fav_list = User.objects.get(user_id=pk).fav_courses.all()
        for course in fav_list:
           fav_average_ratings.append((course, 0))
           for course_feedback in Feedback.objects.filter(course=course.class_id):
               fav_average_ratings[len(fav_average_ratings)-1] = (fav_average_ratings[len(fav_average_ratings)-1][0], fav_average_ratings[len(fav_average_ratings)-1][1] + int(course_feedback.rating))
           fav_average_ratings[len(fav_average_ratings)-1] = (fav_average_ratings[len(fav_average_ratings)-1][0], fav_average_ratings[len(fav_average_ratings)-1][1] / len(Feedback.objects.filter(course=course.class_id)))

        fav_average_ratings = [round(i[1], 1) for i in fav_average_ratings]



        current_average_ratings = []
        current_list = User.objects.get(user_id=pk).current_courses.all()
        for course in current_list:
           current_average_ratings.append((course, 0))
           for course_feedback in Feedback.objects.filter(course=course.class_id):
               current_average_ratings[len(current_average_ratings)-1] = (current_average_ratings[len(current_average_ratings)-1][0], current_average_ratings[len(current_average_ratings)-1][1] + int(course_feedback.rating))
           current_average_ratings[len(current_average_ratings)-1] = (current_average_ratings[len(current_average_ratings)-1][0], current_average_ratings[len(current_average_ratings)-1][1] / len(Feedback.objects.filter(course=course.class_id)))

        current_average_ratings = [round(i[1], 1) for i in current_average_ratings]


        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['user_feedback'] = Feedback.objects.filter(user=pk).all()
        context['feedback_count'] = Feedback.objects.filter(user=pk).count()
        context['favorite_courses'] = zip(fav_list, fav_average_ratings)
        context['current_courses'] = zip(current_list, current_average_ratings)       
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
        context['courses_taught'] = Class.objects.filter(professor=pk).all()
        return context