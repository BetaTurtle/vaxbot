import json
import logging
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

eligiblelist = [
    [
        "I was previously infected with covid 19. When am I eligible to take the vaccine?"
    ],
    ["I have diabetes, blood pressure or asthma. Can I take the vaccine?"],
    ["I have HIV/hepatitis B/C infection. Can I take the vaccine?"],
    ["I am on dialysis or have received an organ transplant. Can I take the vaccine?"],
    [
        "I have dust/pollen allergies, asthma, allergic rhinitis etc. Should I get vaccinated?"
    ],
    ["◀️ Back"],
    ["🏁 End session"],
]
genquerylist = [
    ["Should I get any blood tests before or after getting vaccinated?"],
    ["Will I test positive for covid after vaccination?"],
    [
        "There is news of vaccination scams. How can I ensure that I have received a genuine vaccine?"
    ],
    ["How long will vaccines protect me from covid infection?"],
    ["Can I eat non veg food after vaccination? Are there any food restrictions?"],
    ["Are there any restrictions on alcohol intake before or after vaccination?"],
    ["I am planning on traveling to a foreign country. What vaccine should I get?"],
    ["Is one vaccine better than others? Do vaccines protect against Delta variant?"],
    ["Can I take doses of two different vaccines? Is vaccine mixing safe?"],
    ["Can I get revaccinated with a completely different vaccine?"],
    ["◀️ Back"],
    ["🏁 End session"],
]
postvacquery = [
    ["Are there any general precautions I should take after getting vaccinated?"],
    [
        "I'm getting fever, bodyache, headache or weakness after vaccination. What to do?"
    ],
    [
        "I have been vaccinated. How can I ensure it worked? When can I get an antibody test?"
    ],
    ["I am fully vaccinated. Does this mean that I cannot get covid anymore?"],
    ["◀️ Back"],
    ["🏁 End session"],
]
femalequery = [
    ["🩸 Can I get vaccinated while having periods?"],
    ["🤰🏻 I am pregnant. Can I get vaccinated?"],
    ["🤱🏻 I am breastfeeding. Can I get vaccinated?"],
    ["👩🏻‍⚕️ General vaccination related queries."],
]
mainmenuquery = [
    ["Queries regarding vaccine eligibility"],
    ["Post vaccination queries"],
    ["General queries about vaccines"],
    ["💉 Start over"],
    ["🏁 End session"],
]
flow = {
    "/start": ["Please choose your age group", [["Under 18", "Above 18"]]],
    "💉 Start over": ["Please choose your age group", [["Under 18", "Above 18"]]],
    "Under 18": [
        "Under 18 not eligible for vaccination. Would you like to start again?",
        [["💉 Start over"], ["🏁 End session"]],
    ],
    "Above 18": ["Select your gender", [["🙋🏻‍♂️ Male", "🙋🏻‍♀️ Female"]]],
    "🙋🏻‍♂️ Male": [
        "Kindly select the broad nature of your query",
        mainmenuquery,
    ],
    "◀️ Back": [
        "Kindly select the broad nature of your query",
        mainmenuquery,
    ],
    "🙋🏻‍♀️ Female": [
        "Please choose your question",
        femalequery,
    ],
    "👩🏻‍⚕️ General vaccination related queries.": [
        "Kindly select the broad nature of your query.",
        mainmenuquery,
    ],
    "🩸 Can I get vaccinated while having periods?": [
        "Yes. There is no contraindication to getting vaccinated during menstrual periods. However if you have a choice, it is better to get vaccinated about 5-7 days after periods as hormone levels will be stable at that point. ",
        femalequery,
    ],
    "🤰🏻 I am pregnant. Can I get vaccinated?": [
        "Please get vaccinated in consultation with your gynaecologist.",
        femalequery,
    ],
    "🤱🏻 I am breastfeeding. Can I get vaccinated?": [
        "Please get vaccinated. All approved vaccines are safe for  lactating mothers.",
        femalequery,
    ],
    "Queries regarding vaccine eligibility": [
        "Please choose your question",
        eligiblelist,
    ],
    "I have dust/pollen allergies, asthma, allergic rhinitis etc. Should I get vaccinated?": [
        "Yes definitely. Allergic reaction to pollen/dust/paint/etc will not cause allergic reaction to the vaccine. You can mention to the vaccination center staff about your history of allergies in case you have further doubts, but even people with allergies should get vaccinated. The vaccination center will monitor you for 15 minutes after vaccination and they should be equipped with all medications to handle any vaccine related allergic reaction .",
        eligiblelist,
    ],
    "I was previously infected with covid 19. When am I eligible to take the vaccine?": [
        "Get vaccinated 90 days after recovering from covid infection. Date of recovery is considered to be date of discharge for hospitalized patients. For patients who have been treated at home, consider 104 days from the date of diagnosis (as typical course of disease is 14 days).",
        eligiblelist,
    ],
    "I have diabetes, blood pressure or asthma. Can I take the vaccine?": [
        "Yes definitely. People with diabetes, high blood pressure, asthma, people with HIV/hepatitis B/C infection, organ transplant recipients and people on dialysis are all high priority and should get vaccinated at the earliest.",
        eligiblelist,
    ],
    "I have HIV/hepatitis B/C infection. Can I take the vaccine?": [
        "Yes definitely. People with diabetes, high blood pressure, asthma, people with HIV/hepatitis B/C infection, organ transplant recipients and people on dialysis are all high priority and should get vaccinated at the earliest.",
        eligiblelist,
    ],
    "I am on dialysis or have received an organ transplant. Can I take the vaccine?": [
        "Yes definitely. People with diabetes, high blood pressure, asthma, people with HIV/hepatitis B/C infection, organ transplant recipients and people on dialysis are all high priority and should get vaccinated at the earliest.",
        eligiblelist,
    ],  # End of eligibility
    "General queries about vaccines": [
        "Please choose your question",
        genquerylist,
    ],
    "Should I get any blood tests before or after getting vaccinated?": [
        "There is no requirement of getting any blood tests before or after vaccination.",
        genquerylist,
    ],
    "Will I test positive for covid after vaccination?": [
        "No. You should not test positive for covid after vaccination.",
        genquerylist,
    ],
    "There is news of vaccination scams. How can I ensure that I have received a genuine vaccine?": [
        """All vaccinations in India are facilitated by the COWIN platform. You should receive an SMS confirming your vaccination and you can also download a certificate from the CoWIN system.
CoWIN links the registered mobile number with upto 4 beneficiaries. Each registered dose is linked to a reference ID.
Each vaccine camp is supposed to provide printed certificate to all beneficiaries. The same can also be downloaded from cowin.gov.in using the same mobile number that was used at the time of vaccination.""",
        genquerylist,
    ],
    "How long will vaccines protect me from covid infection?": [
        """Covid-19 vaccines trigger your long term immunity and teach the body's long term immunity to fight the infection. The immune system should be able to retain this training for a few years.
However, covid is a rapidly evolving disease, and new variants are coming forward everyday. As of now, all of the vaccines certified for use in India provide a certain degree of protection against all variants.
It is possible that we might have to take updated booster shots in the future, but only time will tell.""",
        genquerylist,
    ],
    "Can I eat non veg food after vaccination? Are there any food restrictions?": [
        """There are absolutely no food related restrictions associated with vaccination. You can eat whatever food you want, including non veg food, before and after vaccination.
That being said, it is always advisable to eat simple, light and healthy food. :)""",
        genquerylist,
    ],
    "Are there any restrictions on alcohol intake before or after vaccination?": [
        """There is no formal advice from health agencies about restricting alcohol intake after vaccination.
However, alcohol can interfere with one's immune system, so as a matter of general advice, it is best to avoid drinking more than 30ml of alcohol a day for about 7-10 days after vaccination.""",
        genquerylist,
    ],
    "I am planning on traveling to a foreign country. What vaccine should I get?": [
        """In such cases your choice of vaccine would depend on the country you are travelling to. As of now, out of the vaccines approved for use in India, Covishield (Indian made Oxford Astra-Zeneca vaccine) and Moderna (mRNA vaccine distributed in India by Cipla) are the ones with the widest international approval as per WHO standards.
WHO is continuously reviewing and approving new vaccines, so you can get the most up-to-date information from their website by following the link below. 
https://tinyurl.com/5annk4ux""",
        genquerylist,
    ],
    "Is one vaccine better than others? Do vaccines protect against Delta variant?": [
        """All the vaccines approved for use in India are proven to be effective in preventing symptomatic infection and reducing chances of death due to covid infection. They have all been shown to be effective against the Delta variant as well.
One vaccine might be technically superior to another, but practically their purpose is the same. The best course of action is to get vaccinated as soon as one is eligible and vaccination slots are available.""",
        genquerylist,
    ],
    "Can I get revaccinated with a completely different vaccine?": [
        """There have been a few trials of mixing vaccines.
The studies have largely focused on taking a second dose of mRNA vaccine like Pfizer or Moderna after taking an initial dose of other vaccines, largely Oxford Astra-Zeneca. It is generally safe to take two doses of different vaccines, like for example first dose of Oxford Astra-Zeneca and second dose of Moderna. 
However, any such mixing of the vaccine should be done after taking the input of a medical professional.""",
        genquerylist,
    ],
    "Can I take doses of two different vaccines? Is vaccine mixing safe?": [
        """There have been a few trials of mixing vaccines.
The studies have largely focused on taking a second dose of mRNA vaccine like Pfizer or Moderna after taking an initial dose of other vaccines, largely Oxford Astra-Zeneca. It is generally safe to take two doses of different vaccines, like for example first dose of Oxford Astra-Zeneca and second dose of Moderna. 
However, any such mixing of the vaccine should be done after taking the input of a medical professional.""",
        genquerylist,
    ],  # End of gen query
    "Post vaccination queries": [
        "Please choose your question",
        postvacquery,
    ],
    "Are there any general precautions I should take after getting vaccinated?": [
        """It is advisable to take a day off work and rest on the day of vaccination and the day after getting vaccinated. Drink plenty of water and avoid strenuous activities including exercise and going to the gym. By avoiding exhaustive activities you are letting your body dedicate its resources to generating immunity.""",
        postvacquery,
    ],
    "I'm getting fever, bodyache, headache or weakness after vaccination. What to do?": [
        """Some mild symptoms such as fever up to 99.5F, headache, body ache, feeling weakness and fatigue, pain at the site of injection are common for 2-3 days after vaccination.
You can take tablet paracetamol 500/650mg (crocin/ dolo/ calpol/ pacimol) up to 3 times a day to relieve such symptoms. If they persist for more than 2-3 days, especially fever, and if the fever is high grade, ie 101F or higher, get checked by a doctor in person.""",
        postvacquery,
    ],
    "I have been vaccinated. How can I ensure it worked? When can I get an antibody test?": [
        """All the vaccines are carefully titrated to doses that will generate robust immune response.
If you want to personally check the response of your body, you can get an antibody test around 10-20 days after getting the second dose. These tests are available at leading pathology laboratories and should be interpreted under the supervision of a doctor.""",
        postvacquery,
    ],
    "I am fully vaccinated. Does this mean that I cannot get covid anymore?": [
        """No. Definitely not.
Vaccines are proven to reduce symptomatic infection and death, but this does not mean that you cannot get covid infection after getting vaccinated.
You have to continue wearing masks and following "covid-appropriate-behavioral practices" till the time that this pandemic is over.""",
        postvacquery,
    ],
    "🏁 End session": [
        """Thank you for using @cov_vax_bot, a covid19india.org initiative.
Send /start to start again.
To book a vaccination appointment, or to download your vaccination certificate, visit https://www.cowin.gov.in/
For more information on coronavirus vaccines and the global fight against covid, visit https://bit.ly/2UqgXtm
For up-to-date statistics on covid-19 in India, visit https://www.covid19india.org
Remember to stay safe, wear masks and most importantly,
get vaccinated!""",
        0,
    ],
}


