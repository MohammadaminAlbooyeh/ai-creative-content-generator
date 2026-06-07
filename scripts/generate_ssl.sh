#!/bin/bash
set -euo pipefail

CERTS_DIR="$(dirname "$0")/../certs"
mkdir -p "$CERTS_DIR"

if [ -f "$CERTS_DIR/fullchain.pem" ] && [ -f "$CERTS_DIR/privkey.pem" ]; then
    echo "SSL certificates already exist in $CERTS_DIR"
    exit 0
fi

echo "Generating self-signed SSL certificates in $CERTS_DIR..."

openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout "$CERTS_DIR/privkey.pem" \
    -out "$CERTS_DIR/fullchain.pem" \
    -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost" 2>/dev/null

openssl dhparam -out "$CERTS_DIR/dhparam.pem" 2048 2>/dev/null

echo "SSL certificates generated successfully"
echo "  fullchain.pem - Certificate"
echo "  privkey.pem   - Private key"
echo "  dhparam.pem   - Diffie-Hellman parameters"
