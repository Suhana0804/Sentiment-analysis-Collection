import tkinter as tk
from textblob import TextBlob
def analysis_sentiment():
    review=c.get("1.0",tk.END)
    if review:
        blob=TextBlob(review)
        polarity=blob.sentiment.polarity
        if polarity>0.6:
            result="positive"
        elif polarity<-0.1:
            result="negative"
        else:
            result="neutral"
        e.config(text=f"sentiment:{result}")
    else:
        e.config(text="please enter a review")
a=tk.Tk()
a.geometry("400x400")
a.title("Sentiment analysis")
b=tk.Label(text="Enter customer review:",fg="purple",bg="light yellow",width=100,height=2,font=("Times New Roman",24))
c=tk.Text(a,height=5,width=40)
d=tk.Button(text="Analysis sentiment",command=analysis_sentiment)
e=tk.Label(text="",width=100,height=2,font=("Times New Roman",20))

b.grid(row=1,column=3)
c.grid(row=3,column=3)
d.grid(row=5,column=3)
e.grid(row=7,column=3)
a.mainloop()