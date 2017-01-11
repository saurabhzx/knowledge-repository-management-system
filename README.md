# knowledge-repository-management-system
It is a Knowledge Management Repository System which basically fills the gap in sharing the knowledge among the organization.
We are interesting in providing the feature in which the implicit knowledge can be converted into explicit knowledge because we find that some of the concepts and knowledge become explicit only when someone ask the question.

Features It supports:-

Admin Panel:
Provides Admin panel for managing all the database and the portal which includes staff member’s access as well as the administrator access.

Blogging:-
Provides Q/A forum for sharing and asking viewpoints.
Users can comments on the articles or Q/A forums for the purpose of improving the knowledge.
Anyone can freely share the knowledge on this platform as this for the user by the user of the user.

Articles:
User can share articles as per their expertise and interest.
User can see his works and articles shared and liked by him.
User can see the number of downloads and views of his/her stuff.

Notification:
Platform will automatically send emails related to the interested articles, questions and comments in a fixed interval of time for gathering interest of the users.

Search:
User can search the topics in a effective manner.
User can add tags for their post hence increasing the reach of the post to the relevant one.

Performance Appraisal of Associates:-
Supervisor can view the rating of the user on the knowledge sharing portal and consider one of the factor for appraisal or promotions.

Software Used in Development:-

Programming language used      :                        Django-Python, AngularJs 
Server/Client side programming :                        JavaScript , Angular , Django-Python Rest Framewor
Messaging                      :                        Celery
Web server                     :                        Apache2

Cloud Service Platform         :                         AWS EC2 , AWS S3
Tools used                     :                         Sublime Text
Database                       :                         MySQL



Installation Steps:-

Go to requirement.txt file of Django RestFul API

run follwoing command:

pip install -r requirement.txt

python manage.py syncdb

python manage.py runserver 8000

Configure the UI with this URL for consuming the restful web services.
