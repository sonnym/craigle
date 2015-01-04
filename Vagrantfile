Vagrant.configure(2) do |config|
  config.vm.box = 'chef/fedora-20'
  config.vm.provision :shell, path: 'deploy/bootstrap.sh'

  config.vm.network :forwarded_port, host: 4567, guest: 80
end
