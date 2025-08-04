# modules/preprocessing.py

import pandas as pd
import logging
import pandas as pd
pd.set_option('future.no_silent_downcasting', True)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        # Convert data types
        df['Credit_History'] = df['Credit_History'].astype('object')
        df['Loan_Amount_Term'] = df['Loan_Amount_Term'].astype('object')

        # Fill missing categorical values
        df['Gender'] = df['Gender'].fillna('Male')
        df['Married'] = df['Married'].fillna(df['Married'].mode()[0])
        df['Dependents'] = df['Dependents'].fillna(df['Dependents'].mode()[0])
        df['Self_Employed'] = df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])
        df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0])
        df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])

        # Fill missing numerical values
        df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())


        # Drop Loan_ID if exists
        if 'Loan_ID' in df.columns:
            df.drop('Loan_ID', axis=1, inplace=True)

        logging.info("Data cleaned successfully.")
        return df

    except Exception as e:
        logging.error("Error in cleaning data: %s", e)
        raise
