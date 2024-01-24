# By default, start from the base STK Engine image
ARG baseImage=ansys/stk:latest-windowsservercore-ltsc2019
FROM ${baseImage}

# Install system dependencies
USER root
RUN set -e; \

    # Install basic development utilities
    yum groupinstall -y development; \
    yum -y install gcc make tar wget; \

    # Install OpenSSL 1.1 dependencies
    yum -y install perl-core pcre-devel; \

    # Install required dependencies for Python 3.X
    yum -y install bzip2-devel libffi-devel tk-devel; \
    yum -y install zlib-devel ncurses-devel sqlite-devel; \
    yum -y install readline-devel gdbm-devel db4-devel libpcap-devel xz-devel; \

    # Clean all unnecessary files
    yum clean all; \
    rm -rf /var/cache/yum

# Install OpenSSL 1.1
RUN set -e; \
   wget --no-check-certificate https://ftp.openssl.org/source/openssl-1.1.1k.tar.gz; \
   tar -xzvf openssl-1.1.1k.tar.gz; \
   cd openssl-1.1.1k; \
   ./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib no-shared zlib-dynamic; \
   make && make install; \
   echo "export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:${LD_LIBRARY_PATH}" > /etc/profile.d/openssl.sh; \
   echo "export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:${LD_LIBRARY_PATH}" >> .bashrc


CMD echo 'Extend this container by installing Python.'
