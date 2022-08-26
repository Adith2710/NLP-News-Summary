import torch
import transformers
import numpy as np
import streamlit as st

st.title("Abstractive Summarization of News Articles ✏️")
text = st.text_input("Input Raw Text:")

state = st.button("Get Summary")

keys=["Short Summary", "Long Summary"]

choose_key = st.radio("Choose Sumarization Type" ,keys)

tokenization_kwargs = {'truncation':True,'max_length':512,'return_tensors':'pt'}
if state:
    if choose_key == "Long Summary":
        st.write("Generating Long Summary")
        summarization_long = transformers.pipeline("summarization", model="google/pegasus-multi_news", tokenizer="google/pegasus-multi_news")
        tokenizer_long = transformers.AutoTokenizer.from_pretrained("google/pegasus-multi_news")
        summary_long_text = tokenizer_long.decode(summarization_long(text, **tokenization_kwargs)[0]["summary_token_ids"])
        st.write(summary_long_text)
    elif choose_key == "Short Summary":
        st.write("Generating Short Summary")
        summarization_short = transformers.pipeline("summarization", model="sshleifer/distilbart-cnn-6-6", tokenizer="sshleifer/distilbart-cnn-6-6")

        tokenizer_short = transformers.AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-6-6")
        summary_short_text = tokenizer_short.decode(summarization_short(text, **tokenization_kwargs)[0]["summary_token_ids"])
        st.write(summary_short_text)




# text= """New York (CNN Business)People are stressed out and exhausted. The past two and a half years, full of public health crises, recession and inflation, have been so eventful that news of a possible alien invasion barely even made a blip. Nights are sleepless and days restless, and we need an extra boost to keep us going. 

# That might help explain why investors are amped for candy, cola and chips. Hershey's (HSY) stock is up 19% this year. Coke (KO) is up nearly 10%. Pepsi (PEP) is up 4%. (Reminder: the overall market is down 10%). Inflation has taken a bite out of retail sales, but people are biting back — and sipping, too. 
# That's good news not only for the giants in the consumer goods industry but also lesser known players. Consider Celsius Holdings (CELH), whose energy drinks are everywhere these days. 
# "The reality of it is that we all need more energy," said John Fieldly, CEO of Celsius. "We're working harder and working longer, and we're never disconnected." Sales of Celsius have surged 137% since last year, and the company reported earnings of 12 cents per share last quarter, up from just one cent last year. 
# Earlier this month, Celsius announced that PepsiCo would make a $550 million investment in the energy drink maker and become its preferred distribution partner.
# "The general sense of those in the industry is that people have come off of a stressful period of uncertainty, and they find comfort in certain beverages and snacks. Even as inflation leads to higher prices they refuse to give up these small luxuries," said Duane Stanford, editor and publisher of Beverage Digest, a business newsletter covering the non-alcoholic drinks industry.
# The appetite for energy drinks is growing. "It's profitable, and large soft drink companies want to be in it. One of the ways they've done it is through these partnerships," said Stanford.
# Celsius markets itself as the ultimate small luxury, the solution to both burnout and anxiety. Celsius claims to give its consumers "healthy energy" without jitters or a comedown and includes ingredients like green tea extract and ginger root. 
# Coffee has become the jolt of choice for many younger consumers who were turned off by the extreme sports vibe of the energy drink market, Stanford said. That's why brands like Celsius are attempting to appeal to a broader audience and to attract Gen Z consumers who were turned off by male bravado marketing. 
# Pepsi's portfolio also includes Rockstar and Mountain Dew Rise. But Coke, which partners with Monster Energy, is currently better positioned in the energy drink sector than Pepsi, says Nik Modi, RBC Capital Markets beverages analyst. 
# Celsius is currently the fifth most popular energy drink on the market, trailing behind Monster (MNST), Red Bull, Bang Energy Drink and Rockstar, but Stanford says that Pepsi is betting it will quickly expand and win market share. 
# The Fed speaks: Expect more rate hikes
# Federal Reserve officials at their July meeting said that they likely won't pull back on interest rate hikes until inflation falls substantially and that a soft landing, in which the US economy avoids a severe downturn, is still possible. 
# The US central bank released the minutes of its two-day meeting last month that resulted in a historically high interest rate hike of 75 basis points.
# Reporters, analysts and investors typically scour over these notes in an attempt to glean any insights into the Fed's thought process and clues as to what will happen at the next meeting. 
# Unfortunately those clues are hard to come by. Fed officials didn't discuss specific amounts of future rate hikes and gave no real timeline, either. 
# It will likely "become appropriate at some point to slow the pace of policy rate increases while assessing the effects of cumulative policy adjustments on economic activity and inflation," the minutes said. 
# The Fed ultimately just wants us to be patient. It will likely "take some time" before the full effects of its policy kick in, it said. In the meantime, it'll continue to closely monitor data and adjust accordingly. 
# American farmers are killing their own crops
# A severe drought and heat waves are devastating American crops.
# Nearly 40% of farmers say that they're plowing their fields and giving up on a harvest that won't reach maturity because of the dry conditions, reports my CNN Business colleague Vanessa Yurkevich. 
# Nearly three quarters of farmers say they've experienced significant crop and income loss due to the lack of rain. Nearly 60% of West, South and Central Plains are experiencing severe drought or worse this year and July was the third-hottest on record for the United States.
# "The effects of this drought will be felt for years to come, not just by farmers and ranchers but also by consumers. Many farmers have had to make the devastating decision to sell off livestock they have spent years raising or destroy orchard trees that have grown for decades," said Zippy Duvall, American Farm Bureau Federation president.
# The Bureau of Labor Statistic's August inflation report shows US consumers are already spending 9.3% more on fruits and vegetables from a year ago. Get ready to shell out even more. 
# It's not just America that's suffering. As my CNN Business colleague Julia Horowitz reports, China and Europe are facing an economic hit from the extreme heat and drought."""
# summary_short_text = tokenizer_short.decode(summarization_short(text, **tokenization_kwargs)[0]["summary_token_ids"])
# print("Short Summary:")
# print(summary_short_text)
# print("\n \n \n \n " )
# print("Long Summary:")
# print(summary_long_text)
# print("\n \n \n \n " )
# st.write(summary_text)
# st.write("\n")


