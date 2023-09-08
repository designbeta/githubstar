# githubstar

Export Github starred repos list to html, bookmark, json or markdown format, grouped by language or topics, order by time, stargazers count etc..

## Installation

- Using [pip](https://pypi.org/project/githubstar/)
```
$ pip install githubstar
```

- Using Binaries (x64 architecture only) from [Release page](https://github.com/designbeta/githubstar/releases)

- You can also clone the repo and build from source


## Quick Start

Run with username
```
$ githubstar --username <username>
```
Run with username, Github access token and default options
```
$ export GITHUB_TOKEN=<Access-Token>
$ githubstar --username <username>
```
or
```
$ githubstar --username <username> --token <Access-Token>
```
Run with language grouped and bookmark format 
```
$ githubstar --username <username> --token <Access-Token> --format bookmark --groupby language
```

## Usage

```
$ githubstar -h

usage: githubstar [-h] [--version] --username USERNAME [--token TOKEN] [--format {html,bookmark,md,json}]
                [--groupby {none,language,topic}]
                [--orderby {timestarred,timeupdated,alphabet,starscount,forkscount,language}]
                [--orderdirection {desc,asc}] [--ordernum {true,false}] [--excludeprivate {true,false}]
                [--destpath DESTPATH] [--destname DESTNAME]

Export a GitHub user's starred list to local file.

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --username USERNAME   [required]username to export from
  --token TOKEN         token from https://github.com/settings/tokens, to avoid rate-limiting, can also store in
                        environment as 'GITHUB_TOKEN'.
  --format {html,bookmark,md,json}
                        output format, default: html
  --groupby {none,language,topic}
                        default: none
  --orderby {timestarred,timeupdated,alphabet,starscount,forkscount,language}
                        default: timestarred
  --orderdirection {desc,asc}
                        default: desc
  --ordernum {true,false}
                        show order number before repository name or not, default: true
  --excludeprivate {true,false}
                        exclude private repositories, default: false
  --destpath DESTPATH   path to store the exported file
  --destname DESTNAME   filename of the exported file
```

## FAQ

 - A 'RateLimitExceededException' error is met?
 
   The Github API rate limiting is reached. An access token is needed in this case. Check out this [https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting](https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting) for more details.
    

 - Where to get the access token? 

   Login with your Github account and go to this page: [https://github.com/settings/tokens](https://github.com/settings/tokens)