# Dev Metrics in Readme

![Project Preview](https://user-images.githubusercontent.com/8397274/87243943-e6b45c00-c457-11ea-94c9-2aa0bf241be8.png)

----

[WakaTime](https://wakatime.com) Weekly Metrics on your Profile Readme:

## Prep Work

1. You need to update the markdown file(.md) with 2 comments. You can refer [here](#update-your-readme) for updating it.
2. You'll need a WakaTime API Key. You can get that from your WakaTime Account Settings
    - You can refer [here](#new-to-wakatime), if you're new to WakaTime
3. **Optional** You'll need a GitHub API Token with `repo` scope from [here](https://github.com/settings/tokens) if you're running the action not in your Profile Repository
    - You can use [this](#other-repository-not-profile) example to work it out
4. You need to save the WakaTime API Key (and the GitHub API Token, if you need it) in the repository secrets. You can find that in the Settings of your Repository.Be sure to save those as the following.
    - WakaTime-api-key as `WAKATIME_API_KEY = <your wakatime API Key>`and
    - The GitHub Access Token as `GH_TOKEN=<your github access token>`
5. You can follow either of the Two Examples according to your needs to get started with.

> I strongly suggest you to run the Action in your Profile Repo since you won't be needing a GitHub Access Token

This Action will run everyday at 00.00 UTC

## Update your Readme

Add a comment to your `README.md` like this:

```md
<!--START_SECTION:waka-->
<!--END_SECTION:waka-->
```

These lines will be our entry-points for the dev metrics.

## New to WakaTime

WakaTime gives you an idea of the time you really spent on coding. This helps you boost your productivity and competitive edge.

- Head over to <https://wakatime.com> and create an account.
- Get your WakaTime API Key from your [Account Settings in WakaTime](https://wakatime.com/settings/account).
- Install the [WakaTime plugin](https://wakatime.com/plugins) in your favourite editor / IDE.
- Paste in your API key to start the analysis.

### Profile Repository

*If you're executing the workflow on your Profile Repository (`<username>/<username>`)*

> You wouldn't need an GitHub Access Token since GitHub Actions already makes one for you.

Please follow the steps below:

1. Go to your `<username>/<username>/actions`, hit `New workflow`, `set up a workflow yourself`, delete all the default content github made for you.
2. Copy the following code and paste it to your new workflow you created at step 1:
  ```yml
  name: Waka Readme

  on:
    workflow_dispatch:
    schedule:
      # Runs at 12am UTC
      - cron: '0 0 * * *'

  jobs:
    update-readme:
      name: Update this repo's README
      runs-on: ubuntu-latest
      steps:
        - uses: athul/waka-readme@master
          with:
            WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
  ```
3. Go to your repo secrets by hitting `Settings => Secrets` tab in your profile repo. You can also enter the url  https://github.com/USERNAME/USERNAME/settings/secrets . Please replace the `USERNAME` with your own username.
4. Create a new `Secret`. `Name`: `WAKATIME_API_KEY`, `Value`: Paste the Wakatime API key here. If you don't know what is the key, please go to  [Account Settings in WakaTime](https://wakatime.com/settings/account) to find your API Key there.
5. Add a comment to your `README.md` like this:

  ```md
  <!--START_SECTION:waka-->
  <!--END_SECTION:waka-->
  ```
6. Go to Workflows menu (mentioned in step 1), click `Waka Readme`, click `Run workflow`.
7. Go to your profile page. you will be able to see it. 

### Other Repository (not Profile)



*If you're executing the workflow on another repo other than `<username>/<username>`*

You'll need to get a [GitHub Access Token](https://docs.github.com/en/actions/configuring-and-managing-workflows/authenticating-with-the-github_token) with a `repo` scope and save it in the Repo Secrets `GH_TOKEN = <Your GitHub Access Token>`

Here is Sample Workflow File for running it:

```yml
name: Waka Readme

on:
  schedule:
    # Runs at 12am UTC
    - cron: '0 0 * * *'

jobs:
  update-readme:
    name: Update Readme with Metrics
    runs-on: ubuntu-latest
    steps:
      - uses: athul/waka-readme@master
        with:
          WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
          GH_TOKEN: ${{ secrets.GH_TOKEN }}
          USERNAME: <username> # optional, it will automatically use the username of the owner of the repository who's executing the workflow.
```

## Extras

1. If you want to add the week in the Header of your stats, you can add `HEAD_FLAG: true` in your workflow file like this

```yml
- uses: athul/waka-readme@master
        with:
          WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
          GH_TOKEN: ${{ secrets.GH_TOKEN }}
          USERNAME: <username>
          SHOW_TITLE: true
```

`SHOW_TITLE` flag can be set to true if you want to display the week number and days in the readme, by default it will be false. Here is an example output with `SHOW_TITLE` set to true.

```text
Week: 10 July, 2020 - 17 July, 2020
Python      8 hrs 52 mins       ███████████████████░░░░░░   75.87 % 
Go          1 hr 15 mins        ██░░░░░░░░░░░░░░░░░░░░░░░   10.79 % 
Markdown    52 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   07.43 % 
Docker      16 mins             ░░░░░░░░░░░░░░░░░░░░░░░░░   02.32 % 
YAML        7 mins              ░░░░░░░░░░░░░░░░░░░░░░░░░   01.07 %
```
