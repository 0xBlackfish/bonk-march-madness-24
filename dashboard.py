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
    
def identify_pack_black_brackets(id):
    if id in ['DJGxMzdoTHWEcqhfvhTUu7kRpjMDgqzL7zLbM7eGkjHa','H5sSq7Dno6EqpCuV9x73prdEzrvQ1xZiPNzGS7nLZV2D','H4zRWRAyZFy9DYthqL5PGWudeYjvZncnU1dTwQWzim6X','2YXW5wx1gKsMGvPjy1DnkRDPiT5q9uJN31oPA7N2bKj5','62J3LW5f49ZA8ThaWv6F6xvqmpMYjFPyVfF1hfY8ZnmK','8fYhWG9DECR9vc14ha2eeBXxok5aTFF3sriADnNaTtXQ']:
        return 'Pack'
    elif id in ['6r8ssRbo2XJiiD8g8kjMsBKJi8rA8itu29oShxoQ2kUD','7wzxEsco9CkmPBqzrFA6jZxaWTDzo3kyi1FPwgRz2TbK']:
        return 'Black'
    else:
        return 'Loser'


def score_round_1(selections):
    r1_score = 0
    r1_winners = [
        'UConn',
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
        'Gonzaga',
        'Tennessee',
        'NC State',
        'Illinois',
        'Creighton'
    ]

    r2_ppr = 0
    r2_remaining = [
        'Grand Canyon',
        'Alabama',
        'Clemson',
        'Baylor',
        'Yale',
        'San Diego St.',
        'Houston',
        'Texas A&M',
        'James Madison',
        'Duke',
        'Colorado',
        'Marquette',
        'Purdue',
        'Utah St.'
    ]

    for team in selections:
        if team in r2_winners:
            r2_score += 2
    
    for team in selections:
        if team in r2_remaining:
            r2_ppr += 2

    return r2_score, r2_ppr

def score_sweet_16(selections):
    s16_score = 0
    s16_winners = [
    ]

    s16_ppr = 0
    s16_remaining = [
        'Grand Canyon',
        'Alabama',
        'Clemson',
        'Baylor',
        'Yale',
        'San Diego St.',
        'Houston',
        'Texas A&M',
        'James Madison',
        'Duke',
        'Colorado',
        'Marquette',
        'Purdue',
        'Utah St.',
        'Iowa St.',
        'North Carolina',
        'Arizona',
        'Gonzaga',
        'Tennessee',
        'NC State',
        'Illinois',
        'Creighton'
    ]

    for team in selections:
        if team in s16_winners:
            s16_score += 4
    
    for team in selections:
        if team in s16_remaining:
            s16_ppr += 4

    return s16_score, s16_ppr

def score_elite_8(selections):
    e8_score = 0
    e8_winners = [
    ]

    e8_ppr = 0
    e8_remaining = [
        'Grand Canyon',
        'Alabama',
        'Clemson',
        'Baylor',
        'Yale',
        'San Diego St.',
        'Houston',
        'Texas A&M',
        'James Madison',
        'Duke',
        'Colorado',
        'Marquette',
        'Purdue',
        'Utah St.',
        'Iowa St.',
        'North Carolina',
        'Arizona',
        'Gonzaga',
        'Tennessee',
        'NC State',
        'Illinois',
        'Creighton'
    ]

    for team in selections:
        if team in e8_winners:
            e8_score += 8
    
    for team in selections:
        if team in e8_remaining:
            e8_ppr += 8

    return e8_score, e8_ppr

def score_final_four(selections):
    f4_score = 0
    f4_winners = [
    ]

    f4_ppr = 0
    f4_remaining = [
        'Grand Canyon',
        'Alabama',
        'Clemson',
        'Baylor',
        'Yale',
        'San Diego St.',
        'Houston',
        'Texas A&M',
        'James Madison',
        'Duke',
        'Colorado',
        'Marquette',
        'Purdue',
        'Utah St.',
        'Iowa St.',
        'North Carolina',
        'Arizona',
        'Gonzaga',
        'Tennessee',
        'NC State',
        'Illinois',
        'Creighton'
    ]

    for team in selections:
        if team in f4_winners:
            f4_score += 16
    
    for team in selections:
        if team in f4_remaining:
            f4_ppr += 16

    return f4_score, f4_ppr

