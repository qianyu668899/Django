=====
Polls
=====

Polls is a simple Django app to conduct Web-based polls.

Detailed documentation is in the "docs" directory

Quick start
------------
1. Add "polls" to your INSTALLED_APPS setting like this ::
	INSTALLED_APPS = {
		...
		'polls',
	}
2. Include the polls URLconf in your project urls.py like this::
	url(r'^polls/', include('polls.urls')),

3. Run 'python manage.py syncdb' to create the polls models.

4. Start the development server and visit http://127.0.0.1:8080/admin to create a poll(you'll need the Admin app enabled)

5. Visit the http://127.0.0.1:8080/polls/ to parcipate in the poll.