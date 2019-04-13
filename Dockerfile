FROM node:10 as react-build

WORKDIR /app

COPY ./package.json ./package.json
RUN yarn install

COPY . .
RUN yarn run build

FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=react-build /app/build /usr/share/nginx/html
EXPOSE 80
CMD [“nginx”, “-g”, “daemon off;”]