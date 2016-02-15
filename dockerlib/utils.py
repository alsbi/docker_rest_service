# -*- coding: utf-8 -*-
__author__ = 'alsbi'


def template(hostname='', domainname='', images=''):
    return """
{{
       "Hostname": "{hostname}",
       "Domainname": "{domainname}",
       "User": "",
       "AttachStdin": false,
       "AttachStdout": true,
       "AttachStderr": true,
       "Tty": false,
       "OpenStdin": false,
       "StdinOnce": false,
       "Cmd":["date"],
       "Image": "{images}",
       "Volumes": {{
               "/tmp": {{}}
       }},
       "WorkingDir": "",
       "NetworkDisabled": false,
       "MacAddress": "12:34:56:78:4a:bc",
       "ExposedPorts": {{
               "22/tcp": {{}}
       }}
}}
""".format(hostname = hostname, domainname = domainname, images = images)
