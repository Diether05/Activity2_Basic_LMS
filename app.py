import database
import menu
import prompt
import looping

print(menu.welcome)
database.create_tables()

looping.loop()