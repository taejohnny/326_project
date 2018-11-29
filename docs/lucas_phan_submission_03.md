For this submission of the project, I built the "Student" Model, which is a one-to-one model extension of the User. This model was necessary for us to add in the new fields linked to each user. Previously, we had many issues with our User model because we had overwritten the Django built-in implementation instead of extending it. Now, we are able to preserve the old functionalities while adding new ones. I also worked on fixing and cleaning up the HTML files to incorporate our new changes and fix small bugs and UI issues.

I created the registration and password reset functionalities for our site. The registration is a form that creates a User and a Student and links them together while giving them the permissions needed to create feedbacks. The way we made this form was actually a combination of two forms: a User form and a Student form. This is because we need to take in field input for both of the OneToOneModels. It asks for a name, username, email, and password and then initializes with those inputs; after this, it automatically logs in the user andd redirects them to their own page. Initially, all of the information about the student is empty. This is where the "Edit Profile" functionality comes into play. 

Thanh did a majority of the coding on the EditProfile functionality, while I fine tuned it for user experience. He created the form to only be accessible to the user if authenticated and only be functional to their own user. I added in touches such as initializing the fields to have whatever the user previously had already inputted (for example, if there was a bio written previously, the text box would initialize with that written bio). The biggest issue I had was initializing the ManyToMany fields, because I wasn't sure how to initialize the form to a QuerySet of values instead of just one value. After searching the internet for a while, I discovered that I could just use ".all()" to initialize everything (so much time for such a small error). I also explicitly defined the form to create a multiple choice checkbox field instead of the usual dropdown menu.
