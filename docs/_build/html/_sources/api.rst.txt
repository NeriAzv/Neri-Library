Using APIs
==========

The ``invoke_api_list`` function is used to make HTTP requests to external APIs. It supports methods such as GET, POST, PUT, DELETE, and PATCH.

Example usage:

.. code-block:: python

   from neri_library import invoke_api_list

   # Example GET request
   response = invoke_api_list("https://api.example.com/data", "your_token")

Parameters:
- **link**: API URL.
- **token**: Authentication token.
- **method**: HTTP method (default: GET).
- **print_response**: Displays the response in the console (default: False).

For more details, refer to the full documentation of the ``invoke_api_list`` function.