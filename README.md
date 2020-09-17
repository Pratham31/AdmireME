<h1 align="center">Admire Me - Action which will encourage you to do more open source contribution.</h1>

[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/Pratham31/AdmireME/blob/master/LICENSE)

# Motivation -
``` >> Do something today that your future self will thank you for.```
``` >> Little things make big days.```

# Reason for developing this GitHub Action -

You know when you admire someone, something gets happened and the human being feels so motivated and gets Positive vibes for self and starts the day with POSITIVE ENERGY. I just want each and every one student must contribute to open source and must be satisfied. My Action helps to get a smile 😊 on each and every Open Source Contributors and also encourages for contributing.

# What it does?🤔

It will send Email with **Processed Congratulating Image of user's avatar and congratulating Note GIF**  .

# Aim and Impact💥

This action will **ENCOURAGE** all future **open source contributors** to do more and more open source contributions and build positive vibes inside contributors


# How to test?🤔

## Note:
You have to make your Email ID **PUBLIC** so that action can easily send mail to User.

1. Just open a new issue on this [AdmireME](https://github.com/Pratham31/AdmireME) Repo.
2. You'll receive a personalized email (email account linked to your **Github**)

![](./.github/YouRockDemo.gif)

# Wanna use it in your repo?

1. Clone the repository.
2. Copy the all repository contents to your repository where you want to add the **Admire ME**.

## Lets see how I made this Action

## 1. First of all Setup an Email Sending Account

1. Create a new gmail account for sending the emails to the Contributors.
2. Authorize Gmail to send automated emails via this tool https://myaccount.google.com/lesssecureapps

![](https://docs.bitnami.com/images/img/apps/common/google-security.png)

3. And in the end create a [Github Secret](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets) Called `GKEY` and add your gmail password to it.

## 2. Setting up the action

1. Make sure that your repository contains all the necessary files which are present in this repository.
2. Click on Actions and `create an action`.
   ![](https://docs.github.com/assets/images/help/repository/actions-tab.png)

3. Add code in `Admire.yml` to your workflow `yml` file.

## 3. Customize your email contents

 - Just Replace the `senders_email` in `AdmireME.py` file with your newly created `email address`
 - And replace the `msg['From']` value with your email name.


## How to change the contribution triggers?

- Trigger Conditions which are used by me in this action are:

```
on:
  issues:
    types: opened
  pull_request_target:
    types: opened
    branches:
      - master
```

- The default triggering conditions are -

1.  Issues - Opened
2.  Pull Request - Opened

You can change the job triggers according to your need.

[Refer the official document from GitHub on Workflow Syntax.](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)

# How it looks like?

<img src="https://github.com/Pratham31/AdmireME/blob/master/Output.gif" height="500" width="900" align="left"></img>

