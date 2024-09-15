#!/bin/bash

# Define file paths
INIT_FILE="torchcam/__init__.py"
TOML_FILE="pyproject.toml"

# Extract version from __init__.py
init_version=$(grep -oP '__version__ = "\K[^"]+' "${INIT_FILE}")
if [ -z "$init_version" ]; then
    echo "Version not found in $INIT_FILE"
    exit 1
fi

# Extract version from pyproject.toml
toml_version=$(grep -oP '^version = "\K[^"]+' "${TOML_FILE}")
if [ -z "${toml_version}" ]; then
    echo "Version not found in ${TOML_FILE}"
    exit 1
fi

# Compare versions
if [ "$init_version" == "${toml_version}" ]; then
    echo "Versions match: ${toml_version}"
else
    echo "Version mismatch:"
    echo "${INIT_FILE}=${init_version}"
    echo "${TOML_FILE}=${toml_version}"
    exit 1
fi
