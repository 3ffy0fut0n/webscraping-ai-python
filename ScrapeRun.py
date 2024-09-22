
import time
import webscraping_ai
from webscraping_ai.rest import ApiException
from pprint import pprint
import json

# Defining the host is optional and defaults to https://api.webscraping.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = webscraping_ai.Configuration(
    host = "https://api.webscraping.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'


# Enter a context with an instance of the API client
with webscraping_ai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webscraping_ai.AIApi(api_client)
    url = 'https://example.com' # str | URL of the target page.
    question = 'What is the summary of this page content?' # str | Question or instructions to ask the LLM model about the target page. (optional)
    context_limit = 4000 # int | Maximum number of tokens to use as context for the LLM model (4000 by default). (optional) (default to 4000)
    response_tokens = 100 # int | Maximum number of tokens to return in the LLM model response. The total context size (context_limit) includes the question, the target page content and the response, so this parameter reserves tokens for the response (see also on_context_limit). (optional) (default to 100)
    on_context_limit = 'error' # str | What to do if the context_limit parameter is exceeded (truncate by default). The context is exceeded when the target page content is too long. (optional) (default to 'error')
    headers = {'key': '{\"Cookie\":\"session=some_id\"}'} # Dict[str, str] | HTTP headers to pass to the target page. Can be specified either via a nested query parameter (...&headers[One]=value1&headers=[Another]=value2) or as a JSON encoded object (...&headers={\"One\": \"value1\", \"Another\": \"value2\"}). (optional)
    timeout = 10000 # int | Maximum web page retrieval time in ms. Increase it in case of timeout errors (10000 by default, maximum is 30000). (optional) (default to 10000)
    js = True # bool | Execute on-page JavaScript using a headless browser (true by default). (optional) (default to True)
    js_timeout = 2000 # int | Maximum JavaScript rendering time in ms. Increase it in case if you see a loading indicator instead of data on the target page. (optional) (default to 2000)
    proxy = 'datacenter' # str | Type of proxy, use residential proxies if your site restricts traffic from datacenters (datacenter by default). Note that residential proxy requests are more expensive than datacenter, see the pricing page for details. (optional) (default to 'datacenter')
    country = 'us' # str | Country of the proxy to use (US by default). Only available on Startup and Custom plans. (optional) (default to 'us')
    device = 'desktop' # str | Type of device emulation. (optional) (default to 'desktop')
    error_on_404 = False # bool | Return error on 404 HTTP status on the target page (false by default). (optional) (default to False)
    error_on_redirect = False # bool | Return error on redirect on the target page (false by default). (optional) (default to False)
    js_script = 'document.querySelector('button').click();' # str | Custom JavaScript code to execute on the target page. (optional)

    try:
        # Get an answer to a question about a given web page
        api_response = api_instance.get_question(url, question=question, context_limit=context_limit, response_tokens=response_tokens, on_context_limit=on_context_limit, headers=headers, timeout=timeout, js=js, js_timeout=js_timeout, proxy=proxy, country=country, device=device, error_on_404=error_on_404, error_on_redirect=error_on_redirect, js_script=js_script)
        print("The response of AIApi->get_question:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIApi->get_question: %s\n" % e)