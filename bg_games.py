import typer
import random
from pathlib import Path

app = typer.Typer()

with open('minions.txt', 'r') as f:
    minions = f.readlines()

@app.command()
def minion_roulette():
    ChosenMinion_text = Path('ChosenMinion.txt')

    # Delete ChosenMinion.txt
    if ChosenMinion_text.exists():
        ChosenMinion_text.unlink()


    chosen_one = random.choice(minions)
    ChosenMinion_text.write_text(f'Target Minion: {chosen_one}')
    typer.echo(chosen_one)


@app.command()
def minion_bingo():
    ChosenMinions_text = Path('BingoMinions.txt')

    # Delete ChosenMinion.txt
    if ChosenMinions_text.exists():
        ChosenMinions_text.unlink()


    minion_options = random.choices(minions, k=7)

    warband = ['Minion Bingo (!bingo):\n']

    for minion in minion_options:
        gold_option = random.choice(['Golden', ''])
        warband.append(f'{gold_option} {minion}')

    with open(ChosenMinions_text, 'w') as f:
        f.writelines(warband)

        for minion in warband:
            typer.echo(minion)


if __name__ == '__main__':
    app()
