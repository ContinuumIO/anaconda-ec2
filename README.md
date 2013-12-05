Anaconda-EC2
============
Anaconda Plug-in for StarCluster

http://continuum.io/blog/blog/starcluster-anaconda/

Installation
============

    $ pip install StarCluster
    $ git clone git://github.com/ContinuumIO/anaconda-ec2.git
    $ mkdir -p $HOME/.starcluster/plugins
    $ cp anaconda-ec2/config.anaconda $HOME/.starcluster/config
    $ cp anaconda-ec2/anaconda_plugin.py $HOME/.starcluster/plugins

Then edit `$HOME/.starcluster/config` and enter your credentials, keypair, and region settings. You can check your settings before launch using:

    $ starcluster start --validate-only myconda

Assuming this command doesnt return any errors you should be ready to launch a cluster:

    $ starcluster start myconda

Changes to StarCluster Config
=============================

The Anaconda StarCluster config uses the Anaconda AMIs:

* AMI US-EAST-1 = ami-63bb2c0a (Anaconda 1.3)
* AMI US-WEST-2: ami-a4d64194 (Anaconda 1.4)

All versions of Anaconda on the Anaconda AMIs can be upgrade with the following commands:

    $ conda update conda
    $ conda update anaconda

The Anaconda StarCluster config defines and configures the necessary plugin and permission sections for Anaconda:

    [plugin anaconda_plugin]
    SETUP_CLASS = anaconda_plugin.ConfigAnaconda

    [permission disco]
    FROM_PORT = 8989
    TO_PORT = 8989

    [cluster smallcluster]
    ...
    PLUGINS = anaconda_plugin 
    PERMISSIONS = disco
