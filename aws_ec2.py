from __future__ import annotations
from typing import List
from pydantic import BaseModel, StrictStr as strr
from pprint import pprint as pp


AWS_DATA = {
    "_id": "instanceIdtest",
    "organization": "5dxxxxxxxxxxxxxxx",
    "accountID": "5dxxxxxxxxxxxxxxx",
    "provider": "aws",
    "entity_type": "vms",
    "checksum": "798128734612770711",
    "data": {
        "tagSet": {
            "item": [
                {
                    "value": "xxxxx",
                    "key": "aws:cloudformation:stack-name"
                }
            ]
        },
        "privateIpAddress": "172.31.50.253",
        "blockDeviceMapping": {
            "item": [
                {
                    "deviceName": "/dev/xvda",
                    "ebs": {
                        "volumeId": "vol-xxxxxxxx",
                        "status": "attached",
                        "attachTime": "2018-05-23T11:17:22.000Z",
                        "deleteOnTermination": "true"
                    }
                }
            ]
        },
        "vpcId": "vpc-xxxxxxxx",
        "placement": {
            "groupName": "",
            "tenancy": "default",
            "availabilityZone": "us-east-1a"
        },
        "subnetId": "subnet-xxxxxxxx",
        "amiLaunchIndex": "0",
        "productCodes": "",
        "instanceType": "t2.small",
        "ipAddress": "54.242.140.130",
        "cpuOptions": {
            "coreCount": "1",
            "threadsPerCore": "1"
        },
        "reason": "",
        "keyName": "Aniruddha",
        "monitoring": {
            "state": "disabled"
        },
        "sourceDestCheck": "true",
        "rootDeviceName": "/dev/xvda",
        "imageId": "iaxxxxxxxx",
        "privateDnsName": "testdnsname",
        "capacityReservationSpecification": {
            "capacityReservationPreference": "open"
        },
        "hibernationOptions": {
            "configured": "false"
        },
        "launchTime": "2019-08-05T12:18:02.000Z",
        "ebsOptimized": "false",
        "instanceState": {
            "code": "16",
            "name": "running"
        },
        "virtualizationType": "hvm",
        "rootDeviceType": "ebs",
        "enclaveOptions": {
            "enabled": "false"
        },
        "dnsName": "ec2-54-242-140-130.compute-1.amazonaws.com",
        "groupSet": {
            "item": {
                "groupId": "sg-xxxxxxxx",
                "groupName": "default"
            }
        },
        "clientToken": "servixxxxxxxx",
        "hypervisor": "xen",
        "networkInterfaceSet": {
            "item": {
                "privateDnsName": "ip-xxxxxxxx",
                "sourceDestCheck": "true",
                "attachment": {
                    "status": "attached",
                    "attachTime": "2018-05-23T11:17:21.000Z",
                    "deleteOnTermination": "true",
                    "attachmentId": "eni-attach-xxxxxxxx",
                    "deviceIndex": "0"
                },
                "interfaceType": "interface",
                "vpcId": "vpc-xxxxxxxx",
                "status": "in-use",
                "macAddress": "12:xxxxxxxx",
                "privateIpAddress": "172.31.50.253",
                "groupSet": {
                    "item": {
                        "groupId": "sg-xxxxxxxx",
                        "groupName": "default"
                    }
                },
                "ipv6AddressesSet": "",
                "networkInterfaceId": "eni-xxxxxxxx",
                "description": "",
                "ownerId": "88xxxxxxxx",
                "association": {
                    "publicIp": "54.242.140.130",
                    "publicDnsName": "ec2-54-242-140-130.compute-1.amazonaws.com",
                    "ipOwnerId": "xxxxxxxx"
                },
                "privateIpAddressesSet": {
                    "item": {
                        "primary": "true",
                        "association": {
                            "publicIp": "54.xxxxxxxx",
                            "publicDnsName": "ec2-xxxxxxxx.compute-1.amazonaws.com",
                            "ipOwnerId": "xxxxxxxx"
                        },
                        "privateIpAddress": "172.xxxxxxxx",
                        "privateDnsName": "ip-xxxxxxxx.ec2.internal"
                    }
                },
                "subnetId": "subnet-xxxxxxxx"
            }
        },
        "instanceId": "xxxxxxxx",
        "architecture": "x86_64"
    }
}




