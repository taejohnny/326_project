import uuid
from django.db.models import Q
from django.db import models
from django.urls import reverse

class Subject(models.Model):
    """Model representing a book genre."""

    subject_name = models.CharField(max_length=200, help_text="Enter a class subject (e.g. Computer Science)")

    def __str__(self):
        """String for representing the Model object."""
        return self.subject_name







class Class(models.Model):
    """Model representing a class."""

    title = models.CharField(max_length=200)
    # Code of the class (326 for CS326 or 250 for CS250)
    code = models.CharField(max_length=100, default='404')
    # Description of class
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the class")
    # Maps to the subject of this class
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    # Number of credits for this class
    num_credits = models.TextField(max_length=1000, help_text="Enter a the number of credits this class fulfills")
    # A boolean field for if there are exams
    exams = models.TextField(max_length=1000, help_text="Does this class have exams?")
    # A boolean field for if attendance is required
    attendance = models.TextField(max_length=1000, help_text="Is attendance taken at this class?")
    # A text field for the required textbooks
    textbooks = models.TextField(max_length=1000, help_text="Does this class require textbooks?")
    # Maps to other classes that are related to this class
    related_classes = models.ManyToManyField("self", help_text="Select a class that is related to this one")
    # Maps to the feedback for this class 
    class_feedback = models.ManyToManyField("Feedback", help_text="Provide feedback for this class")
    # A particular id for this class (simply an integer)
    class_id = models.CharField(
        primary_key=True,
        max_length=1000,
        default=uuid.uuid1,
        help_text="Unique ID for this particular class across the website",
    )
#
#    def display_related(self):
#        """Create a string for the related class. This is required to display related class in Admin."""
#        return ", ".join(related_class.name for related_class in self.related_class.all()[:3])
#
#    related_class.short_description = "Related Class"
#    
#    prereq = models.ManyToManyField(Class, help_text="Select a class that is s prerequisite to this one")
#
#    def display_related(self):
#        """Create a string for the prerequisite. This is required to display the class in Admin."""
#        return ", ".join(prereq.name for prereq in self.prereq.all())
#
#    prereq.short_description = "Prerequisite"

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse("class-detail", args=[str(self.class_id)])


class User(models.Model):
    """Model representing the User."""

    # A character field for the first name.
    first_name = models.CharField(max_length=100)
    # A character field for the last name.
    last_name = models.CharField(max_length=100)
    # A character field for the major.
    major = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    # A list for the classes that were favorited
    course = models.ManyToManyField(Class, help_text="Select the classes this user favorites")
    # A textfield for the user's biography
    bio = models.TextField(max_length=1000, help_text="Enter a bio for this user")
    # A charField for the user's graduation year
    grad_year = models.CharField(max_length=100)
    # A particular id for this user
    user_id = models.CharField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular user",
    )
    
    def display_course(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        # This function uses the string object's join method to "join"
        # all the genre strings into a single string separated by ',
        # '. This uses Python's list comprehension feature. If you do
        # not know what this is you should look this up to see what
        # this is. It is a very powerful language feature!
        #
        # We also use Python's list slicing notation ([:3]). This
        # indicates that we will only take the first 3 elements from
        # indicates that we will only take the first 3 elements from
        # indicates that we will only take the first 3 elements from
        # the list. This is done so we only display some of the genres
        # rather than all of them - efficiency!
        return ", ".join(course.title for course in self.course.all()[:3])
    
    course.short_description = "Favorite Courses"

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse("user-detail", args=[str(self.user_id)])

    def __str__(self):
        """String for representing the Model object."""
        #return f"{self.first_name}, {self.last_name}"
        return '%s %s' % (self.first_name, self.last_name)

class Professor(models.Model):
    """Model representing the Professor."""

    # A character field for the first name.
    first_name = models.CharField(max_length=100)
    # A character field for the last name.
    last_name = models.CharField(max_length=100)
    # A character field for the position.
    position = models.CharField(max_length=100)
    # A list field for the courses taught
    course = models.ManyToManyField(Class, help_text="Select a class this professor teaches")
    # A text field for the contact info
    contact = models.TextField(max_length=1000, help_text="Enter a brief description of the class")

    def display_course(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        # This function uses the string object's join method to "join"
        # all the genre strings into a single string separated by ',
        # '. This uses Python's list comprehension feature. If you do
        # not know what this is you should look this up to see what
        # this is. It is a very powerful language feature!
        #
        # We also use Python's list slicing notation ([:3]). This
        # indicates that we will only take the first 3 elements from
        # indicates that we will only take the first 3 elements from
        # indicates that we will only take the first 3 elements from
        # the list. This is done so we only display some of the genres
        # rather than all of them - efficiency!
        return ", ".join(course.title for course in self.course.all()[:3])
    
#    course.short_description = "Taught Courses"
    
    # A character field for the office
    office = models.CharField(max_length=100)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse("author-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        #return f"{self.last_name}, {self.first_name}"
        return '%s %s' % (self.first_name, self.last_name)

class Feedback(models.Model):
    """Model representing the feedback/reviews"""
    
    # A text field for the comment of the review
    comment = models.TextField(max_length=1000, help_text="Enter a brief comment about the class.")
    # A foreign key for the class it's for
    course = models.ForeignKey("Class", on_delete=models.SET_NULL, null=True)
    # A foreign key for the user it's from
    user = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    # A char field for the rating; should be average of all ratings but we'll just leave it as is for now.
    rating = models.CharField(max_length=100, help_text="Give a rating from 1 to 5")
    # A 
    date = models.DateField(null=True, blank=True)


    def __str__(self):
        """String for representing the Model object."""
        #return f"{self.first_name}, {self.last_name}"
        return '%s %s %s' % (self.user, self.comment, self.rating)