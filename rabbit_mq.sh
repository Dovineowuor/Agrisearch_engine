#! usr/bin/bash
sudo rabbitmqctl add_user explorer password
sudo rabbitmqctl set_user_tags explorer administrator
sudo rabbitmqctl set_permissions -p / explorer ".*" ".*" ".*"