def entry(bot, update):
    try:
        # res = bot.send_message(chat_id="-1001164870268", text=json.dumps(update.to_dict(), indent=2))
        # print(json.dumps(update.to_dict(), indent=2))
        logging.info(update)
        pass
    except Exception as e:
        logging.error(e)
        # bot.send_message(chat_id="-1001164870268", text=str(e))
    if update.message and update.message.text:
        chat_id = update.message.chat_id
        text = update.message.text
        if update.message.text == "/start":
            bot.sendMessage(
                chat_id=chat_id,
                text="Welcome. This bot will help in answering common queries about Covid-19 vaccination.",
            )

        if text in flow:
            if flow[text][1] == 0:
                reply_markup = ReplyKeyboardRemove()
            else:
                reply_markup = ReplyKeyboardMarkup(
                    keyboard=flow[text][1], one_time_keyboard=False
                )
            bot.sendMessage(
                chat_id=chat_id,
                text=flow[text][0],
                reply_markup=reply_markup,
            )
        else:
            logging.error("Unknown reply")

        # # bot.send_message(chat_id=chat_id, text="Hello")
        # ans_list = [
        #     ["Should I get any blood tests before or after getting vaccinated?"],
        #     ["Will I test positive for covid after vaccination?"],
        #     [
        #         "How can I be sure that the vaccine I have received is real and that I am not being given a fake vaccine?"
        #     ],
        #     ["How long will vaccines protect me from covid infection?"],
        #     [
        #         "Are there any restrictions on what food I can eat after getting vaccinated? Can I eat non veg food after vaccination?"
        #     ],
        #     [
        #         "Are there any restrictions on alcohol intake before or after vaccination?"
        #     ],
        #     [
        #         "I am planning on traveling to a foreign country. What vaccine should I get?"
        #     ],
        #     [
        #         "Is there some vaccine that does not work against the Delta variant? Is one vaccine better than the others?"
        #     ],
        #     [
        #         "Can I take doses of two different vaccines? Can I get revaccinated with a completely different vaccine?"
        #     ],
        # ]
        # bot.sendMessage(
        #     chat_id=chat_id,
        #     text="Pick from this",
        #     # reply_markup=ans_list,
        #     reply_markup=ReplyKeyboardMarkup(keyboard=ans_list, one_time_keyboard=True),
        # )

        # InlineKeyboardMarkup([
        #     [InlineKeyboardButton("Should I get any blood tests before\n or after getting vaccinated?", callback_data ="asdf")],
        #     [InlineKeyboardButton("Will I test positive for covid \nafter vaccination?", callback_data ="asd")],
        #     [InlineKeyboardButton("How can I be sure that the \nvaccine I have received is real \nand that I am not being given a fake vaccine?", callback_data ="asdff")],
        #     [InlineKeyboardButton("How long will vaccines protect \nme from covid infection?", callback_data ="asd3f")],
        #     [InlineKeyboardButton("Are there any restrictions on what food I can \neat after getting vaccinated? \nCan I eat non veg food after vaccination?", callback_data ="asdfbds")],
        #     [InlineKeyboardButton("Are there any restrictions\n on alcohol intake \nbefore or after vaccination?", callback_data ="asdfaw")],
        #     [InlineKeyboardButton("I am planning on traveling\n to a foreign country.\n What vaccine should I get?", callback_data ="ashddf")],
        #     [InlineKeyboardButton("Is there some vaccine that\n does not work against\n the Delta variant? Is one vaccine better than the others?", callback_data ="asaadf")],
        #     [InlineKeyboardButton("Can I take doses of two different\n vaccines? Can I get revaccinated\n with a completely different vaccine?", callback_data ="asdbvf")],

        # ])

        # ["Should I get any blood tests before or after getting vaccinated?"],
        # ["Will I test positive for covid after vaccination?"],
        # ["How can I be sure that the vaccine I have received is real and that I am not being given a fake vaccine?"],
        # ["How long will vaccines protect me from covid infection?"],
        # ["Are there any restrictions on what food I can eat after getting vaccinated? Can I eat non veg food after vaccination?"],
        # ["Are there any restrictions on alcohol intake before or after vaccination?"],
        # ["I am planning on traveling to a foreign country. What vaccine should I get?"],
        # ["Is there some vaccine that does not work against the Delta variant? Is one vaccine better than the others?"],
        # ["Can I take doses of two different vaccines? Can I get revaccinated with a completely different vaccine?"]
