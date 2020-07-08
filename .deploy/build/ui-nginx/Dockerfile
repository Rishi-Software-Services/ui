FROM bitnami/node:12-prod

COPY .deploy/build/ui-nginx/install_app.sh /install_app.sh

RUN /install_app.sh ui https://github.com/Rishi-Software-Services/ui

FROM frappe/erpnext-nginx:version-13-beta

COPY --from=0 /home/frappe/frappe-bench/sites/ /var/www/html/
COPY --from=0 /rsync /rsync
RUN echo -n "\nui" >> /var/www/html/apps.txt

VOLUME [ "/assets" ]

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]