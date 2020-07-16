# pull official base image
FROM node:12.12-stretch

# Setup a Development User
RUN useradd -ms /bin/bash appuser

# Make the workdir with the right permissions
RUN mkdir /opt/app
RUN chown appuser /opt/app

# set working directory
WORKDIR /opt/app

# Swap to appuser user
USER appuser

# add `/opt/app/node_modules/.bin` to $PATH
ENV PATH /opt/app/node_modules/.bin:$PATH

# install app dependencies
RUN yarn install --silent
COPY --chown=appuser yarn.lock ./

# add app
COPY --chown=appuser . ./
EXPOSE 3000

# start app
CMD ["yarn", "start"]
