# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:44:31 2023

@author: HP
"""


from flask import Flask, request, render_template
from pymongo import MongoClient

dataDictionary = {}
connectionDBString = "mongodb+srv://sanimish:Jumlendi@cluster0.78vccxq.mongodb.net/test"

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def form(): 
    if(request.method=="POST"):
        
        firstName = str(request.form.get("fname"))
        lastName = str(request.form.get("lname"))
        emailHandle = str(request.form.get("email"))
        socialHandle = str(request.form.get("shandle"))
        fSong = str(request.form.get("fsong"))
        fSchool = str(request.form.get("fschool"))
        phoneNo = '+' + str(request.form.get("number"))
        
        isInitialAge = str(request.form.get("initialAge"))
        isMiddleAge = str(request.form.get("middleAge"))
        isAdult = str(request.form.get("adult"))
        isGraduate = str(request.form.get("graduate"))
        isJobAge = str(request.form.get("jobAge"))
        isSeniorAge = str(request.form.get("seniorAge"))
        
        Ppractice = str(request.form.get("practice"))
        Ppreference = str(request.form.get("preference"))
        Ccomments = str(request.form.get("comments"))
        
        dataDictionary = {"Name":firstName+" "+lastName, "Email Handle":emailHandle, "Social Media Handle":socialHandle, "Phone No.":phoneNo, "Favourite Song":fSong, "Your School/College":fSchool, "Initial":isInitialAge, "Middle":isMiddleAge, "Adult":isAdult, "Graduate":isGraduate, "Job":isJobAge, "Senior":isSeniorAge, "Practice":Ppractice, "Preferences":Ppreference, "Comments":Ccomments}
        dupDictionary = {}
        for i in dataDictionary:
            dupDictionary[i]=dataDictionary[i]
            
        databaseClient = MongoClient(connectionDBString)
        dbInstance = databaseClient['data']
        collectionInstance = dbInstance['dataCollection']
        
        collectionInstance.insert_one(dataDictionary)
        
        return dupDictionary
    
    return render_template("smallForm.html")


if(__name__=="__main__"):
    app.run()