#!/bin/bash

# Environment setup
export AVL_ROOT=$(dirname $(realpath "${BASH_SOURCE[0]}"))

# Verilator setup
if ! command -v verilator --help &> /dev/null
then
    echo "Verilator could not be found. Please install Verilator and ensure it is in your PATH (see https://verilator.org/guide/latest/install.html)."
    return 1
fi

# GTKWave setup
if ! command -v gtkwave --help &> /dev/null
then
    echo "GTKWave could not be found. Please install GTKWave and ensure it is in your PATH (see http://gtkwave.sourceforge.net/)."
    return 1
fi

# Graphviz setup
if ! command -v dot --help &> /dev/null
then
    echo "Graphviz could not be found. Please install Graphviz and ensure it is in your PATH (see https://graphviz.org/download/)."
    return 1
fi

# Python setup

pushd $AVL_ROOT 1>/dev/null

python_packages=(\
.[dev]
)

python3 -m venv venv
source ./venv/bin/activate
for p in ${python_packages[@]}; do
    python3 -m pip install --editable $p
done

popd 1>/dev/null

# Default Simulation setup
export PYTHONPATH=${PYTHONPATH}
export SIM=verilator
export TOPLEVEL_LANG=verilog
