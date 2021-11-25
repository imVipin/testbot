if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Esther-Lopez/FindPDFbot.git /FindPDFbot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /FindPDFbot
fi
cd /FindPDFbot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
