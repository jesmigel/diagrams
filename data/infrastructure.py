from diagrams import Cluster, Diagram
from diagrams.onprem.network import Nginx
from diagrams.oci.security import IDAccess
from diagrams.programming.language import Php, Go
from diagrams.onprem.vcs import Gitlab
from diagrams.generic.storage import Storage
from diagrams.generic.virtualization import Vmware
from diagrams.onprem.iac import Terraform
from diagrams.onprem.ci import Jenkins
from diagrams.generic.os import Ubuntu
from diagrams.oci.storage import FileStorage
from diagrams.generic.network import Switch

with Diagram("infrastructure", show=False):
    switch = Switch("FM Switch")
    with Cluster("Platform Controller"):
        # NGINX
        proxy = Nginx("NGINX proxy")
        # IAM
        with Cluster("IAM"):
            # OpenLDAP
            ldap = IDAccess("OpenLDAP")
            # ldap-user-manager
            ldap_gui = Php("ldap-user-manager")

        repo = [
            Storage("Portainer"),
            Gitlab("Gitlab"),
            Storage("Nexus")
        ]

        # Jenkins
        ci = Jenkins("Jenkins")

        # LDAP DEPENDENCY
        ldap_gui << ldap
        repo << ldap
        ci << ldap

        # PUBLIC FACING PROXY
        ldap_gui << proxy
        repo << proxy
        ci << proxy


    with Cluster("File Storage Host"):
        nfsv4 = [
            FileStorage("ESXI Datastore"),
            FileStorage("Packer RAW images"),
            FileStorage("Controller configuration and Data files")
        ]


    ci << repo
    repo << nfsv4[2]    
    proxy << nfsv4[2]
    switch << proxy


    with Cluster("ESXI Host"):
        # ESXI Host
        esxi = Vmware("ESXI")
        # Terraform
        tf = Terraform("Terraform")
        tf << ci

        with Cluster("K8s (Kubespray) - Ubuntu VM's"):
            control = Ubuntu("Control plane")
            control - Ubuntu("Worker")


        with Cluster("OpenStack - Ubuntu VM's"):
            openstack = Ubuntu("DevStack")


        # ESXI external interactions
        esxi << tf
        esxi << proxy
        esxi << nfsv4[0]
        esxi << repo[0]

        # K8s interaction with controller
        control << repo
        control << esxi

        # K8s interaction with controller
        openstack << repo
        openstack << esxi
        




