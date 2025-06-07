#!/bin/sh
until pg_isready -h db -U user -d mydb; do
  echo "Waiting for PostgreSQL to be ready..."
  sleep 1
done

echo "PostgreSQL is ready!"