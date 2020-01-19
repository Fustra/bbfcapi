# BBFC API

Web API and Python library for [BBFC](https://bbfc.co.uk/).

## High-Level REST Web API

To use the REST API to query BBFC, first run the web server:

```console
$ uvicorn bbfcapi.apiweb:app
```

Then, to query the API using `curl`:

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

## High-Level Python Library

To use the library to get results from BBFC *asynchronously*:

```py
from bbfcapi.apilib import top_search_result
print(await top_search_result(title="interstellar", year=2014))
```

To use the library to get results from BBFC *synchronously*:

```py
import asyncio
from bbfcapi.apilib import top_search_result
print(asyncio.run(top_search_result(title="interstellar", year=2014)))
```

## Low-Level Python Library

To use the library to get raw HTML pages from BBFC *asynchronously*:

```py
from bbfcapi import client
print(await client.search(title="interstellar", year=2014))
```

To use the library to get raw HTML pages from BBFC *synchronously*:

```py
import asyncio
from bbfcapi import client
print(asyncio.run(client.search(title="interstellar", year=2014)))
```

To use the library to parse raw HTML pages from BBFC:

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

### Unreleased

...

### v1.0.1 - 2020-01-19

- Fix parsing 12A age ratings

### v1.0.0 - 2020-01-19

- First release of bbfcapi
