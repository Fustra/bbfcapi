graphql_url = "https://www.bbfc.co.uk/graphql"


graphql_query = """
query Autocomplete($url: String!, $searchTerm: String!) {
  autocomplete(url: $url, searchTerm: $searchTerm) {
    results {
      classification
      title
      type
      releaseDate
      shortFormInsight
      slug
    }
  }
}
""".strip()


def build_search_request(title: str) -> dict:
    return {
        "query": graphql_query,
        "variables": {
            "url": "https://www.bbfc.co.uk/",
            "searchTerm": title,
        },
    }
