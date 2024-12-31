export VENV=test_cicd_venv

if [ ! -d "$VENV" ]; then
    python3 -m venv $VENV
fi

source $VENV/bin/activate
pip3 install -r requirements.txt

echo "run this to activate virtual environment of python"
echo "source $VENV/bin/activate"
