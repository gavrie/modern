wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key |  apt-key add -

line="deb http://pkg.jenkins-ci.org/debian binary/"; [[ -n $(grep "^$line\$" /etc/apt/sources.list) ]] && echo "jenkins fixed" || echo "$line" >> /etc/apt/sources.list

apt-get update
