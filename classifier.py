import os,shutil

cwd=os.getcwd() #Argument to be passed later
direc=os.listdir(cwd)

files={}
files["Images"]={}
files["Images"][".JPG"]='jpg'
files["Images"][".PNG"]='png'
files["Images"][".JPEG"]='jpeg'
files["Images"][".GIF"]='gif'
files["Videos"]={}
files["Videos"]["MP4"]='mp4'
files["Videos"]["MKV"]='mkv'
files["Videos"]["FLV"]='flv'
files["Videos"][".MOV"]='mov'
files["Videos"][".AVI"]='avi'
files["Documents"]={}
files["Documents"]["Word"]=['doc','docx']
files["Documents"]["Html"]=['html','htm']
files["Documents"]["PDF"]='pdf'
files["Documents"]["Excel"]=['xls','xlsx','xlr']
files["Documents"]["Presentations"]=['ppt','pptx',"pps"]

def Func(name):
    x=name.lower()
    t=''
    for i in files.keys():
        os.chdir(cwd)
        for j in files[i].keys():
            if x == files[i][j]:
                if not os.path.exists(i):
                    os.makedirs(i)
                os.chdir(os.path.join(os.getcwd(),i))
                    
                if not os.path.exists(j):
                    os.makedirs(j)
                t=i+'\\'+j
                break
    return (os.getcwd()+"\\"+t)

for x in range(len(direc)):
    if(direc[x]=="classifier.py"):
        continue
    f=Func(direc[x].split('.')[len(direc[x].split('.'))-1])
    os.system('move '+ direc[x] + " " + f)
    print("moved {} file to {} directory".format(direc[x],f))