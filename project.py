from flask import Flask, render_template
import pandas as pd
import  plotly.express as px
import numpy as np

app = Flask(__name__)

def load_data():
    df = pd.read_csv('dataset/data.csv')
    return df 

@app.route('/')
def index():
    return render_template('graph1.html')
    
@app.route('/graph/1')
def graph1():
    rain=  load_data()
    grouped_obj = rain.groupby(["YEAR"]).sum()
    fig = px.area(grouped_obj, x=grouped_obj.index, y='ANNUAL', title='Rainfall year-wise')
    conclusion = 'The graph shows the yearly rainfall.'
    fig.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))
  
    fig1 = px.bar(grouped_obj, x=grouped_obj.index, y='ANNUAL', title='Rainfall month-wise')
    conclusion = 'The graph shows the monthly rainfall.'
    fig1.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month1= ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT','NOV', 'DEC']
    fig2 = px.bar(grouped_obj, x=grouped_obj.index, y=month1, title='Rainfall month-wise',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows the monthly rainfall.'
    fig2.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    return render_template('graph1.html', fig =fig.to_html(), fig1=fig1.to_html(), fig2=fig2.to_html())


@app.route('/graph/2')
def graph2():
    rain=  load_data()
    grouped_obj = rain.groupby(["YEAR"]).sum()
    month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN']
    fig = px.bar(grouped_obj, x=grouped_obj.index, y=month, title='Rainfall semi-annual',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows the Half Yearly rainfall.'
    fig.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))
  

    month1 = ['JUL', 'AUG', 'SEP', 'OCT','NOV', 'DEC']
    fig1 = px.bar(grouped_obj, x=grouped_obj.index, y=month1, title='Rainfall semi-annual',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows the Half-Yearly rainfall.'
    fig1.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))


    month2 = ['JAN', 'FEB', 'MAR']
    fig2 = px.bar(grouped_obj, x=grouped_obj.index, y=month2, title='Rainfall quater-wise',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows the Quarterly rainfall.'
    fig2.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    return render_template('graph2.html', fig =fig.to_html(), fig1=fig1.to_html(), fig2=fig2.to_html())


@app.route('/graph/3')
def graph3():
    rain=  load_data()
    grouped_obj = rain.groupby(["YEAR"]).sum()
    month = ['APR', 'MAY', 'JUN']
    fig = px.bar(grouped_obj, x=grouped_obj.index, y=month, title='Rainfall quater-wise',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows the monthly rainfall.'
    fig.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month1 = ['JUL', 'AUG', 'SEP']
    fig1 = px.bar(grouped_obj, x=grouped_obj.index, y=month1, title='Rainfall quater-wise',labels={'index':'YEAR', 'value':' Rainfall (in mm)'})
    conclusion = 'The graph shows the monthly rainfall.'
    fig1.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month2 = ['OCT','NOV', 'DEC']
    fig2 = px.bar(grouped_obj, x=grouped_obj.index, y=month2, title='Rainfall quater-wise',labels={'index':'YEAR', 'value':' Rainfall (in mm)'})
    conclusion = 'The graph shows the monthly rainfall.'
    fig2.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    return render_template('graph3.html', fig =fig.to_html(), fig1=fig1.to_html(), fig2=fig2.to_html())


@app.route('/graph/4')
def graph4():
    rain=  load_data()
    grouped_obj = rain.groupby(["YEAR"]).sum()
    fig = px.scatter(grouped_obj, x=grouped_obj.index, y='ANNUAL', title='Rainfall year-wise')
    conclusion = 'The graph shows the yearly rainfall.'
    fig.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    month=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG','SEP', 'OCT','NOV', 'DEC']
    fig1 = px.ecdf(grouped_obj, x=grouped_obj.index,y=month, title='Rainfall Yearly')
    conclusion = 'The graph shows the yearly rainfall.'
    fig1.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))

    fig2 = px.area(grouped_obj, x=grouped_obj.index, y='ANNUAL', title='Yearly rainfall state-wise')
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig2.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))
    fig2.show()

    return render_template('graph4.html', fig =fig.to_html(), fig1=fig1.to_html(), fig2=fig2.to_html())


