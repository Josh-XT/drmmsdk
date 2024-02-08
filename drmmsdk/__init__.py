from ezsession import get_session
import json
import requests


class drmmsdk:
    def __init__(self, api_key: str, api_secret: str, server: str = "concord"):
        if not api_key or not api_secret:
            raise ValueError("API key and secret are required")
        self.base_uri = f"https://{server}-api.centrastage.net"
        auth = {
            "type": "oauth_basic",
            "auth_uri": f"{self.base_uri}/auth/oauth/token",
            "username": api_key,
            "password": api_secret,
            "server": server,
        }
        self.session = get_session(**auth)
        self.commands = {
            "Datto RMM - Create site": self.create_site,
            "Datto RMM - Create site variable": self.create_site_variable,
            "Datto RMM - Move device": self.move_device,
            "Datto RMM - Create quick job": self.create_quick_job,
            "Datto RMM - Create account variable": self.create_account_variable,
            "Datto RMM - Reset api keys": self.reset_api_keys,
            "Datto RMM - Fetch site data": self.fetch_site_data,
            "Datto RMM - Update site": self.update_site,
            "Datto RMM - Update site variable": self.update_site_variable,
            "Datto RMM - Delete site variable": self.delete_site_variable,
            "Datto RMM - Create proxy settings": self.create_proxy_settings,
            "Datto RMM - Delete site proxy settings": self.delete_site_proxy_settings,
            "Datto RMM - Set device warranty": self.set_device_warranty,
            "Datto RMM - Set device udf": self.set_device_udf,
            "Datto RMM - Unmutealert": self.unmute_alert,
            "Datto RMM - Resolve alert": self.resolve_alert,
            "Datto RMM - Mute alert": self.mute_alert,
            "Datto RMM - Update account variable": self.update_account_variable,
            "Datto RMM - Delete account variable": self.delete_account_variable,
            "Datto RMM - Get system status": self.get_system_status,
            "Datto RMM - Fetch request rate": self.fetch_request_rate,
            "Datto RMM - Fetch pagination configurations": self.fetch_pagination_configurations,
            "Datto RMM - Get site variables": self.get_site_variables,
            "Datto RMM - Fetch site settings": self.fetch_site_settings,
            "Datto RMM - Fetch site filters": self.fetch_site_filters,
            "Datto RMM - Get site devices": self.get_site_devices,
            "Datto RMM - Fetch resolved alerts": self.fetch_resolved_alerts,
            "Datto RMM - Fetch open alerts": self.fetch_open_alerts,
            "Datto RMM - Fetch job data": self.fetch_job_data,
            "Datto RMM - Fetch job components": self.fetch_job_components,
            "Datto RMM - Get default filters": self.get_default_filters,
            "Datto RMM - Fetch custom filters": self.fetch_custom_filters,
            "Datto RMM - Get device data": self.get_device_data,
            "Datto RMM - Fetch device data": self.fetch_device_data,
            "Datto RMM - Fetch audit data": self.fetch_audit_data,
            "Datto RMM - Fetch audited software": self.fetch_audited_software,
            "Datto RMM - Fetch alert data": self.fetch_alert_data,
            "Datto RMM - Fetch account data": self.fetch_account_data,
            "Datto RMM - Fetch account variables": self.fetch_account_variables,
            "Datto RMM - Get user records": self.get_user_records,
            "Datto RMM - Fetch site records": self.fetch_site_records,
            "Datto RMM - Get devices": self.get_devices,
            "Datto RMM - Fetch components": self.fetch_components,
        }

    async def create_site(
        self,
        name: str,
        description: str,
        notes: str,
        onDemand: bool,
        splashtopAutoInstall: bool,
        proxySettings: dict,
    ):
        url = self.base_uri + "/v2/site"
        payload = {
            "name": name,
            "description": description,
            "notes": notes,
            "onDemand": onDemand,
            "splashtopAutoInstall": splashtopAutoInstall,
            "proxySettings": proxySettings,
        }
        try:
            response = await self.session.put(url, json=payload)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    async def create_site_variable(self, siteUid, name, value, masked):
        url = f"{self.base_uri}/v2/site/{siteUid}/variable"
        payload = {"name": name, "value": value, "masked": masked}
        try:
            response = await self.session.put(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Something went wrong:", err)
        return None

    async def move_device(self, deviceUid, siteUid):
        try:
            url = f"{self.base_uri}/v2/device/{deviceUid}/site/{siteUid}"
            response = await self.session.put(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")
        return None

    async def create_quick_job(self, deviceUid, jobName, jobComponent):
        url = f"{self.base_uri}/v2/device/{deviceUid}/quickjob"
        payload = {"jobName": jobName, "jobComponent": jobComponent}
        try:
            response = await self.session.put(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")
        return None

    async def create_account_variable(
        self, name: str, value: str, masked: bool
    ) -> dict:
        url = self.base_uri + "/v2/account/variable"
        payload = {"name": name, "value": value, "masked": masked}
        try:
            response = await self.session.put(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Error: {err}")
        return {}  # Return an empty dictionary if an error occurs

    async def reset_api_keys(self):
        try:
            url = self.base_uri + "/v2/user/resetApiKeys"
            response = await self.session.post(url)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as e:
            print(f"An error occurred: {e}")
            return None

    async def fetch_site_data(self, siteUid):
        url = f"{self.base_uri}/v2/site/{siteUid}"
        try:
            response = await self.session.get(url)
            response.raise_for_status()
            data = await response.json()
            return data
        except requests.exceptions.HTTPError as e:
            print(f"Error occurred while fetching site data: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None

    async def update_site(
        self, siteUid, name, description, notes, onDemand, splashtopAutoInstall
    ):
        try:
            url = f"{self.base_uri}/v2/site/{siteUid}"
            payload = {
                "name": name,
                "description": description,
                "notes": notes,
                "onDemand": onDemand,
                "splashtopAutoInstall": splashtopAutoInstall,
            }
            response = await self.session.post(url, json=payload)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as e:
            print(f"An error occurred: {e}")
            return None

    async def update_site_variable(self, siteUid, variableId, name, value):
        try:
            url = f"{self.base_uri}/v2/site/{siteUid}/variable/{variableId}"
            payload = {"name": name, "value": value}
            response = await self.session.post(url, json=payload)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")
        return None

    async def delete_site_variable(self, siteUid, variableId):
        try:
            url = f"{self.base_uri}/v2/site/{siteUid}/variable/{variableId}"
            response = await self.session.delete(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Something went wrong:", err)

    async def create_proxy_settings(
        self, siteUid, host, password, port, type, username
    ):
        url = f"{self.base_uri}/v2/site/{siteUid}/settings/proxy"
        payload = {
            "host": host,
            "password": password,
            "port": port,
            "type": type,
            "username": username,
        }
        try:
            response = await self.session.post(url, json=payload)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as e:
            print(f"Error occurred: {e}")
            return None

    async def delete_site_proxy_settings(self, siteUid):
        try:
            url = f"{self.base_uri}/v2/site/{siteUid}/settings/proxy"
            response = await self.session.delete(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Error: {err}")

    async def set_device_warranty(self, deviceUid: str, warrantyDate: str):
        url = f"{self.base_uri}/v2/device/{deviceUid}/warranty"
        payload = {"warrantyDate": warrantyDate}
        try:
            response = await self.session.post(url, json=payload)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as e:
            # Handle client errors (4xx)
            if e.status == 400:
                raise ValueError("Request is invalid.")
            elif e.status == 404:
                raise ValueError("Device was not found.")
            elif e.status == 401:
                raise ValueError("Request cannot be authorized.")
            elif e.status == 403:
                raise ValueError(
                    "Authenticated user doesn't have access to this resource."
                )
            elif e.status == 409:
                raise ValueError(
                    "Request aborted due to concurrent write access to this record."
                )
            else:
                raise ValueError("Unknown client error occurred.")

    async def set_device_udf(
        self,
        deviceUid,
        udf1=None,
        udf2=None,
        udf3=None,
        udf4=None,
        udf5=None,
        udf6=None,
        udf7=None,
        udf8=None,
        udf9=None,
        udf10=None,
        udf11=None,
        udf12=None,
        udf13=None,
        udf14=None,
        udf15=None,
        udf16=None,
        udf17=None,
        udf18=None,
        udf19=None,
        udf20=None,
        udf21=None,
        udf22=None,
        udf23=None,
        udf24=None,
        udf25=None,
        udf26=None,
        udf27=None,
        udf28=None,
        udf29=None,
        udf30=None,
    ):
        url = f"{self.base_uri}/v2/device/{deviceUid}/udf"
        data = {
            "udf1": udf1,
            "udf2": udf2,
            "udf3": udf3,
            "udf4": udf4,
            "udf5": udf5,
            "udf6": udf6,
            "udf7": udf7,
            "udf8": udf8,
            "udf9": udf9,
            "udf10": udf10,
            "udf11": udf11,
            "udf12": udf12,
            "udf13": udf13,
            "udf14": udf14,
            "udf15": udf15,
            "udf16": udf16,
            "udf17": udf17,
            "udf18": udf18,
            "udf19": udf19,
            "udf20": udf20,
            "udf21": udf21,
            "udf22": udf22,
            "udf23": udf23,
            "udf24": udf24,
            "udf25": udf25,
            "udf26": udf26,
            "udf27": udf27,
            "udf28": udf28,
            "udf29": udf29,
            "udf30": udf30,
        }

        try:
            response = await self.session.post(url, json=data)
            response.raise_for_status()
            return await response.json()
        except Exception as e:
            return {"error": str(e)}

    async def unmute_alert(self, alertUid):
        try:
            url = f"{self.base_uri}/v2/alert/{alertUid}/unmute"
            response = await self.session.post(url)
            response.raise_for_status()
            json_response = await response.json()
            return json_response
        except Exception as e:
            print(f"Error occurred: {e}")
            return None

    async def resolve_alert(self, alertUid):
        url = f"{self.base_uri}/v2/alert/{alertUid}/resolve"
        try:
            response = await self.session.post(url)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    async def mute_alert(self, alertUid):
        try:
            url = f"{self.base_uri}/v2/alert/{alertUid}/mute"
            response = await self.session.post(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error occurred: {e}")
            return None

    async def update_account_variable(self, variableId, name, value):
        url = f"{self.base_uri}/v2/account/variable/{variableId}"
        data = {"name": name, "value": value}
        try:
            response = await self.session.post(url, json=data)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Something went wrong:", err)
        return None

    async def delete_account_variable(self, variableId):
        url = f"{self.base_uri}/v2/account/variable/{variableId}"
        try:
            response = await self.session.delete(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        except requests.exceptions.ConnectionError as e:
            print(f"Error Connecting: {e}")
        except requests.exceptions.Timeout as e:
            print(f"Timeout Error: {e}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return None

    async def get_system_status(self):
        url = self.base_uri + "/v2/system/status"
        try:
            response = await self.session.get(url)
            response.raise_for_status()
            data = await response.json()
            return data
        except Exception as e:
            print(f"Error: {e}")
            return None

    async def fetch_request_rate(self):
        try:
            url = self.base_uri + "/v2/system/request_rate"
            response = await self.session.get(url)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Error: {err}")
        return None

    async def fetch_pagination_configurations(self):
        url = self.base_uri + "/v2/system/pagination"
        try:
            response = await self.session.get(url)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
        return None

    async def get_site_variables(self, siteUid, page=None, max=None):
        try:
            url = f"{self.base_uri}/v2/site/{siteUid}/variables"
            params = {}
            if page is not None:
                params["page"] = page
            if max is not None:
                params["max"] = max

            response = await self.session.get(url, params=params)
            response.raise_for_status()
            return await response.json()

        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Something went wrong:", err)

    async def fetch_site_settings(self, siteUid):
        try:
            url = f"{self.base_uri}/v2/site/{siteUid}/settings"
            response = await self.session.get(url)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as e:
            print(f"Error occurred while fetching site settings: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    async def fetch_site_filters(self, siteUid, page=None, max=None):
        url = f"{self.base_uri}/v2/site/{siteUid}/filters"
        params = {}
        if page is not None:
            params["page"] = page
        if max is not None:
            params["max"] = max

        try:
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")
        return None

    async def get_site_devices(self, siteUid, page=None, max=None, filterId=None):
        url = f"{self.base_uri}/v2/site/{siteUid}/devices"
        params = {"page": page, "max": max, "filterId": filterId}
        try:
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            data = await response.json()
            return data
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")
        return None

    async def fetch_resolved_alerts(self, siteUid, page=None, max=None, muted=None):
        try:
            url = f"{self.base_uri}/v2/site/{siteUid}/alerts/resolved"
            params = {"page": page, "max": max, "muted": muted}
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")
        return None

    async def fetch_open_alerts(self, siteUid, page=None, max=None, muted=None):
        url = f"{self.base_uri}/v2/site/{siteUid}/alerts/open"
        params = {"page": page, "max": max, "muted": muted}

        try:
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")
        return None

    async def fetch_job_data(self, jobUid):
        try:
            url = f"{self.base_uri}/v2/job/{jobUid}"
            response = await self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Error:", err)
        return None

    async def fetch_job_components(self, jobUid, page=None, max=None):
        try:
            url = f"{self.base_uri}/v2/job/{jobUid}/components"
            params = {"page": page, "max": max}
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            return await response.json()
        except Exception as e:
            print(f"Error fetching job components: {e}")
            return {}

    async def get_default_filters(self, page=None, max=None):
        try:
            url = f"{self.base_uri}/v2/filter/default-filters"
            params = {}
            if page is not None:
                params["page"] = page
            if max is not None:
                params["max"] = max
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    async def fetch_custom_filters(self, page=None, max=None):
        url = self.base_uri + "/v2/filter/custom-filters"
        params = {"page": page, "max": max}
        try:
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            json_response = await response.json()
            return json_response
        except requests.exceptions.HTTPError as e:
            print(f"Error occurred: {e}")
        except Exception as e:
            print(f"Unknown error occurred: {e}")

    async def get_device_data(self, deviceUid):
        try:
            url = f"{self.base_uri}/v2/device/{deviceUid}"
            response = await self.session.get(url)
            response.raise_for_status()
            data = await response.json()
            return data
        except requests.exceptions.HTTPError as e:
            print(f"An error occurred: {e}")
            return None

    async def fetch_resolved_alerts(self, deviceUid, page=None, max=None, muted=None):
        url = f"{self.base_uri}/v2/device/{deviceUid}/alerts/resolved"
        params = {}
        if page is not None:
            params["page"] = page
        if max is not None:
            params["max"] = max
        if muted is not None:
            params["muted"] = muted

        try:
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            json_response = await response.json()
            return json_response
        except Exception as e:
            print(f"Error occurred: {e}")
            return None

    async def fetch_open_alerts(self, deviceUid, page=None, max=None, muted=None):
        try:
            url = f"{self.base_uri}/v2/device/{deviceUid}/alerts/open"
            params = {"page": page, "max": max, "muted": muted}
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            json_response = await response.json()
            return json_response
        except Exception as e:
            error_message = str(e)
            return {"error": error_message}

    async def fetch_device_data(self, deviceId):
        url = f"{self.base_uri}/v2/device/id/{deviceId}"
        try:
            response = await self.session.get(url)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None

    async def fetch_audit_data(self, deviceUid):
        url = f"{self.base_uri}/v2/audit/printer/{deviceUid}"
        try:
            response = await self.session.get(url)
            response.raise_for_status()
            data = await response.json()
            return data
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")
        return None

    async def fetch_audit_data(self, deviceUid):
        try:
            url = f"{self.base_uri}/v2/audit/esxihost/{deviceUid}"
            response = await self.session.get(url)
            response.raise_for_status()
            data = await response.json()
            return data
        except requests.exceptions.HTTPError as e:
            print(f"Error fetching audit data: {e}")
            return None
        except Exception as e:
            print(f"Error fetching audit data: {e}")
            return None

    async def fetch_audit_data(self, deviceUid):
        url = f"{self.base_uri}/v2/audit/device/{deviceUid}"

        try:
            response = await self.session.get(url)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Error: {err}")

        return None

    async def fetch_audited_software(self, deviceUid, page=None, max=None):
        try:
            url = f"{self.base_uri}/v2/audit/device/{deviceUid}/software"
            params = {}
            if page is not None:
                params["page"] = page
            if max is not None:
                params["max"] = max

            response = await self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")
        return None

    async def fetch_alert_data(self, alertUid):
        try:
            url = self.base_uri + "/v2/alert/" + alertUid
            response = await self.session.get(url)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    async def fetch_account_data(self):
        url = self.base_uri + "/v2/account"
        try:
            response = await self.session.get(url)
            response.raise_for_status()
            data = await response.json()
            return data
        except requests.exceptions.HTTPError as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    async def fetch_account_variables(self, page=None, max=None):
        url = self.base_uri + "/v2/account/variables"
        params = {"page": page, "max": max}
        try:
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Error: {err}")
        return None

    async def get_user_records(self, page=None, max=None):
        url = self.base_uri + "/v2/account/users"
        params = {"page": page, "max": max}
        try:
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            data = await response.json()
            return data
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None

    async def fetch_site_records(self, page=None, max=None):
        try:
            url = self.base_uri + "/v2/account/sites"
            params = {"page": page, "max": max}
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            json_response = await response.json()
            return json_response
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Something went wrong:", err)
        return None

    async def get_devices(self, page=None, max=None, filterId=None):
        url = self.base_uri + "/v2/account/devices"
        params = {"page": page, "max": max, "filterId": filterId}
        try:
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            data = await response.json()
            return data
        except requests.exceptions.HTTPError as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    async def fetch_components(self, page=None, max=None):
        url = self.base_uri + "/v2/account/components"
        params = {}
        if page is not None:
            params["page"] = page
        if max is not None:
            params["max"] = max

        try:
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")

        return None

    async def fetch_resolved_alerts(self, page=None, max=None, muted=None):
        try:
            params = {}
            if page is not None:
                params["page"] = page
            if max is not None:
                params["max"] = max
            if muted is not None:
                params["muted"] = muted

            url = self.base_uri + "/v2/account/alerts/resolved"
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            return await response.json()
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Error:", err)
        return None

    async def fetch_open_alerts(self, page=None, max=None, muted=None):
        url = self.base_uri + "/v2/account/alerts/open"
        params = {"page": page, "max": max, "muted": muted}
        try:
            response = await self.session.get(url, params=params)
            response.raise_for_status()
            json_response = await response.json()
            return json_response
        except Exception as e:
            print(f"Error fetching open alerts: {e}")
            return None
