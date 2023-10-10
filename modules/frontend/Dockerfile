FROM node:14.8.0-alpine3.12

WORKDIR .

COPY ./modules/frontend/package.json ./
COPY ./modules/frontend/package-lock.json ./

RUN npm install --unsafe-perm
RUN npm install react-scripts@3.4.3 -g 

COPY ./modules/frontend/ ./

EXPOSE 3000

CMD ["npm", "start"]

