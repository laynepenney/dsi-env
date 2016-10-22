import click
import os


@click.group(name='dsci')
@click.option('--home', default=None)
@click.pass_context
def main(ctx, home):
    """dsci env tool"""
    home = os.path.abspath(home or '.')
    ctx.obj = home
    # click.echo('home={0}'.format(home))


@main.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='world', required=False)
def hello(name, as_cowboy):
    """say hello"""
    greet = 'Howdy' if as_cowboy else 'Hello'
    click.echo('{0}, {1}.'.format(greet, name))


@main.command()
@click.option('--env', '-e', default='dsienv')
@click.pass_obj
def activate(home, env):
    """activate dsci env"""
    click.echo("home={0}, activate env={1}".format(home, env))


@main.command()
@click.option('--env', '-e', default='dsienv', required=False)
@click.pass_obj
def deactivate(home, env):
    """deactivate dsci env"""
    click.echo("home={0}, deactivate env={1}".format(home, env))
