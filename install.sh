pip install .
cat > /bin/start_tomato.sh << EOF
#!/bin/sh
tomato
EOF

chmod +x /bin/start_tomato.sh
chown qing /bin/start_tomato.sh

cp etc/init.d/tomato /etc/init.d/tomato
update-rc.d tomato defaults
