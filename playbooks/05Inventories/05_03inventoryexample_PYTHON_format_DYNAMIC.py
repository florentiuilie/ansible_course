#!/usr/bin/env python3
import json

inventory = {
    "webservers": {
        "hosts": ["web1.example.com", "web2.example.com"],
        "vars": {
            "ansible_user": "admin"
        }
    },
    "dbservers": {
        "hosts": ["db1.example.com", "db2.example.com"],
        "vars": {
            "ansible_user": "dbadmin"
        }
    },
    "_meta": {
        "hostvars": {
            "web1.example.com": {"ansible_host": "192.168.1.10", "http_port": 80},
            "web2.example.com": {"ansible_host": "192.168.1.11", "http_port": 8080},
            "db1.example.com": {"ansible_host": "192.168.1.20", "db_name": "prod_db"},
            "db2.example.com": {"ansible_host": "192.168.1.21", "db_name": "test_db"}
        }
    }
}

print(json.dumps(inventory))
