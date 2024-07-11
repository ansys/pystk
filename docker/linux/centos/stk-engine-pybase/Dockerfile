# By default, start from the base STK Engine image
ARG baseImage=ansys/stk:dev-centos7
FROM ${baseImage}

# Install system dependencies
USER root
RUN set -e; \

    # Install basic development utilities
    # Install devtoolset-10 to install later version of gcc needed for Python 3.11
    # (https://github.com/python/cpython/issues/94825)
    yum groupinstall -y development; \
    yum install -y centos-release-scl; \
    yum -y install devtoolset-10 make tar wget; \

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
   wget --no-check-certificate https://www.openssl.org/source/openssl-1.1.1w.tar.gz; \
   tar -xzvf openssl-1.1.1w.tar.gz; \
   cd openssl-1.1.1w; \
   scl enable devtoolset-10 "./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib no-shared zlib-dynamic"; \
   scl enable devtoolset-10 "make && make install"; \
   echo "export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:${LD_LIBRARY_PATH}" > /etc/profile.d/openssl.sh; \
   echo "export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:${LD_LIBRARY_PATH}" >> .bashrc


CMD ["echo", "Extend this container by installing Python."]

USER stk