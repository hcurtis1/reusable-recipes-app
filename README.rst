===
Recipes Blog
===

Recipes blog is a reusable app for Django. 

For detailed information, us the "docs" directory.

A few steps to get you started
------------------------------

1. Add 'recipes_blog' to your INSTALLED_APPS in your settings file. See below:
	INSTALLED_APPS = (
		...
		'recipes_blog'
	)
	
2. Include the URLconf pattern in your urls.py:
	url(r'^blog/', include('recipes_blog.urls'))
	
3. Run 'python manage.py migrate' in order to create your models.

4. Add the css for the blog into your html:
	<link> rel="stylesheet" href="{% static "css/blog.css" %}"</link>
	
5. for links to the blog use the below in your html:
	<a href="/blog/">*Desired Content*</a>