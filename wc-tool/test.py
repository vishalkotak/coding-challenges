import typer

app = typer.Typer()


@app.command()
def create(file_path: str):
    print(f"Creating user: {file_path}")


@app.command()
def delete(file_path: str):
    print(f"Deleting user: {file_path}")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context, file_path: str):
    """
    Manage users in the awesome CLI app.
    """
    if ctx.invoked_subcommand is None:
        print(f"Initializing database {file_path}")


if __name__ == "__main__":
    app()