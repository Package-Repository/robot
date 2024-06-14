#!/usr/bin/env python3

from vision_main import VideoRunner
from services import ServiceNames, ServicePorts
from gen_srv import start_generic_server

if __name__ == "__main__":
    start_generic_server(ServiceNames.SPEAK, ServicePorts[ServiceNames.SPEAK], VideoRunner)
