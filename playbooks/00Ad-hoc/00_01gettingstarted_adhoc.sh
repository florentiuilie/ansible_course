#!/bin/sh
ansible all -m ping
ansible webserver -m copy -a "src=/path/to/local/file.txt dest=/path/to/remote/file.txt"
ansible webservers -m yum -a "name=nginx state=present"
ansible webservers -m apt -a "name=nginx state=present"
ansible dbservers -m file -a "path=/testdir state=directory"
ansible all -m shell -a "cat /var/log/messages | grep 'Apache HTTP Server'"
ansible all -m setup
ansible webservers -m service -a "name=httpd state=restarted"
ansible all -m user -a "name=username state=present"
ansible all -m shell -a "df -h"
ansible webservers -b -m shell -a "yum update"

