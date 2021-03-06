# Skeleton of a CLI

import click

import testpy


@click.command('testpy')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(testpy.has_legs)
