Anaconda-EC2
============

Anaconda Plug-in for StarCluster

Installation
============

Install StarCluster

In .starcluster:
   move and renmae config.anaconda to config
   move anaconda_plugin.py to .startcluster/plugins



Changes to StarCluster Config
============

Use Anaconda AMI:
NODE_IMAGE_ID = ami-39298750

Add the Anaconda plugin to the list of used PLUGINS
PLUGINS = anaconda_plugin 

Define the Plugin

[plugin anaconda_plugin]
# myplugin module either lives in ~/.starcluster/plugins or is
# in your PYTHONPATH
SETUP_CLASS = anaconda_plugin.ConfigAnaconda
