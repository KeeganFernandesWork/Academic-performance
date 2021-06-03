import streamlit as st
from sklearn import preprocessing
import pandas as pd
import pickle


categorical = ['gender','NationalITy','PlaceofBirth','StageID','GradeID','SectionID','Topic','Semester','Relation','ParentAnsweringSurvey','StudentAbsenceDays','Class','ParentschoolSatisfaction']
numerical = ['raisedhands','AnnouncementsView','Discussion']
x_features = ['gender','NationalITy','PlaceofBirth','StageID','GradeID','SectionID','Topic','Semester','Relation','ParentAnsweringSurvey','StudentAbsenceDays','Class','ParentschoolSatisfaction','raisedhands','AnnouncementsView','Discussion']
label = "VisITedResources"
model_file = 'Data_science/H4_model.sav'
le_file = 'Data_science/Label_Encoder_2.sav'
model = pickle.load(open(model_file, 'rb'))


st.header("Predict")
gender = st.selectbox("Gender",["M","F"])
nationality = st.selectbox('Nationality',["Egypt",
                                          "Iran",
                                          "Iraq",
                                          "Jordan",
                                          "KW",
                                          "lebanon",
                                          "Lybia",
                                          "Morocco",
                                          "Palestine",
                                          "SaudiArabia",
                                          "Syria",
                                          "Tunis",
                                          "USA",
                                          "venzuela",
                                          ])
place_of_birth = st.selectbox('Place of Birth',[
"Egypt",
"Iran",
"Iraq",
"Jordan",
"KuwaIT",
"lebanon",
'Lybia',
"Morocco",
"Palestine",
"SaudiArabia",
"Syria",
"Tunis",
"USA",
"venzuela"
])
stage_id = st.selectbox('StageID',[
"HighSchool",
"lowerlevel",
"MiddleSchool"
])
grade_level = st.selectbox('GradeID',[
"G-02",
"G-04",
"G-05",
"G-06",
"G-07",
"G-08",
"G-09",
"G-10",
"G-11",
"G-12",
])
topic = st.selectbox('Topic',[
"Arabic",
"Biology",
"Chemistry",
"English",
"French",
"Geology",
"History",
"IT",
"Math",
"Quran",
"Science",
"Spanish",
])
section = st.selectbox('Section',[
"A",
"B",
"C",

])
semester = st.selectbox('Semester',[
"F",
"S"

])
relation = st.selectbox('Relation',[
"Father",
"Mum"
])
parent_answering_survey = st.selectbox('Parent Answering Survey',[
"No",
"Yes",

])
parent_school_satisfaction = st.selectbox('Parent School Satisfaction',[
"Bad",
"Good"
])
student_absence_days = st.selectbox('Student Absence Days',[
"Above-7",
"Under-7",
])
classes_f = st.selectbox('Class',[
"H",
"L",
"M",
])
raise_hands = st.slider('Raised Hands',0,100,1)
discussion = st.slider('Discussion',0,100,1)
announcement = st.slider('Announcement',0,100,1)
if st.button("Submit"):
    X_data = {
        'gender': [gender], 'NationalITy': [ nationality ], 'PlaceofBirth': [ place_of_birth ], 'StageID': [stage_id], 'GradeID':[grade_level],
        'SectionID':[section], 'Topic':[topic], 'Semester':[semester], 'Relation':[relation], 'ParentAnsweringSurvey':[parent_answering_survey],
        'StudentAbsenceDays':[student_absence_days], 'Class':[classes_f], 'ParentschoolSatisfaction':[parent_school_satisfaction],
        'raisedhands' : [raise_hands], 'AnnouncementsView':[announcement], 'Discussion':[discussion]
    }
    df = pd.DataFrame(X_data)
    le = preprocessing.LabelEncoder()
    for x in categorical:
        le.fit(df[x])
        df[x] = le.transform(df[x])
    a = model.predict(df)
    if a == 0:
        st.success("A")
    if a == 1:
        st.success("B")
    if a == 2:
        st.success("C")
