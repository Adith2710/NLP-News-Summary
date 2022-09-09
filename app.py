import torch
import transformers
import numpy as np
import streamlit as st
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup






st.title("Abstractive Summarization of News Articles ✏️")
types= ["URL", "Raw Text"]
choose_type= st.radio("Choose Type of Input", types)

if choose_type== "Raw Text":
    text = st.text_input("Input Raw Text:")

    state = st.button("Get News Summary")

    keys=["Summary Version 1", "Summary Version 2"]

    choose_key = st.radio("Choose Sumarization Type" ,keys)

    tokenization_kwargs = {'truncation':True,'max_length':512,'return_tensors':'pt'}
    if state:
        if choose_key == "Summary Version 2":
            st.write("Generating Summary Version 2")
            summarization_long = transformers.pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", tokenizer="sshleifer/distilbart-cnn-12-6")
            tokenizer_long = transformers.AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
            summary_long_text = tokenizer_long.decode(summarization_long(text, **tokenization_kwargs)[0]["summary_token_ids"])
            st.write(summary_long_text)
        elif choose_key == "Summary Version 1":
            st.write("Generating Summary Version 1")
            summarization_short = transformers.pipeline("summarization", model="sshleifer/distilbart-cnn-6-6", tokenizer="sshleifer/distilbart-cnn-6-6")

            tokenizer_short = transformers.AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-6-6")
            summary_short_text = tokenizer_short.decode(summarization_short(text, **tokenization_kwargs)[0]["summary_token_ids"])
            st.write(summary_short_text)



elif choose_type== "URL":

    text = st.text_input("Input URL:")

    state = st.button("Get News Summary")
    
    

    keys=["Summary Version 1", "Summary Version 2"]

    choose_key = st.radio("Choose Sumarization Type" ,keys)

    tokenization_kwargs = {'truncation':True,'max_length':512,'return_tensors':'pt'}
    if text.isalpha()== True:
        if state:
            url = text
            html = urlopen(url).read()
            soup = BeautifulSoup(html, features="html.parser")

            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()    # rip it out

            # get text
            text = soup.get_text()

            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)

            if choose_key == "Summary Version 2":
                st.write("Generating Summary Version 2")
                summarization_long = transformers.pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", tokenizer="sshleifer/distilbart-cnn-12-6")
                tokenizer_long = transformers.AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
                summary_long_text = tokenizer_long.decode(summarization_long(text, **tokenization_kwargs)[0]["summary_token_ids"])
                st.write(summary_long_text)
            elif choose_key == "Summary Version 1":
                st.write("Generating Summary Version 1")
                summarization_short = transformers.pipeline("summarization", model="sshleifer/distilbart-cnn-6-6", tokenizer="sshleifer/distilbart-cnn-6-6")

                tokenizer_short = transformers.AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-6-6")
                summary_short_text = tokenizer_short.decode(summarization_short(text, **tokenization_kwargs)[0]["summary_token_ids"])
                st.write(summary_short_text)





