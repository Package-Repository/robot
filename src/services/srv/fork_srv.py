#!/usr/bin/env python3

from forker import Forker
from services import ServiceNames, ServicePorts
from gen_srv import start_generic_server

if __name__ == "__main__":
    start_generic_server(ServiceNames.YOLO, ServicePorts[ServiceNames.YOLO], Forker)
