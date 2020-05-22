FROM mhart/alpine-node:12
RUN mkdir /src
WORKDIR /src
COPY package.json /src/
RUN npm i react-scripts --global
RUN npm i yarn --global
RUN npm i serve --global
COPY yarn.lock /src/
RUN yarn
COPY . /src/
RUN npm run build
CMD serve -s build -p $PORT
