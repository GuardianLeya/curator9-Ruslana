import telebot

bot = telebot.TeleBot("6931948410:AAE94yCjXdkb8CWArB-bxju5j4569ZxqreA")


@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, "Хай! Здесь ты сможешь узнать много нового про Вселенную Черепашек-Ниндзя")


@bot.message_handler(commands=["characters"])
def main(message):
    bot.send_message(message.chat.id,
                     "*Главные герои:*\n Леонардо, Рафаэль, Донателло, Микеланджело, Сплинтер, Эйприл, Кейси, Карай, Шреддер, Крэнги \n *Второстепенные герои:*\n Крис Брэдфорд, Ксевер Монтес,Бакстер Стокман,Такеши, Крэнг Прайм, Кирби О'Нил,  Шинигами, Спайк (Слэш),Кожеголовый и др.",
                     parse_mode=" Markdown")


@bot.message_handler(commands=["Versions"])
def main(message):
    bot.send_message(message.chat.id, "Здесь собраны все телевизионные версии Черепашек-Ниндзя (без фильмов): \n "
                                      "Черепашки-ниндзя сериал (1987) \n Аниме Черепашки-Ниндзя (1996) \n  Живой сериал того же названия (1997) \n Черепашки-Ниндзя.Новые приключения!(2003) \n Черепашки-Ниндзя мультсериал (2012) \n Черепашки-ниндзя: Восстание (2018)")


@bot.message_handler(commands=["history"])
def main(message):
    bot.send_message(message.chat.id,
                     "*В первые черепашек ниндзя увидел свет (5 мая 1984 году )* \n Идея о черепашках мутантов появилась у двух друзей , Кевина Истмена и Питера лэрда . одним вечером, когда они вместе рисовали комические рисунки. Взяв денег взаймы у дяди Истмэна, молодые художники сами издали первый выпуск комикса, который по начальной задумке должен был быть пародией на четыре популярных комикса 80-х: Сорвиголова, New Mutants,Cerebus и Ronin. Первоначально все черепашки-ниндзя были чёрно-белыми, но Истмен предлагал рисовать на обложке только красные повязки. Однако, когда черепашки стали популярны в 80-х, Лэрд и Истмэн позволили каждой черепашке иметь свой собственный цвет банданы: красная бандана была лишь у Рафаэля, синяя досталась Леонардо, фиолетовая у Донателло и оранжевая у Микеланджело. \n По мотивам комиксов создали: \n 1 сериал (1997) \n 4 мультсериала (1987, 2003, 2012,2016;2018) \n 6 разных серий комиксов \n 8 фильмов: 5 из них — художественные (1990, 1991, 1993, 2014, 2016), 3 — анимационные (2007, 2009, 2019).",
                     parse_mode="Markdown")


@bot.message_handler(commands=["film"])
def main(message):
    bot.send_message(message.chat.id, " [Это фильм 2014 года Черепашки-Ниндзя]("
                                      "https://281123.lordfilm3.black/14382-film-cherepashki-nindzja-2014.html",
                     parse_mode="Markdown")


bot.infinity_polling()