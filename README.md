Anaconda-EC2
============

Anaconda Plug-in for StarCluster
http://continuum.io/blog/blog/starcluster-anaconda/

Installation
============

Install StarCluster

In ~/.starcluster/:
   move and rename config.anaconda to config
   move anaconda_plugin.py to .startcluster/plugins



Changes to StarCluster Config
============

Use Anaconda AMI:
* AMI US-EAST-1 = ami-63bb2c0a (Anaconda 1.3)
* AMI US-WEST-2: ami-a4d64194 (Anaconda 1.4)

all versions of Anaconda can be upgrade with the following command:

    >>> conda update conda
    >>> conda update anaconda

Added the Anaconda plugin to the list of used PLUGINS
PLUGINS = anaconda_plugin 
PERMISSIONS = disco

Define the Plugin

[plugin anaconda_plugin]
SETUP_CLASS = anaconda_plugin.ConfigAnaconda

[permission disco]
from_port = 8989
to_port = 8989
