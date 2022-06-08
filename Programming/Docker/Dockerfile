# A Dockerfile is a script that contains all commands for building a Docker image. 
# The Dockerfile contains all instructions that will be used to create the Docker image with the 'docker build' command.

# And from an image we can build containers that is specially designed for our needs.

# Here is some of the most used instructions you can use:

# FROM
# Set the base-image for the new image that you want to create. The FROM instruction will initialize the new build-stage and must be located at the top of the Dockerfile.

# LABEL
# With this instruction, you can add additional information about your Docker image, such as the version, description, maintainer, etc. The LABEL instruction is a key-value pair that allows you to add multiple labels and multi-line values.

# RUN
# This instruction used to execute command during the build process of the docker image. You can install additional packages needed for your Docker images.

# ADD
# The ADD instruction is used to copy files, directories, or remote files from URL to your Docker images, from the 'src' to the absolute path 'dest'. Also, you can set up the default ownership of your file.

# ENV
# The ENV instruction is used to define an environment variable that can be used during the build stage and can be replaced inline in many as well.

# CMD
# The CMD instruction is used to define the default command to execute when running the container. And the Dockerfile must only contain one CMD instruction, and if there is multiple CMD, the last CMD instruction will be run.

# EXPOSE
# This instruction is used to expose the container port on the specific network ports at runtime. The default protocol exposed is TCP, but you can specify whether the TCP or UDP.

# ARG
# The ARG instruction is used to define a variable that the user can pass at the built-time. You can use this instruction in the docker 'build command' during the build time using the '--build-arg variable=value' option and can be pass through the Dockerfile. Also, you can use multiple ARG at the Dockerfile.

# ENTRYPOINT
# The ENTRYPOINT instruction is used to define the first and default command that will be executed when the container is running. Define the command to start your application with the ENTRYPOINT instruction.

# WORKDIR
# The WORKDIR instruction is used to define the default working directory of your Docker image. The RUN, CMD, ENTRYPOINT, and ADD instructions follow the WORKDIR instruction. You can add multiple WORKDIR instruction on your Dockerfile, and if there is doesn't exist, it will be created automatically.

# USER
# The USER instruction is used to define the default user or gid when running the image. The RUN, CMD, and ENTRYPOINT follow the USER instruction in the Dockerfile.

# VOLUME
# The VOLUME instruction ad used to enable access/linked directory between the container and the host machine. 

# Here is an example:

# Download base image ubuntu 20.04
FROM ubuntu:20.04

# LABEL about the custom image
LABEL maintainer="admin@sysadminjournal.com"
LABEL version="0.1"
LABEL description="This is custom Docker Image for \
the PHP-FPM and Nginx Services."

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# Update Ubuntu Software repository
RUN apt update

# Install nginx, php-fpm and supervisord from ubuntu repository
RUN apt install -y nginx php-fpm supervisor && \
    rm -rf /var/lib/apt/lists/* && \
    apt clean
    
# Define the ENV variable
ENV nginx_vhost /etc/nginx/sites-available/default
ENV php_conf /etc/php/7.4/fpm/php.ini
ENV nginx_conf /etc/nginx/nginx.conf
ENV supervisor_conf /etc/supervisor/supervisord.conf

# Enable PHP-fpm on nginx virtualhost configuration
COPY default ${nginx_vhost}
RUN sed -i -e 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' ${php_conf} && \
    echo "\ndaemon off;" >> ${nginx_conf}
    
# Copy supervisor configuration
COPY supervisord.conf ${supervisor_conf}

RUN mkdir -p /run/php && \
    chown -R www-data:www-data /var/www/html && \
    chown -R www-data:www-data /run/php
    
# Volume configuration
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx", "/var/www/html"]

# Copy start.sh script and define default command for the container
COPY start.sh /start.sh
CMD ["./start.sh"]

# Expose Port for the Application 
EXPOSE 80 443
