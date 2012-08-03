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
NODE_IMAGE_ID = ami-39298750

Added the Anaconda plugin to the list of used PLUGINS
PLUGINS = anaconda_plugin 

Define the Plugin

[plugin anaconda_plugin]
SETUP_CLASS = anaconda_plugin.ConfigAnaconda
