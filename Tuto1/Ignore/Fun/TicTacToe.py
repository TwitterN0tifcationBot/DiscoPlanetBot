import discord
from discord.ext import commands

class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.game_active = False
        self.board = [' ' for _ in range(9)]
        self.current_player = None

    @commands.command(name='tictactoe', description='Start a game of TicTacToe', usage='tictactoe @opponent')
    async def tictactoe(self, ctx, opponent: discord.Member):
        if self.game_active:
            await ctx.send("A game is already in progress!")
            return

        self.game_active = True
        self.current_player = ctx.author
        self.opponent = opponent
        self.board = [' ' for _ in range(9)]
        await ctx.send(f"TicTacToe game started between {ctx.author.mention} and {opponent.mention}!")
        await self.display_board(ctx)

    @commands.command(name='place', description='Place your mark on the board', usage='place <position>')
    async def place(self, ctx, position: int):
        if not self.game_active:
            await ctx.send("No game is currently active. Start a new game with `!tictactoe @opponent`.")
            return

        if ctx.author != self.current_player:
            await ctx.send("It's not your turn!")
            return

        if position < 1 or position > 9 or self.board[position - 1] != ' ':
            await ctx.send("Invalid position! Choose a number between 1 and 9 that hasn't been taken.")
            return

        self.board[position - 1] = 'X' if self.current_player == ctx.author else 'O'
        if self.check_winner():
            await self.display_board(ctx)
            await ctx.send(f"{self.current_player.mention} wins!")
            self.game_active = False
            return

        if ' ' not in self.board:
            await self.display_board(ctx)
            await ctx.send("It's a tie!")
            self.game_active = False
            return

        self.current_player = self.opponent if self.current_player == ctx.author else ctx.author
        await self.display_board(ctx)

    async def display_board(self, ctx):
        board_str = ''
        for i in range(9):
            if i % 3 == 0:
                board_str += '\n'
            board_str += f' {self.board[i]} '
        await ctx.send(f"```{board_str}```")

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

def setup(bot):
    bot.add_cog(TicTacToe(bot))