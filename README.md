# BBFC API

Web API and Python library for [BBFC](https://bbfc.co.uk/).

To use the REST API to query BBFC:

```console
$ uvicorn bbfcapi.api:app

$ curl "127.0.0.1:8000?title=interstellar&year=2014"
{"title":"INTERSTELLAR","year":2014,"age_rating":"12"}
```

To use the REST API from a web page:

```js
async function call()
{
    const response = await fetch('http://127.0.0.1:8000/?title=interstellar&year=2014');
    const responseJson = await response.json();
    console.log(JSON.stringify(responseJson));
}
call();
```

To use the library to get raw HTML pages from BBFC *asynchronously*:

```py
from bbfcapi import client
print(await client.search(title="interstellar", year=2014))
```

To use the library to get raw HTML pages from BBFC *synchronously*:

```py
from bbfcapi import client
print(asyncio.run(client.search(title="interstellar", year=2014)))
```

To use the library to parse raw HTML pages from BBFC:

```py
from bbfcapi import parser
print(parser.top_search_result(b"<BBFC search page byte-string>"))
```

## Development

1. `poetry install` to set up the virtualenv (one-off)
2. `poetry run uvicorn bbfcapi.api:app --reload` to run the web server
3. `make fix`, `make check`, and `make test` before committing

### Contributing

Pull requests are welcome :)
