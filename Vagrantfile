Vagrant.configure(2) do |config|
  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.provision :shell, path: 'deploy/bootstrap.sh'

  config.vm.define 'testing', primary: true do |test|
    test.vm.box = 'chef/fedora-20'
    test.vm.network :forwarded_port, host: 4567, guest: 80
  end

  config.vm.define 'production' do |production|
    production.vm.hostname = 'craigle.us'

    production.ssh.private_key_path = '~/.ssh/id_rsa'
    production.ssh.username = 'sonny'
    production.ssh.pty = true

    production.vm.box = 'digital_ocean'
    production.vm.box_url = "https://github.com/smdahlen/vagrant-digitalocean/raw/master/box/digital_ocean.box"

    production.vm.provider :digital_ocean do |provider, _|
      provider.token = File.read(File.expand_path('~/.digitalocean_token'))

      provider.image = 'fedora-20-x64'
      provider.region = 'nyc3'
      provider.size = '512mb'

      provider.backups_enabled = false
    end
  end
end
