# By default, start from the base STK Engine image
ARG baseImage=ansys/stk:latest-ubuntu22.04
FROM ${baseImage}

# Install system dependencies
USER root
RUN set -e; \
    # Install basic development utilities
    apt-get install -y build-essential; \
    apt-get install -y tar wget; \
    # Install OpenSSL 1.1 dependencies
    # Install required dependencies for Python 3.X
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y pkg-config \
          libbz2-dev libffi-dev libgdbm-dev libgdbm-compat-dev liblzma-dev \
            libncurses5-dev libreadline6-dev libsqlite3-dev libssl-dev \
            lzma lzma-dev tk-dev uuid-dev zlib1g-dev; \
    # Clean all unnecessary files
    apt-get clean;

# Install OpenSSL 1.1
RUN set -e; \
   wget --no-check-certificate https://ftp.openssl.org/source/openssl-1.1.1k.tar.gz; \
   tar -xzvf openssl-1.1.1k.tar.gz; \
   cd openssl-1.1.1k; \
   ./config --prefix=/tmp/openssl no-shared zlib-dynamic; \
   make && make install_sw;

CMD echo 'Extend this container by installing Python.'
