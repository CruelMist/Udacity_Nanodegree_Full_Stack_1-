import media
import fresh_tomatoes

summary_game = "A group of friends who meet regularly for game nights find themselves entangled in a real-life mystery."  # noqa
image_url_game = "https://m.media-amazon.com/images/M/MV5BMjQxMDE5NDg0NV5BMl5BanBnXkFtZTgwNTA5MDE2NDM@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg"  # noqa
trailer_url_game = "https://youtu.be/qmxMAdV6s4U"
game_night = media.Movie("Game Night", summary_game, image_url_game,
                         trailer_url_game)

summary_ready = "When the creator of a virtual reality world called the OASIS dies, he releases a video in which he challenges all OASIS users to find his Easter Egg, which will give the finder his fortune."  # noqa
image_url_ready = "https://m.media-amazon.com/images/M/MV5BY2JiYTNmZTctYTQ1OC00YjU4LWEwMjYtZjkwY2Y5MDI0OTU3XkEyXkFqcGdeQXVyNTI4MzE4MDU@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg"  # noqa
trailer_url_ready = "https://youtu.be/cSp1dM2Vj48"
ready_player_one = media.Movie("Ready Player One", summary_ready,
                               image_url_ready, trailer_url_ready)

summary_deadpool2 = "Foul-mouthed mutant mercenary Wade Wilson (AKA. Deadpool), brings together a team of fellow mutant rogues to protect a young boy with supernatural abilities from the brutal, time-traveling cyborg, Cable."  # noqa
image_url_deadpool2 = "https://m.media-amazon.com/images/M/MV5BMjI3Njg3MzAxNF5BMl5BanBnXkFtZTgwNjI2OTY0NTM@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg"  # noqa
trailer_url_deadpool2 = "https://youtu.be/D86RtevtfrA"
deadpool2 = media.Movie("Deadpool 2", summary_deadpool2, image_url_deadpool2,
                        trailer_url_deadpool2)

summary_infinity = "The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe."  # noqa
image_url_infinity = "https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg"  # noqa
trailer_url_infinity = "https://youtu.be/6ZfuNTqbHE8"
avengers_infinity_war = media.Movie("Avengers: Infinity War", summary_infinity,
                                    image_url_infinity, trailer_url_infinity)

summary_ant2 = "As Scott Lang balances being both a Super Hero and a father, Hope van Dyne and Dr. Hank Pym present an urgent new mission that finds the Ant-Man fighting alongside The Wasp to uncover secrets from their past."  # noqa
image_url_ant2 = "https://m.media-amazon.com/images/M/MV5BYjcyYTk0N2YtMzc4ZC00Y2E0LWFkNDgtNjE1MzZmMGE1YjY1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg"  # noqa
trailer_url_ant2 = "https://youtu.be/8_rTIAOohas"
ant_man2 = media.Movie("Ant-Man and the Wasp", summary_ant2, image_url_ant2,
                       trailer_url_ant2)

summary_beasts2 = "The second installment of the Fantastic Beasts series set in J.K. Rowling's Wizarding World featuring the adventures of magizoologist Newt Scamander."  # noqa
image_url_beasts2 = 'https://m.media-amazon.com/images/M/MV5BNzQwNzI2NzU3Nl5BMl5BanBnXkFtZTgwNDU4NzIwNTM@._V1_QL50_.jpg'  # noqa
trailer_url_beasts2 = "https://youtu.be/5sEaYB4rLFQ"
fantastic_beasts2 = media.Movie("Fantastic Beasts: The Crimes of Grindelwald",
                                summary_beasts2, image_url_beasts2,
                                trailer_url_beasts2)


movies = [game_night, ready_player_one, deadpool2, avengers_infinity_war,
          ant_man2, fantastic_beasts2]
fresh_tomatoes.open_movies_page(movies)
