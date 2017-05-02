# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.synced_folder ".", "/home/vagrant/project", create: true

  config.vm.provider "virtualbox" do |vb|
    vb.name = "robohead project"
    vb.memory = 512
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision.yml"
  end

end
