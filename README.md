# BBFC API

Web API and Python library for [BBFC](https://bbfc.co.uk/).

## High-Level REST Web API

To use the REST API to query BBFC:

```console
$ uvicorn bbfcapi.apiweb:app
```

```
$ curl "127.0.0.1:8000?title=interstellar&year=2014"
{"title":"INTERSTELLAR","year":2014,"age_rating":"12"}
```

To use the REST API from a web page:

```console
$ uvicorn bbfcapi.apiweb:app
```

```js
async function call()
{
    const response = await fetch('http://127.0.0.1:8000/?title=interstellar&year=2014');
    const responseJson = await response.json();
    console.log(JSON.stringify(responseJson));
}
call();
```

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
