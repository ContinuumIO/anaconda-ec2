from starcluster.clustersetup import ClusterSetup

DISCO_CONFIG = '/opt/anaconda/var/disco/disco_8989.config'


class ConfigAnaconda(ClusterSetup):

    def __init__(self):
       pass
    # Do the things common to both the run method and the on_add_node
    # methods here.
    def init_node(self, node, master):
        """
        Create the disco directories on the ephemeral storage.
        """
        if node == master:
            node.ssh.execute("touch /media/test-master")
        else:
            pass
            node.ssh.execute("touch /media/test-node")
            
    def config_disco(self, master, nodes):
        """
        Create a disco config file that includes all the nodes and restart disco.
        """
        remote_nodes = filter(lambda n: not n.is_master(), nodes)
        #names = map(lambda n: n.alias, remote_nodes)
        recs = map(lambda n: ',\n["%s", "%d"]' % (n.alias, n.num_processors), remote_nodes)
        body = reduce(lambda x, y: x + y, recs, '')
        dconfig = '[["master", "%d"]' % (master.num_processors,) + body + ']'

        cfd = master.ssh.remote_file(DISCO_CONFIG)
        cfd.write(dconfig)
        cfd.close()
        
        master.ssh.execute("/etc/init.d/disco stop")
        master.ssh.execute("/etc/init.d/disco start")
    
    def config_anaconda(self, master, nodes):
            """
            Create a disco config file that includes all the nodes and restart disco.
            """
            remote_nodes = filter(lambda n: not n.is_master(), nodes)
            names = map(lambda n: n.alias, remote_nodes)
            #recs = map(lambda n: ',\n["%s", "%d"]' % (n.alias, n.num_processors), remote_nodes)
            #body = reduce(lambda x, y: x + y, recs, '')
            #master.ssh.execute("sudo su - disco;")
            master.ssh.execute("/etc/init.d/disco stop")
            
            for node in names:
                print node
                print "scp ~disco/.ssh/id_rsa.pub %s:~disco/.ssh/authorized_keys" % (node)
                
                master.ssh.execute("scp ~disco/.ssh/id_rsa.pub %s:~disco/.ssh/authorized_keys" % (node))
                master.ssh.execute("scp ~disco/.erlang.cookie %s:~disco/" % (node))
                
            
            for node in nodes:
                 node.ssh.execute("chown -R disco:disco ~disco")
                 
            master.ssh.execute("/etc/init.d/disco start")

    def run(self, nodes, master, user, user_shell, volumes):
        for node in nodes:
            self.init_node(node, master)
        self.config_disco(master, nodes)
        self.config_anaconda(master,nodes);
        
        
    def on_add_node(self, node, nodes, master, user, user_shell, volumes):
        self.init_node(node, master)
        
        # What happens to running jobs on a restart?
        self.config_disco(master, nodes)
        self.config_anaconda(master,nodes);
        

    def stop_node(self, node):
        pass

    def on_remove_node(self, node, nodes, master, user, user_shell, volumes):
        self.stop_node(node)

    def on_shutdown(self, nodes, master, user, user_shell, volumes):
        for node in nodes:
            self.stop_node(node)
