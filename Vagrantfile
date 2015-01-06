Vagrant.configure(2) do |config|
  config.vm.box = 'chef/fedora-20'

  config.vm.provision :shell, path: 'deploy/bootstrap.sh', args: "#{ENV['SUPERUSER_PASSWORD']}"

  config.vm.define 'testing', primary: true do |test|
    test.vm.network :forwarded_port, host: 4567, guest: 80
  end

  config.vm.define 'production' do |production|
    production.vm.hostname = 'craigle.us'

    production.vm.box = 'digital_ocean'
    production.vm.box_url = "https://github.com/smdahlen/vagrant-digitalocean/raw/master/box/digital_ocean.box"

    production.vm.provider :digital_ocean do |provider, override|
      override.ssh.username = 'sonny'
      override.ssh.private_key_path = '~/.ssh/id_rsa'
      override.ssh.pty = true

      provider.token = File.read(File.expand_path('~/.digitalocean_token'))

      provider.image = 'fedora-20-x64'
      provider.region = 'nyc3'
      provider.size = '512mb'
    end
  end
end
