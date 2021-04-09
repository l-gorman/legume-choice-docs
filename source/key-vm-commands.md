# Key Commands for Virtual Machine

This document contains key information to get started working with the legumeCHOICE VM. It includes some information about where important files are stored as well as a cheatsheet for running, stopping, and restarting processes.

A repository has been created for two of the main server files, this can be found {{ '[here]({}{})'.format(githubBase,serverConfRepo) }}.

To restart the NGINX server enter the command `systemctl restart nginx`

To restart the python daemon enter the command `systemctl restart legume_choice_data_process.service`, followed by the command `systemctl daemon-reload`.

To restart the API, enter the command `pm2 restart ~USERNAME/legumeCHOICE/api/server.js`.
