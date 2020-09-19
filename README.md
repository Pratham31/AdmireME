<div align="center">
<img src="https://github.com/Pratham31/AdmireME/blob/master/AdmireMELogo.png" width ="500" height="350">
</div>

<h1 align="center">Admire Me - Action which will encourage you to do more open source contribution.</h1>
<br>
<br>

# Motivation -
``` >> Do something today that your future self will thank you for.```
<br>
``` >> Little things make big days.```
<br>

# Reason for developing this GitHub Action -

You know when you admire someone, something gets happened and the human being feels so motivated and gets Positive vibes for self and starts the day with POSITIVE ENERGY. I just want each and every one student must contribute to open source and must be satisfied. My Action helps to get a smile 😊 on each and every Open Source Contributors and also encourages for contributing.
<br>

# What does it do?🤔

It will send an Email with **Processed Congratulating Image of user's avatar and congratulating Note GIF**  .
Check out official Document of [GitHub Action](https://docs.github.com/en/actions) from GitHub.
<br>

# Aim and Impact💥

This action will **ENCOURAGE** all future **open source contributors** to do more and more open source contributions and build positive vibes inside contributors
<br>

# How to test it?🤔

## Note:
You have to make your Email ID **PUBLIC** so that action can easily send mail to User.
You can make your Email ID public just by going into ```settings->Emails->Keep my email addresses private``` and Uncheck the Keep my email addresses private option.

1. You just have to open a new issue on this [AdmireME](https://github.com/Pratham31/AdmireME) Repo.
2. then You'll receive a email with processed your GitHub Avatar attachment.

![](./.github/YouRockDemo.gif)

# Wanna use it in your repo?

1. Clone the repository.
2. Copy the all repository contents to your repository where you want to add the **Admire ME**.
<br>
<br>

## Lets see how I made this Action
<br>

## 1. First of all Setup an Email Sending Account

1. I Created a new gmail account for sending the emails to the Contributors.
2. Then you have to authorize Gmail to send the automated emails via this https://myaccount.google.com/lesssecureapps

![](https://docs.bitnami.com/images/img/apps/common/google-security.png)

3. And in the end create a [Github Secret](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets) Called `GKEY` and add your gmail password to it.
<br>

## 2. Setting up the action in your Repository

1. Make sure that your repository contains all the necessary files which are present in this repository.
2. Click on the Actions tab and then `create an action`.
   ![](https://docs.github.com/assets/images/help/repository/actions-tab.png)
3. Add code in `Admire.yml` to your workflow `yml` file.
<br>

## 3. Modify Email Contents 

 - You just have to Replace the `sender_mailID` in `AdmireME.py` file with your newly created `email address`
 - And then replace the `msg['From']` with your email name.
 - that's it!!!!
<br>

## Trigger Conditions?

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


[Refer the official document from GitHub on Workflow Syntax.](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
<br>

# How it looks like?

<img src="https://github.com/Pratham31/AdmireME/blob/master/Output.gif" height="500" width="900" align="left"></img>

