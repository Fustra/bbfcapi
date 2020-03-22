# BBFC API

![PyPI](https://img.shields.io/pypi/v/bbfcapi)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bbfcapi)
![PyPI - License](https://img.shields.io/pypi/l/bbfcapi)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/fustra/bbfcapi)

Web API and Python library for [BBFC](https://bbfc.co.uk/).

## Public REST API

![Mozilla HTTP Observatory Grade](https://img.shields.io/mozilla-observatory/grade-score/bbfcapi.fustra.co.uk?publish)
![Security Headers](https://img.shields.io/security-headers?url=https%3A%2F%2Fbbfcapi.fustra.co.uk%2Fhealthz)
<a href="https://uptime.statuscake.com/?TestID=SgEZQ2v2KF" title="bbfcapi uptime report">
    <img src="https://app.statuscake.com/button/index.php?Track=K7juwHfXel&Days=7&Design=6"/>
</a>

* Hosted @ <https://bbfcapi.fustra.co.uk>
* Documentation @ <https://bbfcapi.fustra.co.uk/redoc>
* Alternative documentation @ <https://bbfcapi.fustra.co.uk/docs>

Try it now:

```console
$ curl "https://bbfcapi.fustra.co.uk?title=interstellar&year=2014"
{"title":"INTERSTELLAR","year":2014,"ageRating":"12"}
```

Use the Python client:

```console
$ pip install bbfcapi[apis]
```

```py
>>> from bbfcapi.apis import top_search_result
>>> top_search_result("interstellar", 2014)
Film(title='INTERSTELLAR', year=2014, age_rating=<AgeRating.AGE_12: '12'>)
```

## Project Overview

The project is divided into:

* "I want to self-host the REST API demoed above"
    * BBFCAPI - Python REST Web API
    * `pip install bbfcapi[app]`
* "I want a Python library to talk to the REST API as demoed above"
    * Python client for BBFCAPI
    * `pip install bbfcapi[api]` (async variant)
    * `pip install bbfcapi[apis]` (sync variant)
* "I want a Python library to talk to the BBFC website"
    * Python library for the BBFC website
    * `pip install bbfcapi[lib]` (async variant)
    * `pip install bbfcapi[libs]` (sync variant)
* "I want to download the raw HTML web pages from BBFC"
    * Python network client for the BBFC website
    * `pip install bbfcapi[client]` (async variant)
    * `pip install bbfcapi[clients]` (sync variant)
* "I want to parse the downloaded web pages from BBFC"
    * Python HMTL parser for the BBFC web pages
    * `pip install bbfcapi`

Sync versions use the `requests` library, while async variants use `aiohttp`.

## High-Level REST Web API

Install `pip install bbfcapi[app]`.

To use the REST API to query BBFC, first run the web server:

```console
$ uvicorn bbfcapi.app:app
```

Then, to query the API using the Python library *synchronously*:

```py
from bbfcapi.apis import top_search_result
top_search_result("interstellar", 2014, base_url="http://127.0.0.1:8000")
```

Or, to query the API using the Python library *asynchronously*:

```py
from bbfcapi.api import top_search_result
print(await top_search_result("interstellar", 2014, base_url="http://127.0.0.1:8000"))
```

```py
import asyncio
from bbfcapi.api import top_search_result
print(asyncio.run(top_search_result("interstellar", 2014, base_url="http://127.0.0.1:8000")))
```

Or, to query the API using `curl`:

```console
$ curl "127.0.0.1:8000?title=interstellar&year=2014"
{"title":"INTERSTELLAR","year":2014,"age_rating":"12"}
```

Or, to query the API from another web page:

```js
async function call()
{
    const response = await fetch('http://127.0.0.1:8000/?title=interstellar&year=2014');
    const responseJson = await response.json();
    console.log(JSON.stringify(responseJson));
}
call();
```

Additional notes:

* HTTP 404 Not Found is returned when there is no film found.
* Browse documentation @ <http://127.0.0.1:8000/redoc>.
* Or, browse documentation @ <http://127.0.0.1:8000/docs>.
* Samples on hosting this web application are available in the repository's [/docs](/docs) folder.

## High-Level Python Library

To use the library to get results from BBFC *synchronously*:

```py
from bbfcapi.lib import top_search_result
print(top_search_result(title="interstellar", year=2014))
```

To use the library to get results from BBFC *asynchronously*:

```py
from bbfcapi.lib import top_search_result
print(await top_search_result(title="interstellar", year=2014))
```

```py
import asyncio
from bbfcapi.lib import top_search_result
print(asyncio.run(top_search_result(title="interstellar", year=2014)))
```

## Low-Level BBFC Network Client & Parser

To use the library to get raw HTML pages from BBFC *synchronously*:

```console
$ pip install bbfcapi[clients]`
```

```py
from bbfcapi.clients import search
print(search(title="interstellar", year=2014))
```

To use the library to get raw HTML pages from BBFC *asynchronously*:

```console
$ pip install bbfcapi[client]`
```

```py
from bbfcapi.client import search
print(await search(title="interstellar", year=2014))
```

```py
import asyncio
from bbfcapi.client import search
print(asyncio.run(search(title="interstellar", year=2014)))
```

To use the library to parse raw HTML pages from BBFC:

```console
$ pip install bbfcapi`
```

```py
from bbfcapi import parser
print(parser.parse_top_search_result(b"<BBFC search page byte-string>"))
```

## Development

1. `poetry install` to set up the virtualenv (one-off)
2. `poetry run uvicorn bbfcapi.apiweb:app --reload` to run the web server
3. `make fix`, `make check`, and `make test` before committing

There is also `make test-live` which will run live integration tests against
the BBFC website.

### Contributing

Pull requests are welcome :)

### Publishing

This application is published on PyPi.

1. Ensure you have configured the PyPi repository with Poetry (one-off)
2. Run `make release` to execute the check-list

To publish to the test repository:

1. Ensure you have configured the Test PyPi repository with Poetry (one-off)
2. `poetry publish --build -r testpypi` to upload to the test repository

## Changelog

### v2.0.0.dev1

- Reorganise entire package
- Use camelCasing for JSON fields in the web API

### v1.0.1 - 2020-01-19

- Fix parsing 12A age ratings

### v1.0.0 - 2020-01-19

- First release of bbfcapi
