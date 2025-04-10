import pandas as pd

def get_all_jobs():
    df = pd.read_csv('../job_description.csv', encoding='latin1')
    return df['Job Title'].dropna().unique().tolist()

def summarize_jd(job_role):
    df = pd.read_csv('../job_description.csv', encoding='latin1')
    jd = df[df['Job Title'] == job_role].iloc[0]

    return f"""
    Job Title: {jd['Job Title']}
    Skills: {jd['Skills']}
    Experience: {jd['Experience']}
    Responsibilities: {jd['Responsibilities']}
    """
