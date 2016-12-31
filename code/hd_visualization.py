import csv
import matplotlib.pyplot as plt
from pylab import plot, show, savefig
import numpy as np
import os
import sys
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
from wordcloud import WordCloud


py.sign_in('ahmedss', 'txo3OeybB5fgLuKpnaJ0')

def LineChart(filepath):

    if os.path.isfile(filepath):
        input_file = open(filepath,'r')
    else:
        print "File does NOT exist"
        sys.exit()

    rdr = csv.reader(input_file)
    header = rdr.next()
    input_data = [ [] , [] ]

    count = 0

    for l in input_file:
        line = l.split(',')
        count += 1
        for i in range(len(line)):
            input_data[i].append(line[i])

    #print count, type(input_data[0]), type(input_data[1])

    plt.clf()
    plt.plot(input_data[0], input_data[1])
    plt.ylabel('Search Relevancy')
    plt.xlabel('Product Id')
    plt.title('Line chart - Search Relevancy/Product Id')
    savefig(os.path.dirname(os.path.abspath(__file__))+'/Output/Visualization/LineChart - Search Relevancy VS Product Id.png')
    plt.show()

    plt.clf()
    plt.plot(input_data[1], input_data[0])
    plt.xlabel('Search Relevancy')
    plt.ylabel('Product Id')
    plt.title('Line chart - Product Id/Search Relevancy')
    savefig(os.path.dirname(os.path.abspath(__file__))+'/Output/Visualization/LineChart - Product Id VS Search Relevancy.png')
    plt.show()

    round_off_relevance = [float("%.2f" % float(i))  for i in input_data[1]]
    minrelevance = min(round_off_relevance)
    maxrelevance = max(round_off_relevance)
    all_relevance = np.arange(minrelevance, maxrelevance+0.01, 0.01)
    relevance_count = []
    for i in range(int(minrelevance*100), int(maxrelevance*100)+1):
        relevance_count.append(round_off_relevance.count(float(float(i)/100)))

    data = [go.Scatter(x = all_relevance, y = relevance_count)]
    layout = go.Layout (
        title = 'LineChart - Relevancy Count/Relevancy',
        xaxis = dict(
            title = 'Relevancy'
        ),
        yaxis = dict(
            title = 'Relevancy Count'
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig,filename = 'LineChart - Relevancy Count VS Possible Relevancy')
    print 'LineChart - Relevancy Count VS Possible Relevancy', plot_url


def Histogram(filepath):
    if os.path.isfile(filepath):
        input_file = open(filepath,'r')
    else:
        print "File does NOT exist"
        sys.exit()

    rdr = csv.reader(input_file)
    header = rdr.next()
    input_data = [ [] , [] ]

    count = 0

    for l in input_file:
        line = l.split(',')
        count += 1
        for i in range(len(line)):
            input_data[i].append(line[i])

    round_off_relevance = [float("%.2f" % float(i))  for i in input_data[1]]
    minrelevance = min(round_off_relevance)
    maxrelevance = max(round_off_relevance)
    all_relevance = np.arange(minrelevance, maxrelevance+0.01, 0.01)
    relevance_count = []
    for i in range(int(minrelevance*100), int(maxrelevance*100)+1):
        relevance_count.append(round_off_relevance.count(float(float(i)/100)))

    data = [go.Histogram(x = round_off_relevance, opacity = 0.8)]
    layout = go.Layout (
        bargap = 0.35,
        title = 'Histogram - Frequency of Relevancies',
        xaxis = dict(
            title = 'Relevancy'
        ),
        yaxis = dict(
            title = 'Frequency'
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig,filename = 'Histogram - Frequency of Relevancies')
    print 'Histogram - Frequency of Relevancies', plot_url


def Wordcloud(filepath1,filepath2,filepath3):
    if os.path.isfile(filepath1):
        input_file1 = open(filepath1,'r')
    else:
        print "File does NOT exist"
        sys.exit()

    rdr = csv.reader(input_file1)
    header = rdr.next()
    output_data = [[] for i in header]
    
    output_count = 0
    actual_count = 0
    for l in input_file1:
        line = l.split(',')
        output_count += 1
        if len(line) == len(output_data):
            actual_count += 1
            for i in range(len(line)):
                output_data[i].append(line[i])
                #print i, line[i]
    
    plt.clf()
    wordcloud = WordCloud().generate(" ".join(output_data[3]))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.title('Word Cloud - Search Terms(in Train Data)')
    savefig(os.path.dirname(os.path.abspath(__file__))+'/Output/Visualization/WordCloud - Search Terms(in Train Data).png')
    plt.show()
    input_file1.close()


    if os.path.isfile(filepath2):
        input_file2 = open(filepath2,'r')
    else:
        print "File does NOT exist"
        sys.exit()

    rdr = csv.reader(input_file2)
    header = rdr.next()
    output_data = [[] for i in header]
    
    output_count = 0
    actual_count = 0
    for l in input_file2:
        line = l.split(',')
        output_count += 1
        if len(line) == len(output_data):
            actual_count += 1
            for i in range(len(line)):
                output_data[i].append(line[i])
                #print i, line[i]
    
    plt.clf()
    wordcloud = WordCloud().generate(" ".join(output_data[3]))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.title('Word Cloud - Search Terms(in Test Data)')
    savefig(os.path.dirname(os.path.abspath(__file__))+'/Output/Visualization/WordCloud - Search Terms(in Test Data).png')
    plt.show()
    input_file2.close()


    if os.path.isfile(filepath3):
        input_file3 = open(filepath3,'r')
    else:
        print "File does NOT exist"
        sys.exit()

    rdr = csv.reader(input_file3)
    header = rdr.next()
    output_data = [[] for i in header]
    
    output_count = 0
    actual_count = 0
    for l in input_file3:
        line = l.split(',')
        output_count += 1
        if len(line) == len(output_data):
            actual_count += 1
            for i in range(len(line)):
                output_data[i].append(line[i])
                #print i, line[i]
    
    plt.clf()
    wordcloud = WordCloud().generate(" ".join(output_data[4]))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.title('Word Cloud - Search Terms(in Combined data)')
    savefig(os.path.dirname(os.path.abspath(__file__))+'/Output/Visualization/WordCloud - Search Terms(in Combined data).png')
    plt.show()
    input_file3.close()



def PieChart(filepath):
    if os.path.isfile(filepath):
        input_file = open(filepath,'r')
    else:
        print "File does NOT exist"
        sys.exit()

    rdr = csv.reader(input_file)
    header = rdr.next()
    input_data = [ [] , [] ]

    count = 0

    for l in input_file:
        line = l.split(',')
        count += 1
        for i in range(len(line)):
            input_data[i].append(line[i])

    round_off_relevance = [float("%.2f" % float(i))  for i in input_data[1]]
    minrelevance = min(round_off_relevance)
    maxrelevance = max(round_off_relevance)
    
    diff = int(maxrelevance*100) - int(minrelevance*100)-1
    
    for i in [2,4,8]:
        arr_diff = []
        Data = []
        t_count = [0]

        for j in range(1,i):
            temp = minrelevance + (diff*float(j)/float(i))/100
            arr_diff.append(temp)
            if j == 1:
                Data.append(str(arr_diff[j-1])+"-"+str(minrelevance))
            else:
                Data.append(str(arr_diff[j-1])+"-"+str(arr_diff[j-2]))
            t_count.append(0)
        arr_diff.append(maxrelevance)
        Data.append(str(maxrelevance)+"-"+str(arr_diff[i-2]))
        
        for k in round_off_relevance:
            for l in arr_diff:
                if(k <= l):
                    t_count[arr_diff.index(l)] += 1
                    break

        tot = sum(t_count)
        Values = [float(k*100)/float(tot) for k in t_count]

        #print Values
        
        fig = {
            'data': [{'labels': Data,
                    'values': Values,
                    'type': 'pie'}],
            'layout': {'title': 'Piechart of Possible Relevancies - '+str(i)+' Splits'}
        }

        plot_url = py.plot(fig,filename = 'Piechart - '+str(i)+' Splits')
        print 'Piechart - '+str(i)+' Splits', plot_url


def ScatterPlot(filepath):
    if os.path.isfile(filepath):
        input_file = open(filepath,'r')
    else:
        print "File does NOT exist"
        sys.exit()

    rdr = csv.reader(input_file)
    header = rdr.next()
    input_data = [ [] , [] ]

    count = 0

    for l in input_file:
        line = l.split(',')
        count += 1
        for i in range(len(line)):
            input_data[i].append(line[i])

    round_off_relevance = [float("%.2f" % float(i))  for i in input_data[1]]
    minrelevance = min(round_off_relevance)
    maxrelevance = max(round_off_relevance)

    all_relevance = np.arange(minrelevance, maxrelevance+0.01, 0.01)
    relevance_count = []
    for i in range(int(minrelevance*100), int(maxrelevance*100)+1):
        relevance_count.append(round_off_relevance.count(float(float(i)/100)))

    trace = go.Scattergl(
        x = round_off_relevance,
        y = relevance_count,
        mode = 'markers',
    )
    data = [trace]

    plot_url = py.plot(data, filename='ScatterPlot - Count of All Relevancies')
    print 'ScatterPlot - Count of All Relevancies', plot_url