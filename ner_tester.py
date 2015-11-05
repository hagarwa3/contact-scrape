from nltk.tag.stanford import NERTagger
import os
print "hahahahah"
java_path = "C:/Program Files/Java/jdk1.7.0_71/bin/java.exe"
os.environ['JAVAHOME'] = java_path
print "java"
st = NERTagger('C:/Users/Harshit Agarwal/Downloads/stanford-ner-2014-06-16/stanford-ner-2014-06-16/classifiers/english.all.3class.distsim.crf.ser.gz','C:/Users/Harshit Agarwal/Downloads/stanford-ner-2014-06-16/stanford-ner-2014-06-16/stanford-ner.jar')
print st.tag('Sarita Adve hi Molly Flesner hi hello'.split()) 
print "okdone"