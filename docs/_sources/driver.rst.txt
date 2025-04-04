Driver Configuration
====================

The ``Instancedriver`` class is used to configure and initialize the browser driver. It offers various options to customize the browser's behavior.

Example usage:

.. code-block:: python

   from neri_library import Instancedriver

   # Initialize the driver
   driver = Instancedriver()

Available options:
- **Version**: Browser version.
- **Subprocess**: Runs the browser in a separate process.
- **Browser**: Defines the browser to be used (e.g., Chrome, Firefox).
- **Driver_path**: Custom path to the driver executable.
- **Stealth_min**: Advanced settings to avoid detection.
- **Timeout**: Maximum wait time in case of freezing.

For more details, refer to the full documentation of the ``Instancedriver`` class.