class ItemItem(BaseModel):
    value: strr
    key: strr


class TagSet(BaseModel):
    item: List[ItemItem]


class Ebs(BaseModel):
    volumeId: strr
    status: strr
    attachTime: strr
    deleteOnTermination: strr


class ItemItem1(BaseModel):
    deviceName: strr
    ebs: Ebs


class BlockDeviceMapping(BaseModel):
    item: List[ItemItem1]


class Placement(BaseModel):
    groupName: strr
    tenancy: strr
    availabilityZone: strr


class CpuOptions(BaseModel):
    coreCount: strr
    threadsPerCore: strr


class Monitoring(BaseModel):
    state: strr


class CapacityReservationSpecification(BaseModel):
    capacityReservationPreference: strr


class HibernationOptions(BaseModel):
    configured: strr


class InstanceState(BaseModel):
    code: strr
    name: strr


class EnclaveOptions(BaseModel):
    enabled: strr


class Item(BaseModel):
    groupId: strr
    groupName: strr


class GroupSet(BaseModel):
    item: Item


class Attachment(BaseModel):
    status: strr
    attachTime: strr
    deleteOnTermination: strr
    attachmentId: strr
    deviceIndex: strr


class Item2(BaseModel):
    groupId: strr
    groupName: strr


class GroupSet1(BaseModel):
    item: Item2


class Association(BaseModel):
    publicIp: strr
    publicDnsName: strr
    ipOwnerId: strr


class Association1(BaseModel):
    publicIp: strr
    publicDnsName: strr
    ipOwnerId: strr


class Item3(BaseModel):
    primary: strr
    association: Association1
    privateIpAddress: strr
    privateDnsName: strr


class PrivateIpAddressesSet(BaseModel):
    item: Item3


class Item1(BaseModel):
    privateDnsName: strr
    sourceDestCheck: strr
    attachment: Attachment
    interfaceType: strr
    vpcId: strr
    status: strr
    macAddress: strr
    privateIpAddress: strr
    groupSet: GroupSet1
    ipv6AddressesSet: strr
    networkInterfaceId: strr
    description: strr
    ownerId: strr
    association: Association
    privateIpAddressesSet: PrivateIpAddressesSet
    subnetId: strr


class NetworkInterfaceSet(BaseModel):
    item: Item1


class Data(BaseModel):
    tagSet: TagSet
    privateIpAddress: strr
    blockDeviceMapping: BlockDeviceMapping
    vpcId: strr
    placement: Placement
    subnetId: strr
    amiLaunchIndex: strr
    productCodes: strr
    instanceType: strr
    ipAddress: strr
    cpuOptions: CpuOptions
    reason: strr
    keyName: strr
    monitoring: Monitoring
    sourceDestCheck: strr
    rootDeviceName: strr
    imageId: strr
    privateDnsName: strr
    capacityReservationSpecification: CapacityReservationSpecification
    hibernationOptions: HibernationOptions
    launchTime: strr
    ebsOptimized: strr
    instanceState: InstanceState
    virtualizationType: strr
    rootDeviceType: strr
    enclaveOptions: EnclaveOptions
    dnsName: strr
    groupSet: GroupSet
    clientToken: strr
    hypervisor: strr
    networkInterfaceSet: NetworkInterfaceSet
    instanceId: strr
    architecture: strr


class Model(BaseModel):
    _id: strr
    organization: strr
    accountID: strr
    provider: strr
    entity_type: strr
    checksum: strr
    data: Data


aws = Model(**AWS_DATA)
pp(aws.organization)
#pp(aws.dict())
