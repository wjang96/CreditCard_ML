#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request


# In[2]:


import joblib


# In[3]:


app = Flask(__name__)


# In[4]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        purchases = float(request.form.get("purchases"))
        suppcard = float(request.form.get("suppcard"))
        print(purchases, suppcard)
        model1 = joblib.load("LogReg")
        pred1 = model1.predict([[purchases, suppcard]])
        model2 = joblib.load("CART")
        pred2 = model2.predict([[purchases, suppcard]])
        model3 = joblib.load("RF")
        pred3 = model3.predict([[purchases, suppcard]])
        model4 = joblib.load("GB")
        pred4 = model4.predict([[purchases, suppcard]])
        return(render_template("index.html", result1=pred1, result2=pred2, result3=pred3, result4=pred4))
    else:
        return(render_template("index.html", result1="waiting", result2="waiting", result3="waiting", result4="waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




