#!/bin/bash
# Zix
# SSH with password and IP address is for l00sers
# This is so you can link a name to the address (like DNS)
# It also does key gen stuff so you don't have to enter password to login to host anymore


if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <hostname> <ip_address>"
    exit 1
fi

HOSTNAME=$1
IP_ADDRESS=$2

if ! grep -q "$HOSTNAME" /etc/hosts; then
    echo "$IP_ADDRESS $HOSTNAME" | sudo tee -a /etc/hosts > /dev/null
    echo "Added $HOSTNAME to /etc/hosts"
else
    echo "Entry for $HOSTNAME already exists in /etc/hosts"
fi

SSH_KEY="$HOME/.ssh/id_rsa"
if [ ! -f "$SSH_KEY" ]; then
    ssh-keygen -t rsa -N "" -f "$SSH_KEY"
fi

ssh-copy-id "$USER@$IP_ADDRESS"

echo "Setup complete. You can now SSH into $IP_ADDRESS without a password."
