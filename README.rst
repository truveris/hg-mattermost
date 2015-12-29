hg-mattermost - Mercurial notifications in Mattermost
=====================================================

hg-mattermost is a mercurial hook publishing commits to Mattermost using
webhooks.

Configuration
-------------
To enable and configure hg-mattermost, you need to create an "Incoming
Webhook" in Mattermost (Account Settings, Integrations, Incoming Webhooks),
then you need to add the following to your repository's `hgrc` file::

    [hooks]
    incoming.mattermost = hg-mattermost

    [mattermost]
    hgweb_url = https://hg.example.com
    username = Mercurial
    webhook_url = https://mattermost.example.com/hooks/q9w8jq9wdw89sd7agf7sq7qweh
    icon_url = https://s3.amazonaws.com/truveris-mattermost-icons/mercurial.png
    skip_merges = true

Installation
------------
Install it just like any python project::

    pip install hg-mattermost
