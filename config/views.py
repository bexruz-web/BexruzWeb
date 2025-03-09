from django.shortcuts import render, redirect
from django.contrib import messages

from settings_app.models import TelegramBotSettings

from about_me.models import About

from portfolio_app.models import Category, Portfolio

from about_me.forms import ContactMessagesForm

import requests


def Home_page(request):
    about = About.objects.last()

    portfolio_category = Category.objects.all()
    portfolios = Portfolio.objects.all()

    ctx = {
        'about': about,
        'portfolio_category': portfolio_category,
        'portfolios': portfolios
    }

    # Telegram Bot Send
    if request.method == "POST":
        form = ContactMessagesForm(request.POST)
        bot = TelegramBotSettings.objects.last()

        if form.is_valid():
            if bot is not None:
                bot_token = bot.token
                user_id_list = str(bot.userid_list).split(", ")
                url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

                try:
                    for user_id in user_id_list:
                        print(user_id)
                        response = requests.post(
                            url=url,
                            json={
                                'chat_id': user_id,
                                'text': f"<b>🔔 Yangi xabar:</b>\n\n"
                                        f"<b>👤 Ismi:</b> {request.POST['name']}\n"
                                        f"<b>📞 Telefon raqami:</b> {request.POST['phone_number']}\n"
                                        f"<b>📑 Xabari:</b> {request.POST['text']}",
                                'parse_mode': 'HTML'
                            }
                        )
                except:
                    print("Error")

            form.save()

            messages.success(request, "Xabaringiz yuborildi. Tez orada siz bilan bog'lanamiz!")
            return redirect("Home_page")
        else:
            messages.error(request, "Xatolik! Qaytadan urinib ko'ring")
            return redirect('Home_page')
    else:
        form = ContactMessagesForm()

    ctx['form'] = form

    return render(request, 'index.html', ctx)