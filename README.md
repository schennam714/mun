# Website

The official website for the Thomas Jefferson High School for Science and Technology Model United Nations club.
Created by Vikram Raghu.
Currently Supervised by Vikram Raghu.

## User Accounts
* To login, navigate to http://localhost:8000/login/ion or click the login button on this site
* To make yourself a superuser, run this in the Django shell (`python manage.py shell`) in another terminal
```
username="<TJ USERNAME>"; from tjmun.apps.users.models import User; u = User.objects.get(username=username); u.is_superuser = True; u.is_staff = True; u.is_officer = True; u.save()
```
# Site Info
This site is built using Django
* [Django Documentation] (https://docs.djangoproject.com/en/2.2/)
* [Django Tags] (https://docs.djangoproject.com/en/2.2/topics/templates/)
* [Django Templates] (https://docs.djangoproject.com/en/2.2/ref/templates/builtins/)

# Content Management
* To add Awards, navigate to activities.tjhsst.edu/mun/admin
Click on "Years" under the section titled "Awards", and add a new year if the current one does not exist
For naming conventions, click on a previous year object to view
Within each Year object, click the green '+' sign to add a new conference
In the new window, fill out the information with the naming conventions found under all Conference objects
Repeat the process to add committees
In each committee, input the name of the committee, and add delegation objects by clicking the '+' sign
The naming convention for delegations is as follows below:
[AwardTitle] - [Delegate Name(s)] [(Delegate Position)]
for example: GAVEL - Vikram Raghu (Secretary of State) 
         or: Verbal - Sean Nguyen and Lisa Raj (Paraguay)
Capitalize the AwardTitle if it is a gavel, and check the box labeled 'gavel' to put the gavel icon on the page

* To Add Techmun committees, do the same underneath the section titled "Techmun"
There are existing CommTypes, under which you can create and delete committee objects
As always, see previous examples for reference

* The other pages are basic html, but check the urls.py and views.py in each app to understand the layout
* refer to the documentation links above for clarification
