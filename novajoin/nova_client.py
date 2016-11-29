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

from novaclient import client
import novaclient.exceptions
from novajoin import keystone_client


NOVA_API_VERSION = 2


def get_client():
    session = keystone_client.get_session()
    return client.Client(NOVA_API_VERSION, session=session)


def get_instance(instance_id):
    client = get_client()
    try:
        return client.servers.get(instance_id)
    except novaclient.exceptions.NotFound:
        return None
