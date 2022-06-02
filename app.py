import numpy as np
import pickle
import pandas as pd
import streamlit as st 


#pickle_in = open("regressor.pkl","rb")
regressor=pickle.load(open("regressor.pkl","rb"))

def welcome():
    return "Welcome All"
def predict_note_performance(environmentsatisifaction,JobInvolvement,JobSatisfaction,Experience,WorkLifeBalance,BehaviourialCompetence,OntimeDelivery,Feedbacks,TicketSolvingManagements,ProjectevlautionorCompleteion,AnnualIncome,Workinghrs,PsychoSocialIndicators,PercentSalaryHike):
    
    """Let's calculate the performance rating 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: environmentsatisifaction
        required: true
      - name: JobInvolvement
        required: true
      - name: JobSatisfaction
        required: true
      - name: Experience
        required: true
      - name: WorkLifeBalance
        required: true
      - name: BehaviourialCompetence
        required: true
      - name: OntimeDelivery
        required: true
      - name: Feedbacks
        required: true
      - name: TicketSolvingManagements
        required: true
      - name: ProjectevlautionorCompleteion
        required: true
      - name: AnnualIncome
        required: true
      - name: Workinghrs 
        required: true
      - name: PsychoSocialIndicators
        required: true
      - name: PercentSalaryHike
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=regressor.predict([[environmentsatisifaction,JobInvolvement,JobSatisfaction,Experience,WorkLifeBalance,BehaviourialCompetence,OntimeDelivery,Feedbacks,TicketSolvingManagements,ProjectevlautionorCompleteion,AnnualIncome,Workinghrs,PsychoSocialIndicators,PercentSalaryHike]])
    print(prediction)
    return prediction
    

def main():
    st.title("Employee Performance Analysis")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> Employee Performance Analysis ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    environmentsatisifaction = st.selectbox("environmentsatisifaction",options=[1,2,3,4,5])
    JobInvolvement = st.selectbox("JobInvolvement",options=[1,2,3,4,5])
    JobSatisfaction = st.selectbox("JobSatisfaction",options=[1,2,3,4,5])
    Experience = st.selectbox("Experience",options=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
    WorkLifeBalance = st.selectbox("WorkLifeBalance",options=[1,2,3,4,5])
    BehaviourialCompetence = st.selectbox("BehaviourialCompetence",options=[1,2,3,4,5])
    OntimeDelivery = st.selectbox("OntimeDelivery",options=[1,2,3,4,5])
    Feedbacks = st.selectbox("Feedbacks",options=[1,2,3,4,5])
    TicketSolvingManagements = st.selectbox("TicketSolvingManagements",options=[1,2,3,4,5])
    ProjectevlautionorCompleteion = st.selectbox("ProjectevlautionorCompleteion",options=[1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    AnnualIncome = st.selectbox("AnnualIncome",options=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
    Workinghrs = st.selectbox("Workinghrs",options=[9,10,11,12,13,14,15])
    PsychoSocialIndicators = st.selectbox("PsychoSocialIndicators",options=[1,2,3,4,5])
    PercentSalaryHike = st.selectbox("PercentSalaryHike",options=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    result=""
    if st.button("Predict"):
        result=predict_note_performance(environmentsatisifaction,JobInvolvement,JobSatisfaction,Experience,WorkLifeBalance,BehaviourialCompetence,OntimeDelivery,Feedbacks,TicketSolvingManagements,ProjectevlautionorCompleteion,AnnualIncome,Workinghrs,PsychoSocialIndicators,PercentSalaryHike)
    st.success('The output is {}'.format(result))
 
    
 # convert string into int
    result = float(result)
    if result < 5.0:
       st.text("performance is bad need to improve")

    else:
       st.text("your performance is good keep going")


if __name__=='__main__':
    main()
    

#run the above code as streamlit run app2.py