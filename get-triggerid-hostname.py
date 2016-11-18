#!/usr/bin/python
import sys
import logging
from pyzabbix import ZabbixAPI

#for debug
#stream = logging.StreamHandler(sys.stdout)
#stream.setLevel(logging.DEBUG)
#log = logging.getLogger('pyzabbix')
#log.addHandler(stream)
#log.setLevel(logging.DEBUG)

zapi = ZabbixAPI("http://zabbix.example.com")
zapi.login('zabbix','zabbix')
#Servers
#templateid - шаблон с триггером о недостопности узла сети
for trigger in zapi.trigger.get(groupids="13",filter={"templateid": "13836"}):
    for host in zapi.host.get(triggerids=trigger['triggerid']):
	print(host['name'], trigger['triggerid'])
#voip
for trigger in zapi.trigger.get(groupids="14"):
    for host in zapi.host.get(triggerids=trigger['triggerid']):
	print(host['name'], trigger['triggerid'])