def score_final(selections):
    final_score = 0
    final_winners = [
    ]

    final_ppr = 0
    final_remaining = [
        'Grand Canyon',
        'Alabama',
        'Clemson',
        'Baylor',
        'Yale',
        'San Diego St.',
        'Houston',
        'Texas A&M',
        'James Madison',
        'Duke',
        'Colorado',
        'Marquette',
        'Purdue',
        'Utah St.',
        'Iowa St.',
        'North Carolina',
        'Arizona',
        'Gonzaga',
        'Tennessee',
        'NC State',
        'Illinois',
        'Creighton'
    ]

    for team in selections:
        if team in final_winners:
            final_score += 32
    
    for team in selections:
        if team in final_remaining:
            final_ppr += 32

    return final_score, final_ppr

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

## Add Scores
df_brackets['r1_score'] = df_brackets['round_of_32'].apply(lambda  x: score_round_1(x))
df_brackets['r2_score'] = df_brackets['sweet_16'].apply(lambda x: score_round_2(x)[0])
df_brackets['total_score'] = df_brackets['r1_score'] + df_brackets['r2_score']

## Add Points Possible Remaining
df_brackets['r2_ppr'] = df_brackets['sweet_16'].apply(lambda x: score_round_2(x)[1]) 
df_brackets['s16_ppr'] = df_brackets['elite_8'].apply(lambda x: score_sweet_16(x)[1])
df_brackets['e8_ppr'] = df_brackets['final_four'].apply(lambda x: score_elite_8(x)[1])
df_brackets['f4_ppr'] = df_brackets['championship'].apply(lambda x: score_final_four(x)[1])
df_brackets['final_ppr'] = df_brackets['winner'].apply(lambda x: score_final(x)[1])
df_brackets['ppr'] = df_brackets['r2_ppr'] + df_brackets['s16_ppr'] + df_brackets['e8_ppr'] + df_brackets['f4_ppr'] + df_brackets['final_ppr']
df_brackets.drop(columns=['r2_ppr','s16_ppr','e8_ppr','f4_ppr','final_ppr'],inplace=True)

## Add Rank and Other Fields
df_brackets['overall_rank'] = df_brackets['total_score'].rank(method='min', ascending=False)
df_brackets['bracket_owner'] = df_brackets['id'].apply(identify_pack_black_brackets)
df_brackets['tensor_link'] = 'https://www.tensor.trade/item/'+df_brackets['id']

## List of NCAA tourney teams
ncaa_tourney_teams = [
    'All',
    'Akron',
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
    'Yale'
]

## Create dashboard filters
filter1, filter2, filter3, filter4, filter5, filter6, filter7 = st.columns(7)

with filter1:
    filter_winner = st.multiselect("Winner", ncaa_tourney_teams, 'All')
with filter2:
    filter_championship = st.multiselect("Championship", ncaa_tourney_teams, 'All')
with filter3:
    filter_final_four = st.multiselect("Final Four", ncaa_tourney_teams, 'All')
with filter4:
    filter_elite_8 = st.multiselect("Elite 8", ncaa_tourney_teams, 'All')
with filter5:
    filter_sweet_16 = st.multiselect("Sweet 16", ncaa_tourney_teams, 'All')
with filter6:
    filter_round_of_32 = st.multiselect("Round of 32", ncaa_tourney_teams, 'All')
with filter7:
    filter_pack_black = st.multiselect("Bracket Owner", ['All','Pack','Black','Loser'], 'All')

df_filtered = df_brackets[
    ((df_brackets['bracket_owner'].isin(filter_pack_black)) | ('All' in filter_pack_black)) &
    ((df_brackets['winner'].isin(filter_winner)) | ('All' in filter_winner)) &
    ((df_brackets['championship'].apply(lambda x: any(item in filter_championship for item in x))) | ('All' in filter_championship)) &
    ((df_brackets['final_four'].apply(lambda x: any(item in filter_final_four for item in x))) | ('All' in filter_final_four)) &
    ((df_brackets['elite_8'].apply(lambda x: any(item in filter_elite_8 for item in x))) | ('All' in filter_elite_8)) &
    ((df_brackets['sweet_16'].apply(lambda x: any(item in filter_sweet_16 for item in x))) | ('All' in filter_sweet_16)) &
    ((df_brackets['round_of_32'].apply(lambda x: any(item in filter_round_of_32 for item in x))) | ('All' in filter_round_of_32))
]

st.dataframe(df_filtered.sort_values(by='total_score',ascending=False).reset_index(drop=True),use_container_width=True)
