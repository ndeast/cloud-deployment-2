"""
Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item. 
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

link = request.LAN("lan")
 
# Create 4 XenVMs
for i in range(4):
    node = request.XenVM("node-" + i+1)
    iface = node.addInterface("if" + i+1)
    
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"

    iface.component_id = "eth" + i+1
    iface.addAddress(rspec.IPv4Address("192.168.1." + i+1, "255.255.255.0"))

    link.addInterface(iface)

    if(i == 0):
        # Set public IP address
        node.routable_control_ip = "true"
        # Install and execute a script that is contained in the repository.
        node.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))


# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
