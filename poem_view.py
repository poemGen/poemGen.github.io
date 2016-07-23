import os
from lxml import html
from bs4 import BeautifulSoup
import requests


#record = open('record\\' + timestamp, 'w')
#record.write(poem)
#record.close()

#path = "C:\\Users\\MelanieandStephen\\Desktop\\coding\\poemGen 2.0\\record\\"
path = "raw_poems/"
include_path = "include/"
site_path = ""
#poempath = 

allSnippets = []
startSnip = 0
stopSnip = 0
title = ''
lines = ''


def build_poem_display_files(filename):
        raw_poem = open(path + filename, 'r')
        raw_poem = raw_poem.read()
        header = open(include_path + 'poem_header.html', 'r')
        header = header.read()
        footer = open(include_path + 'footer.html', 'r')
        footer = footer.read() 
        poem_html = open("poems/" + filename, 'w')  
        poem_html.write(header)
        poem_html.close()
        poem_html = open("poems/" + filename, 'a')  
        poem_html.write(raw_poem)
        poem_html.write(footer)
        poem_html.close()


for filename in os.listdir(path):
    build_poem_display_files(filename)
#    print filename
    snippet = []
    content = open(path + filename, 'r')
    content = content.read()
#    print content
#    break
    openTagCount = 0
    closeTagCount = 0
    charCount = -1 
    for tag in content:
        charCount += 1 
        if tag == "<":
            openTagCount += 1
        elif tag == ">":
            closeTagCount += 1
        if openTagCount == 2:
            title = content[21:charCount - 7] 
        if closeTagCount == 3:
            startSnip = charCount + 2
#            print startSnip
        if closeTagCount == 6:
            stopSnip = charCount - 6
#            print stopSnip        
        lines = content[startSnip:stopSnip]
    snippet.append(filename)
    snippet.append(title)
    snippet.append(lines)
    allSnippets.append(snippet)
    

#print len(allSnippets)
#print allSnippets


def strip_tags(allSnippets):
    cleantext = []
    for snippet in allSnippets:
        cleansnippet = []
#        print snippet
        for title_lines in snippet:
            cleansnippet.append(BeautifulSoup(title_lines, "lxml").text)
        cleantext.append(cleansnippet)
    return cleantext
    
    
    
def add_ptag(snippet):
#    if "\n" in snippet[1]:
#        snippet[2].replace("\n", "</p><p class=\"lead\">")
    lines = "</p><p class=\"lead\">".join(snippet.split("\n"))
#    print lines
    return lines
    
    

    
    
    
def build_snippet_page(snippets):
        header = open(include_path + 'header.html', 'r')
        header = header.read()       
        snippet_page = open(site_path + 'snippets.html', 'w')
        snippet_page.write(header)
        snippet_page.close()
        for snippet in snippets:
            lines = add_ptag(snippet[2])
            top = open(include_path + 'top_snippet-body.html', 'r')
            top = top.read()
            snippet_body = open(include_path + 'snippet-body.html', 'w')
            snippet_body.write(top)
            snippet_body.close()
            snippet_body = open(include_path + 'snippet-body.html', 'a')
            snippet_body.write(snippet[0] + "\"" + ">" + snippet[1] + "</a>" + "</span> </h3> <h2></h2>")
            snippet_body.write("<p class=\"lead\">" + lines + "</p>")
            snippet_body.close()            
            bottom = open(include_path + 'bottom_snippet_body.html', 'r')
            bottom = bottom.read()
            snippet_body = open(include_path + 'snippet-body.html', 'a')            
            snippet_body.write(bottom)
            snippet_body.close()
            snippet_body = open(include_path + 'snippet-body.html', 'r')
            snippet_body = snippet_body.read()
            snippet_page = open(site_path + 'snippets.html', 'a')
            snippet_page.write(snippet_body)
        footer = open(include_path + 'footer.html', 'r')
        footer = footer.read()       
        snippet_page = open(site_path + 'snippets.html', 'a')
        snippet_page.write(footer)
        snippet_page.close()
            

            
            
            
  
    
#################################################################################        
        
snippets = strip_tags(allSnippets)

print build_snippet_page(snippets)








        
    

        
            
                
                
    
    
    
    

        
    




        

        
   
    
    