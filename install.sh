#!/bin/bash


set -e

pip install .
cat > /bin/start_tomato.sh << EOF
tomato
EOF

chmod +x /bin/start_tomato.sh

cp etc/init.d/tomato /etc/init.d/tomato
update-rc.d tomato defaults
