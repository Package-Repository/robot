#!/usr/bin/env python3

from client import call_service
from services import ServiceNames, ServicePorts
from req_resp import GenericRequest

def recieveData():
    return call_service(port=ServicePorts[ServiceNames.DVL], 
                request=GenericRequest(
                    function="recieveData", 
                    args={}
    ))

if __name__ == "__main__":
    print(recieveData())
