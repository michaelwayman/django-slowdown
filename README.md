## Django-SlowDown

Slows down Django's responses to clients.

Add Django-Slowdown to your MIDDLEWARE and slow the response time of every request.

Sometimes you need to slow things down during development to get a realistic feel for the user experience in production.

**This package will help you develop better UX Flow.**

When the backend loads too fast during development it is easy to forget to:

 - Add a spinner during loading.
 - Disable buttons to prevent double form submit.
 - Add simple animations and transitions.
 - Load as you scroll.
 - Look at your site *while* content loads.
 - etc...

## Installation & Usage

#### 1. Install python package

`python setup.py`

#### 2. Add to django MIDDLEWARE

```
MIDDLEWARE = [
    ...
]

if DEBUG is True:
    MIDDLEWARE.append('slowdown.middleware.SlowDownMiddleware')
```

#### 3. Customize django-slowdown (optional)

in settings.py

```
# Number of seconds to slow down each request
SLOW_DOWN = 0.5
```



