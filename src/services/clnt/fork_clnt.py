#!/usr/bin/env python3

from client import call_service
from services import ServiceNames, ServicePorts
from req_resp import GenericRequest

def fork(script: str):
    call_service(port=ServicePorts[ServiceNames.FORK], 
                request=GenericRequest(
                    function="run_script", 
                    args={"script": script}
    ))

if __name__ == "__main__":
    fork("server.py")