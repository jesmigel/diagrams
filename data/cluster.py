from diagrams import Cluster, Diagram
from diagrams.generic.compute import Rack
from diagrams.onprem.network import Internet
from diagrams.generic.network import Router
from diagrams.generic.network import Switch
from diagrams.onprem.compute import Server
from diagrams.generic.storage import Storage


with Diagram("OnPrem", show=False):
    nbn = Internet("NBN")
    with Cluster("Routers"):
        routers = [
            Router("Main"),
            Router("Extender"),
            Router("Cluster")
        ]
        routers[0] << routers[1] << routers[2]

    with Cluster("Switches"):
        switches = [
            Switch("Fully managed switch"),
            Switch("Unmanaged switch")
        ]

    with Cluster("Dell Poweredge Servers"):
        nodes = [
            Rack("r710:MaaS"),
            Server("r810:ESXI"),
            Server("r710:KVM"),
            Server("r710:UNUSED")
        ]
    nas = Storage("NAS")

    routers[2] << switches[0]
    switches[0] << nas
    switches[0] << nodes
    switches[1] << nodes

    nbn << routers[0]