# cli.py
import click
import own_parser as op

"""
First decorator creates a command
Second decorator creates the flag options

create addition arguments with the argument decorator
"""
@click.command()
@click.option('--plot3d', default='', help='plots a 3d figure')
def cli(plot3d):
    click.echo("Hello World")
    click.echo('This is your formula {0}'.format(plot3d))
    op.main('{0}'.format(plot3d))

    #take the string for the cli and send it into the parser to create the file


if __name__ == "__main__":
    cli()