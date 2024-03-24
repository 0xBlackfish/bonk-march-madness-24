import pandas as pd
import streamlit as st
from datetime import datetime, date
import hmac
import ast

st.set_page_config(page_title='Bonk March Madness 2024',layout='wide')

st.title('Bonk March Madness 2024')

# Password protection
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the passward is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.

## Utility Functions
def parse_list(s):
    try:
        return ast.literal_eval(s)
    except (SyntaxError, ValueError):
        return None  # Return None if the parsing fails

def score_round_1(selections):
    r1_score = 0
    r1_winners = [
        'Uconn',
        'Northwestern',
        'San Diego St.',
        'Yale',
        'Duquesne',
        'Illinois',
        'Washington St.',
        'Iowa St.',
        'North Carolina',
        'Michigan St.',
        'Grand Canyon',
        'Alabama',
        'Clemson',
        'Baylor',
        'Dayton',
        'Arizona',
        'Houston',
        'Texas A&M',
        'James Madison',
        'Duke',
        'NC State',
        'Oakland',
        'Colorado/Boise St.',
        'Marquette',
        'Purdue',
        'Utah St.',
        'Gonzaga',
        'Kansas',
        'Oregon',
        'Creighton',
        'Texas',
        'Tennessee'
    ]

    for team in selections:
        if team in r1_winners:
            r1_score += 1

    return r1_score

def score_round_2(selections):
    r2_score = 0
    r2_winners = [
        'Iowa St.',
        'North Carolina',
        'Arizona',
        'Gonzaga'
    ]

    for team in selections:
        if team in r2_winners:
            r2_score += 2

    return r2_score

## Read data from CSV files
df_brackets = pd.read_csv(
    './bracket-data/brackets_final.csv',
    converters={
        'round_of_32': parse_list,
        'sweet_16': parse_list,
        'elite_8': parse_list,
        'final_four' : parse_list,
        'championship' : parse_list
    }
)

df_brackets['r1_score'] = df_brackets['round_of_32'].apply(score_round_1)
df_brackets['r2_score'] = df_brackets['sweet_16'].apply(score_round_2)
df_brackets['total_score'] = df_brackets['r1_score'] + df_brackets['r2_score']

## List of NCAA tourney teams
ncaa_tourney_teams = ['Akron',
 'Alabama',
 'Arizona',
 'Auburn',
 'BYU',
 'Baylor',
 'Boise St.',
 'Charleston',
 'Clemson',
 'Colgate',
 'Colorado',
 'Colorado St.',
 'Creighton',
 'Dayton',
 'Drake',
 'Duke',
 'Duquesne',
 'Florida',
 'Florida Atlantic',
 'Gonzaga',
 'Grambling St.',
 'Grand Canyon',
 'Houston',
 'Howard',
 'Illinois',
 'Iowa St.',
 'James Madison',
 'Kansas',
 'Kentucky',
 'Long Beach St.',
 'Longwood',
 'Marquette',
 'McNeese',
 'Michigan St.',
 'Mississippi St.',
 'Montana St.',
 'Morehead St.',
 'NC St.',
 'Nebraska',
 'Nevada',
 'New Mexico',
 'North Carolina',
 'Northwestern',
 'Oakland',
 'Oregon',
 'Purdue',
 "Saint Mary's",
 "Saint Peter's",
 'Samford',
 'San Diego St.',
 'South Carolina',
 'South Dakota St.',
 'Stetson',
 'TCU',
 'Tennessee',
 'Texas',
 'Texas A&M',
 'Texas Tech',
 'UAB',
 'UConn',
 'Utah St.',
 'Vermont',
 'Virginia',
 'Wagner',
 'Washington St.',
 'Western Kentucky',
 'Wisconsin',
 'Yale']

## Create dashboard filters
filter1, filter2, filter3, filter4, filter5, filter6 = st.columns(6)

with filter1:
    filter_winner = st.multiselect("Winner", ncaa_tourney_teams)
with filter2:
    filter_championship = st.multiselect("Championship", ncaa_tourney_teams)
with filter3:
    filter_final_four = st.multiselect("Final Four", ncaa_tourney_teams)
with filter4:
    filter_elite_8 = st.multiselect("Elite 8", ncaa_tourney_teams)
with filter5:
    filter_sweet_16 = st.multiselect("Sweet 16", ncaa_tourney_teams)
with filter6:
    filter_round_of_32 = st.multiselect("Round of 32", ncaa_tourney_teams)

st.dataframe(df_brackets.sort_values(by='total_score',ascending=False).reset_index(drop=True))
