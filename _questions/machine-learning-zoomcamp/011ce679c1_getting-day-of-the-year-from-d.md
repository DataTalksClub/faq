---
course: machine-learning-zoomcamp
id: 011ce679c1
question: Getting day of the year from day and month column
section: Miscellaneous
sort_order: 4040
---

Problem description: I have one column day_of_the_month . It has values 1, 2, 20, 25 etc. and int . I have a second column month_of_the_year. It has values jan, feb, ..dec. and are string. I want to convert these two columns into one column day_of_the_year and I want them to be int. 2 and jan should give me 2, i.e. 2nd day of the year, 1 and feb should give me 32, i.e. 32 nd day of the year. What is the simplest pandas-way to do it?

Solution description:

convert dtype in day_of_the_month column from int to str with df['day_of_the_month'] = df['day_of_the_month'].map(str)

convert month_of_the_year column in jan, feb ...,dec into 1,2, ..,12 string using map()

convert day and month into a datetime object with:

df['date_formatted'] = pd.to_datetime(

dict(

year='2055',

month=df['month'],

day=df['day']

)

)

get day of year with: df['day_of_year']=df['date_formatted'].dt.dayofyear

(Bhaskar Sarma)

