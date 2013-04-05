cyclone-rest-handler
====================

Cyclone-rest-handler was forked from [tornado-rest-handler](https://github.com/paulocheque/tornado-rest-handler)
Everything is almost the same, except that you can mix twisted drivers and libraries due to cyclone.
Use the rake stuff to get going: rake dev_env, rake tests etc.
It probably wont work with python 3.3 etc 

From here below this is the original README adjusted to cyclone and butchered accordingly:

A simple Python Cyclone handler that manage Rest requests automatically.

* [Basic Example of Usage](#basic-example-of-usage)
  * [Routes](#routes)
  * [Handlers](#handlers)
  * [Templates](#templates)
* [Installation](#installation)
* [Change Log](#change-log)
* [TODO](#todo)

Basic Example of Usage
------------------------

In the current implementation, there is only one handler for MongoEngine ORM, besides the library does not depends on the MongoEngine!

With +-10 lines of code you can create a handler for your ORM.

Routes
------------------------

One handler manage every Rest routes:

| Method       | Route               | Comment |
|------------- |---------------------|---------|
| GET          | /animal index       | display a list of all animals |
| GET          | /animal/new         | new return an HTML form for creating a new animal |
| POST         | /animal             | create a new animal |
| GET          | /animal/:id         | show an animal |
| GET          | /animal/:id/edit    | return an HTML form for editing a photo |
| PUT          | /animal/:id         | update an animal data |
| DELETE       | /animal/:id         | delete an animal |
| POST*        | /animals/:id/delete | same as DELETE /animals/:id |
| POST*        | /animals/:id        | same as PUT /animals/:id |

* *Since HTML5-forms does not support PUT/DELETE, these additional POSTs were added.

* To specify Cyclone Rest routes you can use the method **rest_routes**:


```python
from cyclone_rest_handler import routes, rest_routes

TORNADO_ROUTES = [
    # another handlers here

    rest_routes(Animal),

    # another handlers here
]

TORNADO_SETTINGS = {}

application = cyclone.web.Application(routes(TORNADO_ROUTES), **TORNADO_SETTINGS)
```

The library does not support auto-pluralization yet, so you may want to change the prefix:

```python
rest_routes(Animal, prefix='animals'),
```

You can also define to where will be redirect after an action succeed:

```python
rest_routes(Animal, prefix='animals', redirect_pos_action='/animals'),
```

Handlers
------------------------

All the get/post/put/delete methods are implemented for you, but if you want to customize some behavior, you write your own handler:

```python
class AnimalHandler(cyclone.web.RequestHandler):
    pass # your custom methods here
```

And then, registered it:

```python
rest_routes(Animal, handler=AnimalHandler),
```

To create a RestHandler for your ORM you must override the RestHandler class and implement the following methods:

```python
from cyclone_rest_handler import RestHandler

class CouchDBRestHandler(RestHandler):
    def instance_list(self): return [] # it can return a list or a queryset etc
    def find_instance_by_id(self, obj_id): pass
    def save_instance(self, obj): pass
    def update_instance(self, obj): pass
    def delete_instance(self, obj): pass
```

By default, the list page will show all models of that type. To filter by user or other properties, override the *instance_list* method:

```python
class AnimalHandler(cyclone.web.RequestHandler):
    def instance_list(self):
        return Animal.objects.filter(...)
```


Templates
------------------------

You must create your own template. Templates will receive the variables **obj** or **objs** and **alert** in case there is some message. The edit template will also receive the variable **errors** and functions **value_for**, **error_for** and **has_error**.

It must have the names list.html, show.html and edit.html. But you can customize if you want to:

```python
rest_routes(Animal, list_template='another_name.html', edit_template='...', show_template='...'),
```

By default, the directory is the model name in lower case (animal in this example).

* animal/list.html
* animal/show.html
* animal/edit.html

But you may change the directory though:

```python
rest_routes(Animal, template_path='your_template_path'),
```


Installation
------------

```
pip install cyclone-rest-handler
```

#### or

```
1. Download zip file
2. Extract it
3. Execute in the extracted directory: python setup.py install
```

#### Requirements/tested with

* Python 2.6 / 2.7 
* Tested with latest cyclone



TODO
-------------
* test with more twisted ORM and db libraries - perhaps define an ORM simple standard
* Handlers for another ORMs (other than MongoEngine).
* Pagination
* i18n
* Use fields and exclude to facilitate auto-generate forms:
* pluralize urls
* splitted handlers
