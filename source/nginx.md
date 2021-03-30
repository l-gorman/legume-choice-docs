# Server

LegumeCHOICE uses an NGINX server. A proxy server has been configured to pass requests to the [API](api.md). All of the configuration for the NGINX server can be found in the default sites-enabled. On the legumeCHOICE VM, this file can be found at:

`/etc/nginx/sites-available/default`

The SSL certificate was obtained using letsencrypt, using this [guide](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04).

Files for [public data](public-data.md) and [private data](administrators.md) are made available using NGINX auto-index. The administrator files are secured with HTTP basic authentication. See [here](https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/) for how authentication was implemented, and how to add new users/passwords.
