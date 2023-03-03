# By default, start from the base STK Engine image
ARG baseImage=ansys/stk:latest-centos7
FROM ${baseImage}

# Install system dependencies
USER root
RUN set -e; \

    # Install basic system utilities
    yum -y install make gcc perl-core pcre-devel wget zlib-devel; \

    # Install required dependencies for Python 3.X
    yum -y install libffi-devel zlib-devel bzip2-devel ncurses-devel sqlite-devel; \
    yum -y install readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel; \
    # yum -y install python3-tkinter python3.10-tkinter; \
    yum -y install epel-release openssl11 openssl11-libs openssl11-devel; \
    yum clean all; \
    rm -rf /var/cache/yum

# Install OpenSSL 1.1
RUN set -e; \
   yum install -y make gcc perl-core pcre-devel wget zlib-devel; \
   wget --no-check-certificate https://ftp.openssl.org/source/openssl-1.1.1k.tar.gz; \
   tar -xzvf openssl-1.1.1k.tar.gz; \
   cd openssl-1.1.1k; \
   ./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib no-shared zlib-dynamic; \
   make && make install; \
   echo "export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:${LD_LIBRARY_PATH}" > /etc/profile.d/openssl.sh; \
   echo "export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:${LD_LIBRARY_PATH}" >> .bashrc


# Install Python 3.10 and generate alias to it
RUN cd /tmp && \
    wget https://www.python.org/ftp/python/3.10.10/Python-3.10.10.tgz && \
    tar xzf Python-3.10.10.tgz && \
    cd Python-3.10.10 && \
    ./configure --enable-optimizations && \
    make altinstall && \
    ln -sfn /usr/local/bin/python3.10 /usr/bin/python && \
    ln -sfn /usr/local/bin/pip3.10 /usr/bin/pip

# Switch back to non-root user
USER stk

# Update the path to include Python executables
ENV PATH="${STK_USER_HOME}/.local/bin:${PATH}" \
    PIP_DEFAULT_TIMEOUT=600 \
    PIP_RETRY=50

ENTRYPOINT [ "python3.10" ]
