# Datto RMM Unofficial Python SDK

This is an unofficial Python SDK for Datto RMM. It was created to provide a Python interface for interacting with the Datto RMM API.

## Installation

You can install the package using pip:

```bash
pip install drmmsdk
```

## Usage

Initialize the SDK by providing your API key, API secret, and server. You can find your API key and API secret in the Datto RMM dashboard. The server is the URL of your Datto RMM instance, such as `concord`, `vidal,`, `zinfandel`, `merlot`, `pinotage`, or `syrah`.

```python
from drmmsdk import drmmsdk

drmm = drmmsdk(api_key="your_api_key", api_secret="your_api_secret", server="your_server")
```

## Methods

The SDK currently supports the following methods:

1. `create_site()`: Creates a new site.
2. `create_site_variable()`: Creates a new site variable.
3. `move_device()`: Moves a device.
4. `create_quick_job()`: Creates a quick job.
5. `create_account_variable()`: Creates an account variable.
6. `reset_api_keys()`: Resets the API keys.
7. `fetch_site_data()`: Fetches site data.
8. `update_site()`: Updates a site.
9. `update_site_variable()`: Updates a site variable.
10. `delete_site_variable()`: Deletes a site variable.
11. `create_proxy_settings()`: Creates proxy settings.
12. `delete_site_proxy_settings()`: Deletes site proxy settings.
13. `set_device_warranty()`: Sets device warranty.
14. `set_device_udf()`: Sets device UDF.
15. `unmute_alert()`: Unmutes an alert.
16. `resolve_alert()`: Resolves an alert.
17. `mute_alert()`: Mutes an alert.
18. `update_account_variable()`: Updates an account variable.
19. `delete_account_variable()`: Deletes an account variable.
20. `get_system_status()`: Gets system status.
21. `fetch_request_rate()`: Fetches request rate.
22. `fetch_pagination_configurations()`: Fetches pagination configurations.
23. `get_site_variables()`: Gets site variables.
24. `fetch_site_settings()`: Fetches site settings.
25. `fetch_site_filters()`: Fetches site filters.
26. `get_site_devices()`: Gets site devices.
27. `fetch_resolved_alerts()`: Fetches resolved alerts.
28. `fetch_open_alerts()`: Fetches open alerts.
29. `fetch_job_data()`: Fetches job data.
30. `fetch_job_components()`: Fetches job components.
31. `get_default_filters()`: Gets default filters.
32. `fetch_custom_filters()`: Fetches custom filters.
33. `get_device_data()`: Gets device data.
34. `fetch_device_data()`: Fetches device data.
35. `fetch_audit_data()`: Fetches audit data.
36. `fetch_audited_software()`: Fetches audited software.
37. `fetch_alert_data()`: Fetches alert data.
38. `fetch_account_data()`: Fetches account data.
39. `fetch_account_variables()`: Fetches account variables.
40. `get_user_records()`: Gets user records.
41. `fetch_site_records()`: Fetches site records.
42. `get_devices()`: Gets devices.
43. `fetch_components()`: Fetches components.

Please note that this is an unofficial SDK and is not endorsed by Datto. Always ensure that you're following all relevant policies and guidelines when interacting with the Datto RMM API.
