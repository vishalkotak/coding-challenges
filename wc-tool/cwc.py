import typer

app = typer.Typer()

def count_lines(file_path: str) -> int:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return len(lines)

def count_words(file_path: str) -> int:
    with open(file_path, 'r') as file:
        words = file.read().split()
    return len(words)

def count_characters(file_path: str) -> int:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    character_count = 0
    for line in lines:
        character_count += len(line) + 1
    return character_count

@app.command("l")
def get_line_count(file_path: str):
    try:
        print(count_lines(file_path))
    except FileNotFoundError:
        typer.echo(f"Error: File '{file_path}' not found.", err=True)
        raise typer.Exit(code=1)

@app.command("w")
def get_word_count(file_path: str):
    try:
        print(count_words(file_path))
    except FileNotFoundError:
        typer.echo(f"Error: File '{file_path}' not found.", err=True)
        raise typer.Exit(code=1)

@app.command("c")
def get_character_count(file_path: str):
    try:
        print(count_characters(file_path))
    except FileNotFoundError:
        typer.echo(f"Error: File '{file_path}' not found.", err=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()