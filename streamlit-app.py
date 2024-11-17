
# 아래와 같은 streamlit의 st.connection 코드 기반에서 csv 파일을 읽어서 sqlite db에 저장하는 구체적인 방법을 코드와 함께 알려줘.

# streamlit_app.py

import streamlit as st
from sqlalchemy import text

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection('pets_db', type='sql')


# Insert some data with conn.session.
with conn.session as s:
    sql = text('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
    s.execute(sql)
    
    sql = text('DELETE FROM pet_owners;')
    s.execute(sql)
    
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for k in pet_owners:
        s.execute(
            text('INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);'),
            params=dict(owner=k, pet=pet_owners[k])
        )
    s.commit()

# Query and display the data you inserted
pet_owners = conn.query('select * from pet_owners')

st.dataframe(pet_owners)
