# mysql-selfmanaged

What cloud environment you decided to use?
  - the cloud enviornment I decided to use was GCP

How you set up your VM (what image you selected - imagine writing a brief tutorial to a new user - what would you include and how to quickly and easily set up a new VM) 
  - Naviagte to VM instances to create one 
  - Make sure to give and rename the VM 
  - Enable Http, Https, 
  - e2 medium, Ubuntu 18.04LTS x86/64

The commands you used to setup the OS image (how did you update the OS image? how did you install the mysql)
  - sudo apt-get update
  - sudo apt install mysql-server mysql-client 
  - sudo mysql

What changes you needed to make in order to make the mysql instance available to external computers (config file? opening ports?) 
  - sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf (configure file) 
  - change bind address 0.0.0.0 (external connection)
  - sudo /etc/init.d/mysql restart (to restart program)
  - navigate GCP to create new firewall for port 3306
  
  Upload data on python file 
