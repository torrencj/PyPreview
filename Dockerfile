FROM python:3
WORKDIR /app
ADD . /app

ENV CHROME_DRIVER_VERSION 2.34

# Install xvfb
RUN apt-get update -y -q
RUN apt-get install -y -q unzip xvfb

# Install Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update
RUN apt-get -y install google-chrome-stable

# Install requirements for chromedriver
# RUN apt install libfontconfig
RUN apt-get -y install libxi6 libgconf-2-4

# Install Chromedriver
RUN wget -N http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -P ~/
RUN unzip ~/chromedriver_linux64.zip -d ~/
RUN rm ~/chromedriver_linux64.zip
RUN mv -f ~/chromedriver /usr/local/bin/chromedriver
RUN chown root:root /usr/local/bin/chromedriver
RUN chmod 0755 /usr/local/bin/chromedriver

# Install requirements.txt via pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Open ports 80 and 443, then run the app
EXPOSE 80
EXPOSE 443
CMD ["python", "app.py"]
