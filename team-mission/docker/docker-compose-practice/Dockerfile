FROM node:14-alpine

WORKDIR /usr/src/app

# package.json과 package-lock.json이 있다면 함께 복사
COPY ./backend/package*.json ./

RUN npm install

COPY ./backend/* .

EXPOSE 3000

CMD ["node", "index.js"]