@app.route('/graph/5')
def graph5():
    rain=  load_data()
    grouped_obj = rain.groupby(["SUBDIVISION"]).sum()
    grouped_obj.drop(['YEAR'], axis=1, inplace=True)
    fig = px.area(rain, x='SUBDIVISION', y=['ANNUAL'], title='Average Rainfall ',labels={'value':'Rainfall in mm'})
    mean_rainfall = rain['ANNUAL'].mean()
    fig.add_annotation(xref='paper', yref='paper', x=0.1, y=1, text=f"Average Rain = {mean_rainfall:.0f}",showarrow=False)
    fig.show()

    fig1 = px.bar(grouped_obj, x=grouped_obj.index, y='ANNUAL', title='State-wise')
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig1.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))
    fig1.show()

    month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT','NOV', 'DEC']
    fig2 = px.bar(grouped_obj, x=grouped_obj.index, y=month, title='State-wise',height=600,labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig2.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))
    fig2.show()

    return render_template('graph5.html', fig =fig.to_html(), fig1=fig1.to_html(), fig2=fig2.to_html())



@app.route('/graph/6')
def graph6():
    rain=  load_data()
    grouped_obj = rain.groupby(["SUBDIVISION"]).sum()
    grouped_obj.drop(['YEAR'], axis=1, inplace=True)
    month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN']
    fig = px.funnel(grouped_obj, x=grouped_obj.index, y=month, title='State-wise',height=600)
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))
    fig.show()

    month1 = ['JUL', 'AUG', 'SEP', 'OCT','NOV', 'DEC']
    fig1 = px.funnel(grouped_obj, x=grouped_obj.index, y=month1, title='State-wise',height=600)
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig1.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))
    fig1.show()

    month2 = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG','SEP', 'OCT','NOV', 'DEC']
    fig2 = px.density_contour(grouped_obj, x=grouped_obj.index, y=month2, title='State-wise',height=600,labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig2.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))
    fig2.show()

    return render_template('graph6.html', fig =fig.to_html(), fig1=fig1.to_html(), fig2=fig2.to_html())

@app.route('/graph/7')
def graph7():
    rain=  load_data()
    grouped_obj = rain.groupby(["SUBDIVISION"]).sum()
    grouped_obj.drop(['YEAR'], axis=1, inplace=True)
    month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN']
    fig = px.ecdf(grouped_obj,x=grouped_obj.index, y=month, title='State-wise',height=600)
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))
    fig.show()

    month1 = ['JUL', 'AUG', 'SEP', 'OCT','NOV', 'DEC']
    fig1 = px.ecdf(grouped_obj,x=grouped_obj.index, y=month1, title='State-wise',height=600)
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig1.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))
    fig1.show()

    month2 = ['JAN', 'FEB', 'MAR'] 
    fig2 = px.line(grouped_obj, x=grouped_obj.index, y=month2, title='Rainfall quaterly-wise',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig2.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))
    fig2.show()

    return render_template('graph7.html', fig =fig.to_html(), fig1=fig1.to_html(), fig2=fig2.to_html()) 


@app.route('/graph/8')
def graph8():
    rain=  load_data()
    grouped_obj = rain.groupby(["SUBDIVISION"]).sum()
    grouped_obj.drop(['YEAR'], axis=1, inplace=True)
    month = ['APR', 'MAY', 'JUN']
    fig = px.line(grouped_obj, x=grouped_obj.index, y=month, title='State-wise',height=600,labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12)) 
    fig.show()

    month1 = ['JUL', 'AUG', 'SEP']
    fig1 = px.line(grouped_obj, x=grouped_obj.index, y=month1, title='State-wise',height=600,labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig1.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12)) 
    fig1.show()

    month2 = ['OCT','NOV', 'DEC']
    fig2 = px.line(grouped_obj, x=grouped_obj.index, y=month2, title='State-wise',height=600,labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows rainfall from every State and UT.'
    fig2.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12)) 
    fig2.show()

    return render_template('graph8.html', fig =fig.to_html(), fig1=fig1.to_html(), fig2=fig2.to_html())

