# BBFC API

![PyPI](https://img.shields.io/pypi/v/bbfcapi)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bbfcapi)
![PyPI - License](https://img.shields.io/pypi/l/bbfcapi)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/fustra/bbfcapi)

Web API and Python library for [BBFC](https://bbfc.co.uk/).

## Public REST API

![Mozilla HTTP Observatory Grade](https://img.shields.io/mozilla-observatory/grade-score/bbfcapi.fustra.uk?publish)
![Security Headers](https://img.shields.io/security-headers?url=https%3A%2F%2Fbbfcapi.fustra.uk%2Fhealthz)
<a href="https://uptime.statuscake.com/?TestID=SgEZQ2v2KF" title="bbfcapi uptime report">
    <img src="https://app.statuscake.com/button/index.php?Track=K7juwHfXel&Days=7&Design=6"/>
</a>

* Hosted @ <https://bbfcapi.fustra.uk>
* Documentation @ <https://bbfcapi.fustra.uk/redoc>
* Alternative documentation @ <https://bbfcapi.fustra.uk/docs>

Try it now:

```console
$ curl "https://bbfcapi.fustra.uk?title=interstellar"
{"title":"Interstellar","ageRating":"12"}
```

Use the Python client:

```console
$ pip install bbfcapi[api_sync]
```

```py
>>> from bbfcapi.api_sync import best_match
>>> best_match("interstellar", 2014)
Film(title='INTERSTELLAR', age_rating=<AgeRating.AGE_12: '12'>)
```

## Project Overview

The project is divided into:

* "I want to self-host the REST API demoed above"
    * BBFCAPI - Python REST Web API
    * `pip install bbfcapi[app]`
* "I want a Python library to talk to the REST API as demoed above"
    * Python client for BBFCAPI
    * `pip install bbfcapi[api_async]` (async variant)
    * `pip install bbfcapi[api_sync]` (sync variant)
* "I want a Python library to talk to the BBFC website"
    * Python library for the BBFC website
    * `pip install bbfcapi[lib_async]` (async variant)
    * `pip install bbfcapi[lib_sync]` (sync variant)
* "I want to download the raw HTML web pages from BBFC"
    * Python network client for the BBFC website
    * `pip install bbfcapi[client_async]` (async variant)
    * `pip install bbfcapi[client_sync]` (sync variant)
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
from bbfcapi.api_sync import best_match
best_match("interstellar", base_url="http://127.0.0.1:8000")
```

Or, to query the API using the Python library *asynchronously*:

```py
from bbfcapi.api_async import best_match
print(await best_match("interstellar", base_url="http://127.0.0.1:8000"))
```

```py
import asyncio
from bbfcapi.api_async import best_match
print(asyncio.run(best_match("interstellar", base_url="http://127.0.0.1:8000")))
```

Or, to query the API using `curl`:

```console
$ curl "127.0.0.1:8000?title=interstellar"
{"title":"Interstellar",age_rating":"12"}
```

Or, to query the API from another web page:

```js
async function call()
{
    const response = await fetch('http://127.0.0.1:8000/?title=interstellar');
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
from bbfcapi.lib_async import best_match
print(best_match(title="interstellar"))
```

To use the library to get results from BBFC *asynchronously*:

```py
from bbfcapi.lib_async import best_match
print(await best_match(title="interstellar"))
```

```py
import asyncio
from bbfcapi.lib_async import best_match
print(asyncio.run(best_match(title="interstellar")))
```

## Low-Level BBFC Network Client & Parser

To use the library to get raw HTML pages from BBFC *synchronously*:

```console
$ pip install bbfcapi[client_sync]`
```

```py
from bbfcapi.client_sync import search
print(search(title="interstellar"))
```

To use the library to get raw HTML pages from BBFC *asynchronously*:

```console
$ pip install bbfcapi[client_async]`
```

```py
from bbfcapi.client_async import search
print(await search(title="interstellar"))
```

```py
import asyncio
from bbfcapi.client_async import search
print(asyncio.run(search(title="interstellar")))
```

To use the library to parse results from BBFC's GraphQL API:

```console
$ pip install bbfcapi[parser]`
```

```py
from bbfcapi import parser
print(parser.best_autocomplete_match({"BBFC": "...graphql json..."}))
```

## Development

1. `poetry install -E all` to set up the virtualenv (one-off)
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

### Unpublished

...

### v3.0.1 - 2021-03-04

- Change primary host to bbfcapi.fustra.uk
- [Security] Upgrade dependencies

### v3.0.0 - 2020-11-08

- IMPORTANT: Major changes for compatibility with BBFC's new website
- Update various dependencies

### v2.0.2 - 2020-03-22

- Fix another missing dependency

### v2.0.1 - 2020-03-22

- Fix missing dependencies

### v2.0.0 - 2020-03-22

- Add Python client library for the BBFCAPI REST Web API
- Use camelCasing for JSON fields in the web API
- Reorganise entire package

### v1.0.1 - 2020-01-19

- Fix parsing 12A age ratings

### v1.0.0 - 2020-01-19

- First release of bbfcapi
