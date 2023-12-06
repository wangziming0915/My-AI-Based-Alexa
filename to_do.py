import click

# Create a list to store tasks
tasks = []

@click.group()
def cli():
    """Simple To-Do List CLI"""
    pass

@cli.command()
@click.argument('task')
def add(task):
    """Add a task to the to-do list"""
    tasks.append(task)
    click.echo(f'Task "{task}" added to the to-do list.')

@cli.command()
def list():
    """List all tasks in the to-do list"""
    if tasks:
        click.echo("To-Do List:")
        for i, task in enumerate(tasks, 1):
            click.echo(f"{i}. {task}")
    else:
        click.echo("Your to-do list is empty.")

@cli.command()
@click.argument('task_number', type=int)
def remove(task_number):
    """Remove a task from the to-do list by task number"""
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        click.echo(f'Task "{removed_task}" removed from the to-do list.')
    else:
        click.echo("Invalid task number. Use 'list' to see task numbers.")

if __name__ == '__main__':
    cli()