#!/bin/bash

# if backup os is not complete or not exist, then will be reboot.

case $1 in
    "recently")
        test -d /home/partimag/$2 && exit || echo -e "\033[31mThe backup os image ${2} is NOT complete!\033[0m\n\033[33mrebooting now...\033[0m"; sleep 5; reboot
        ;;
    "factory")
        test -d /home/partimag/init-image && exit || echo -e "\033[31mThe backup os image is NOT complete!\033[0m\n\033[33mrebooting now...\033[0m"; sleep 5; reboot
        ;;
    *)
        ;;
esac
