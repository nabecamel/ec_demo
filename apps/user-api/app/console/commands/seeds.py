import typer

from app.helpers import env_helpers
from common.database import seeders

app = typer.Typer()


@app.command()
def seeds():
    if not env_helpers.is_local():
        typer.echo("ローカル環境以外では実行できません。")
        return

    seeders.UserSeeder().handle()
    seeders.ProductSeeder().handle()
    typer.echo("シードデータの作成が完了しました。")


if __name__ == "__main__":
    app()