@app.route('/graph/9')
def graph9():
    rain =  load_data()
    grouped_obj = rain.groupby(["YEAR"]).sum()
    grouped_obj.drop(['ANNUAL'], axis=1, inplace=True)
    month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT','NOV', 'DEC']
    fig = px.area(grouped_obj, x=grouped_obj.index, y=month, title='Rainfall YEAR-wise',labels={'value':'Rainfall in mm'})
    conclusion = 'The graph shows  monthly rainfall.'
    fig.add_annotation(text=conclusion, xref='paper', yref='paper', x=.5, y=1, bgcolor='grey', showarrow=False, font=dict(size=12))
    fig.show()


    return render_template('graph9.html', fig =fig.to_html())

@app.route('/graph/10')
def graph10():
    rain=  load_data()
    grouped_obj = rain.groupby(['ANNUAL']).sum()
    grouped_obj.drop(['YEAR'], axis=1, inplace=True)
    grouped_obj.reset_index(inplace=True)
    fig1 = px.scatter(grouped_obj, x='ANNUAL', y=['JAN','FEB','MAR'], title='Rainfall in First Quarter', trendline='ols', log_y=True,labels={'value':'Rainfall in mm'})
    fig1.show()

    fig2 = px.scatter(grouped_obj, x='ANNUAL', y=['APR','MAY','JUN'], title='Rainfall in Second Quarter', trendline='ols', log_y=True,labels={'value':'Rainfall in mm'})
    fig2.show()

    return render_template('graph10.html', fig1 =fig1.to_html(), fig2=fig2.to_html())

@app.route('/graph/11')
def graph11():
    rain =  load_data()
    grouped_obj = rain.groupby(['ANNUAL']).sum()
    grouped_obj.drop(['YEAR'], axis=1, inplace=True)
    grouped_obj.reset_index(inplace=True)
    fig = px.scatter(grouped_obj, x='ANNUAL', y=['JUL','AUG','SEP'], title='Rainfall in Third Quarter', trendline='ols', log_y=True,labels={'value':'Rainfall in mm'})
    fig.show()

    fig1 = px.scatter(grouped_obj, x='ANNUAL', y=['OCT','NOV','DEC'], title='Rainfall in Fourth Quarter', trendline='ols', log_y=True,labels={'value':'Rainfall in mm'})
    fig1.show()

    fig2 = px.scatter(grouped_obj, x=['JAN','MAR','MAY', 'JUL', 'SEP', 'NOV'], y='ANNUAL', title='Rainfall in Half-Yearly basis', trendline='ols', log_y=True,labels={'value':'Rainfall in mm'})
    fig2.show()

    return render_template('graph10.html', fig =fig.to_html(), fig1=fig1.to_html(), fig2=fig2.to_html())

@app.route('/graph/12')
def graph12():
    rain =  load_data()
    grouped_obj = rain.groupby(['ANNUAL']).sum()
    grouped_obj.drop(['YEAR'], axis=1, inplace=True)
    grouped_obj.reset_index(inplace=True)
    fig = px.scatter(grouped_obj, x=['FEB','APR','JUN', 'AUG', 'OCT', 'DEC'], y='ANNUAL', title='Rainfall in Half-Yearly Basis', trendline='ols', log_y=True,labels={'value':'Rainfall in mm'})
    fig.show()

    return render_template('graph12.html', fig =fig.to_html())  


@app.route('/graph/13')
def graph13():
    rain=  load_data()
    rain.sort_values(by="YEAR", inplace=True)
    fig=px.scatter_mapbox(
         rain, lat="Latitude", lon="Longitude", color="ANNUAL", size="ANNUAL",
    color_continuous_scale=px.colors.sequential.Plasma, size_max=50, zoom=3,
    mapbox_style="carto-positron", title='Annual Rainfall in India', height=800,
    animation_frame='YEAR', animation_group='SUBDIVISION')
    fig.show()

    return render_template('graph13.html', fig =fig.to_html())



def retreive_data():
    df = pd.read_csv('dataset/rainfall_India_2017.csv')
    return df 


@app.route('/eda/1')
def eda1():
    return render_template('eda1.html')     

    


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)