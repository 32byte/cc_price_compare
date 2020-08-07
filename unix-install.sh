#!/bin/bash
#
#              _           _           _        _ _ 
#  _   _ _ __ (_)_  __    (_)_ __  ___| |_ __ _| | |
# | | | | '_ \| \ \/ /____| | '_ \/ __| __/ _` | | |
# | |_| | | | | |>  <_____| | | | \__ \ || (_| | | |
#  \__,_|_| |_|_/_/\_\    |_|_| |_|___/\__\__,_|_|_|
# 
####################################################

datadir='/usr/lib/cc_price_compare'
installcli='/usr/bin/cc_price_cli'
installgui='/usr/bin/cc_price_gui'

clean () {
    echo "Cleaning..."
    rm -rf $datadir
    rm -f $installcli
    rm -f $installgui
    echo "done!"
}

if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit
fi

if [ $# -gt 0 ] && [ $1 == "uninstall" ]; then
    clean
    exit
fi

if [ ! -d "$datadir" ]; then
    git clone https://github.com/32byte/cc_price_compare.git $datadir
fi

if [ $# -gt 0 ] && [ $1 == "update" ]; then
    cd $datadir &&
    echo "Updating..."
    git pull
    echo "done!"
    exit
fi

pip3 install -r $datadir/requirements.txt &&

echo "#!/bin/bash" > $installcli &&
echo "python3 /usr/lib/cc_price_compare/cli.py \"\$@\"" >> $installcli &&
chmod +x $installcli &&

echo "#!/bin/bash" > $installgui &&
echo "python3 /usr/lib/cc_price_compare/gui.py \"\$@\"" >> $installgui &&
chmod +x $installgui &&

echo "Installed successfully" ||
( echo "There was an error!" && clean )