# Copyright 2016 Red Hat, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_config import cfg
from oslo_log import log


service_opts = [
    cfg.StrOpt('join_listen',
               default="0.0.0.0",
               help='IP address to listen on'),
    cfg.PortOpt('join_listen_port',
                default=9090,
                help='Port to listen on'),
    cfg.StrOpt('url', default=None,
               help='IPA JSON RPC URL (e.g. '
                    'https://ipa.host.domain/ipa/json)'),
    cfg.StrOpt('keytab', default='/etc/krb5.keytab',
               help='Kerberos client keytab file'),
    cfg.StrOpt('service_name', default=None,
               help='HTTP IPA Kerberos service name '
                    '(e.g. HTTP@ipa.host.domain)'),
    cfg.StrOpt('domain', default='test',
               help='Domain for new hosts'),
    cfg.IntOpt('connect_retries', default=1,
               help='How many times to attempt to retry '
               'the connection to IPA before giving up'),
    cfg.BoolOpt('project_subdomain', default=False,
                help='Treat the project as a DNS subdomain '
                'so a hostname would take the form: '
                'instance.project.domain'),
    cfg.BoolOpt('normalize_project', default=True,
                help='Normalize the project name to be a valid DNS label'),
]


#CONF = cfg.ConfigOpts()
CONF = cfg.CONF
CONF.register_opts(service_opts)
log.register_options(CONF)

#    CONF(sys.argv[1:], project='join', version='1.0.0')
#    log.setup(CONF, 'join')
#    launcher = process_launcher()
#    server = WSGIService('join')
#    launcher.launch_service(server, workers=server.workers)
#    launcher.wait()
#
#
#if __name__ == '__main__':
#    main()