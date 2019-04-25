# snapshotalyzer-3000

Demo project to manage AWS EC2 instance snapshots

## About

This project uses boto3 to manage AWS EC@ instance snapshoots.

## Configuring

shotty uses the configuration file created by the AWS CLI. e.g.

'aws configure --profile shotty'

## Running

'pipenv run python shotty/shotty.py <command> <subcommand> <--project=PROJECT>'

*command* is instances, volumes, or snapshots
*subcommand* list, start, or stop for instances,
             list for volumes,
             list for snapshots
*project* is optional
