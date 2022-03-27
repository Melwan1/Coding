from time import gmtime

calendar=[[2022,3,26,18,15,"test"],[2022,3,27,9,2,"autre test"],[2022,4,16,19,13,"encore test"]]

def table_to_timestamp(table):
    year,month,day,hour,minute=table[:5]
    timestamp=0
    timestamp+=(year-1970)*31536000
    if year %4 == 0:
        daysYear=[0,0,31,60,91,121,152,182,213,244,274,305,335,366]
    else:
        daysYear=[0,0,31,59,90,120,151,181,212,243,273,304,334,365]
    timestamp+=(daysYear[month]+day-1)*86400
    timestamp+=hour*3600
    timestamp+=minute*60
    return timestamp
    

def see_calendar_day(calendar):
    print("")
    i=0
    now=gmtime()
    while i < len(calendar) and calendar[i][2]==now[2]:
        year,month,day,hour,minute,task=calendar[i]
        if hour>=now[3]:
            if day<10:
                day="0"+str(day)
            if month<10:
                month="0"+str(month)
            if hour<10:
                hour="0"+str(hour)
            if minute<10:
                minute="0"+str(minute)
            print(i+1," | ",day,"/",month,"/",year," ",hour,":",minute," - ",task,sep="")
        i+=1
    interface_initiale()

def see_calendar_week(calendar):
    i=0
    year,month,day,hour,minute,task=calendar[i]
    if year %4 == 0:
        daysYear=[0,0,31,60,91,121,152,182,213,244,274,305,335,366]
    else:
        daysYear=[0,0,31,59,90,120,151,181,212,243,273,304,334,365]
    
    now=gmtime()
    while i < len(calendar):
        year,month,day,hour,minute,task=calendar[i]
        if daysYear[int(month)]+int(day)<=now[7]+6:
            if hour>=now[3] or daysYear[int(month)]+int(day)>now[7]:
                if day<10:
                    day="0"+str(day)
                if month<10:
                    month="0"+str(month)
                if hour<10:
                    hour="0"+str(hour)
                if minute<10:
                    minute="0"+str(minute)
                print(i+1," | ",day,"/",month,"/",year," ",hour,":",minute," - ",task,sep="")
        i+=1
    interface_initiale()

def see_calendar_month(calendar):
    i=0
    year,month,day,hour,minute,task=calendar[i]
    if year %4 == 0:
        daysYear=[0,0,31,60,91,121,152,182,213,244,274,305,335,366]
    else:
        daysYear=[0,0,31,59,90,120,151,181,212,243,273,304,334,365]
    
    now=gmtime()
    while i < len(calendar):
        year,month,day,hour,minute,task=calendar[i]
        if daysYear[int(month)]+int(day)<=now[7]+daysYear[int(month)+1]-daysYear[int(month)]:
            if hour>=now[3] or daysYear[int(month)]+int(day)>now[7]:
                if day<10:
                    day="0"+str(day)
                if month<10:
                    month="0"+str(month)
                if hour<10:
                    hour="0"+str(hour)
                if minute<10:
                    minute="0"+str(minute)
                print(i+1," | ",day,"/",month,"/",year," ",hour,":",minute," - ",task,sep="")
        i+=1
    interface_initiale()

def see_whole_calendar(calendar):
    print("")
    i=0
    while i < len(calendar):
        year,month,day,hour,minute,task=calendar[i]
        if day<10:
            day="0"+str(day)
        if month<10:
            month="0"+str(month)
        if hour<10:
            hour="0"+str(hour)
        if minute<10:
            minute="0"+str(minute)
        print(i+1," | ",day,"/",month,"/",year," ",hour,":",minute," - ",task,sep="")
        i+=1
    interface_initiale()

def ajout_calendrier(calendar,taskPlus):
    calendar2=[]
    n=len(calendar)
    i=0
    daysYear=[0,0,31,60,91,121,152,182,213,244,274,305,335,366]
    time1 = taskPlus[0]*525600+(daysYear[taskPlus[1]]+taskPlus[2])*1440+taskPlus[3]*60+taskPlus[4]
    while i < n:
        time2 = calendar[i][0]*525600+(daysYear[calendar[i][1]]+calendar[i][2])*1440+calendar[i][3]*60+calendar[i][4]
        if time1<=time2:
            calendar2.append(taskPlus)
            k=i
            for j in range(k+1,n):
                calendar2.append(calendar[j])
            i=n
        else:
            calendar2.append(calendar[i])
            i+=1
    if n==len(calendar2):
        calendar2.append(taskPlus)
    
    calendar=calendar2
    interface_initiale()
            
"""
Interface initiale
"""



def interface_initiale():
    print("")
    maintenant=gmtime()
    tousJours = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
    tousMois = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
    jour=tousJours[maintenant[6]]
    mois=tousMois[maintenant[1]-1]
    print(jour,maintenant[2],mois,maintenant[0],"                                                                            ",maintenant[3]+1,"h",maintenant[4])
    
    print("")
    print(1,"Consulter le calendrier")
    print(2,"Modifier le calendrier")
    print(3,"")
    print(4,"")
    action=int(input("Que faire ? "))
    
    if action==1:
        print(1,"Vue journalière")
        print(2,"Vue hebdomadaire")
        print(3,"Vue mensuelle")
        print(4,"Calendrier complet")
        print(4,"Retour à l'écran initial" )
        action=int(input("Que faire ? "))
        
        if action==1:
            see_calendar_day(calendar)
        if action==2:
            see_calendar_week(calendar)
        if action==3:
            see_calendar_month(calendar)
        if action==4:
            see_whole_calendar(calendar)
        if action==5:
            interface_initiale()
    
    if action==2:
        print(1,"Ajouter une tâche")
        print(2,"Supprimer une tâche")
        print(3,"Retour à l'écran initial")
        
        action=int(input("Que faire ?"))
        if action==1:
            annee=int(input("Année de la tâche"))
            mois=int(input("Mois de la tâche"))
            jour=int(input("Jour de la tâche"))
            heure=int(input("Heure de la tâche"))
            minute=int(input("Minute de la tâche"))
            tache=str(input("Nom de la tâche"))
            ajout_calendrier(calendar,[annee,mois,jour,heure,minute,tache])
            print("Nouveau calendrier :",calendar)
interface_initiale()
