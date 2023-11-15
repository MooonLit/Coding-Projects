import streamlit as st
import csv


st.write('Hello this is me using streamlit in python! My name is leo')
with open('restData.csv', 'r') as restData:

    csv_reader = csv.reader(restData)
    mood = st.text_input('What mood are you in?')
    i = 0

    for row in csv_reader:
        if mood:
            mood = mood.lower().strip()

            if mood in row[1]:
                i += 1
                if i == 1:
                    split_address = row[3].split('/')
                    split_row2 = row[2].split('/')
                    instance = 0

                    st.write(f'You may like {row[0]}\n')
                    st.write("")
                    if len(split_row2) > 1:
                        st.write(f'{row[0]} is located in {len(split_address)} locations, here '
                                 f'are the address\'s to those:')
                        for obj in split_row2:
                            if instance > len(split_address):
                                break
                            else:
                                st.write(split_address[instance])
                                instance += 1

                    elif len(split_row2) == 1:
                        st.write(f'{row[0]} is located in {len(split_address)} location, here '
                                 f'is the address to that resteraunt:')
                        st.write(split_address[instance])
                    else:
                        continue
                elif i > 1:
                    split_address = row[3].split('/')
                    split_row2 = row[2].split('/')
                    instance = 0
                    st.write("")
                    st.write("")
                    st.write(f'\n\nYou may also like {row[0]}')
                    st.write("")
                    if len(split_row2) > 1:
                        st.write(f'{row[0]} is located in {len(split_address)} locations, here '
                                 f'are the address\'s to those:')
                        for obj in split_row2:
                            if instance > len(split_address):
                                break
                            else:
                                st.write(split_address[instance])
                                instance += 1

                    elif len(split_row2) == 1:
                        st.write(f'{row[0]} is located in {len(split_address)} location, here '
                                 f'is the address to that resteraunt:')
                        st.write(split_address[instance])
                    else:
                        continue
