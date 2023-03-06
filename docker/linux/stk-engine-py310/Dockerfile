# By default, start from the base STK Engine image
ARG baseImage=ansys/stk:latest-centos7
FROM ${baseImage}

# Install system dependencies
USER root
RUN set -e; \

    # Install basic development utilities
    yum groupinstall -y development; \
    yum -y install gcc make tar wget; \

    # Install OpenSSL 1.1 (required for Python >= 3.10) dependencies
    yum -y perl-core pcre-devel; \

    # Install required dependencies for Python 3.X
    yum -y install bzip2-devel libffi-devel tk-devel; \
    yum -y install libffi-devel zlib-devel ncurses-devel sqlite-devel; \
    yum -y install readline-devel gdbm-devel db4-devel libpcap-devel xz-devel; \

    # Clean all unnecessary files
    yum clean all; \
    rm -rf /var/cache/yum

# Install OpenSSL 1.1 (required by Python >= 3.10)
RUN set -e; \
   wget --no-check-certificate https://ftp.openssl.org/source/openssl-1.1.1k.tar.gz; \
   tar -xzvf openssl-1.1.1k.tar.gz; \
   cd openssl-1.1.1k; \
   ./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib no-shared zlib-dynamic; \
   make && make install; \
   echo "export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:${LD_LIBRARY_PATH}" > /etc/profile.d/openssl.sh; \
   echo "export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:${LD_LIBRARY_PATH}" >> .bashrc


# Install Python 3.10 and create a symbolic link named "python".
# This overrides the default Python 2.7 in CentOS7.
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
