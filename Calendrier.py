from time import gmtime

calendrier=[[2022,3,26,18,15,"test"],[2022,3,27,9,2,"autre test"],[2022,4,16,19,13,"encore test"]]


def voir_calendrier_jour(calendrier):
    print("")
    i=0
    maintenant=gmtime()
    while i < len(calendrier) and calendrier[i][2]==maintenant[2]:
        annee,mois,jour,heure,minute,tache=calendrier[i]
        if heure>=maintenant[3]:
            if jour<10:
                jour="0"+str(jour)
            if mois<10:
                mois="0"+str(mois)
            if heure<10:
                heure="0"+str(heure)
            if minute<10:
                minute="0"+str(minute)
            print(i+1," | ",jour,"/",mois,"/",annee," ",heure,":",minute," - ",tache,sep="")
        i+=1

def voir_calendrier_semaine(calendrier):
    i=0
    annee,mois,jour,heure,minute,tache=calendrier[i]
    if annee %4 == 0:
        jourAnnee=[0,0,31,60,91,121,152,182,213,244,274,305,335,366]
    else:
        jourAnnee=[0,0,31,59,90,120,151,181,212,243,273,304,334,365]
    
    maintenant=gmtime()
    while i < len(calendrier):
        annee,mois,jour,heure,minute,tache=calendrier[i]
        if jourAnnee[int(mois)]+int(jour)<=maintenant[7]+6:
            if heure>=maintenant[3] or jourAnnee[int(mois)]+int(jour)>maintenant[7]:
                if jour<10:
                    jour="0"+str(jour)
                if mois<10:
                    mois="0"+str(mois)
                if heure<10:
                    heure="0"+str(heure)
                if minute<10:
                    minute="0"+str(minute)
                print(i+1," | ",jour,"/",mois,"/",annee," ",heure,":",minute," - ",tache,sep="")
        i+=1

def voir_calendrier_mois(calendrier):
    i=0
    annee,mois,jour,heure,minute,tache=calendrier[i]
    if annee %4 == 0:
        jourAnnee=[0,0,31,60,91,121,152,182,213,244,274,305,335,366]
    else:
        jourAnnee=[0,0,31,59,90,120,151,181,212,243,273,304,334,365]
    
    maintenant=gmtime()
    while i < len(calendrier):
        annee,mois,jour,heure,minute,tache=calendrier[i]
        if jourAnnee[int(mois)]+int(jour)<=maintenant[7]+jourAnnee[int(mois)+1]-jourAnnee[int(mois)]:
            if heure>=maintenant[3] or jourAnnee[int(mois)]+int(jour)>maintenant[7]:
                if jour<10:
                    jour="0"+str(jour)
                if mois<10:
                    mois="0"+str(mois)
                if heure<10:
                    heure="0"+str(heure)
                if minute<10:
                    minute="0"+str(minute)
                print(i+1," | ",jour,"/",mois,"/",annee," ",heure,":",minute," - ",tache,sep="")
        i+=1

def voir_calendrier(calendrier):
    print("")
    i=0
    while i < len(calendrier):
        annee,mois,jour,heure,minute,tache=calendrier[i]
        if jour<10:
            jour="0"+str(jour)
        if mois<10:
            mois="0"+str(mois)
        if heure<10:
            heure="0"+str(heure)
        if minute<10:
            minute="0"+str(minute)
        print(i+1," | ",jour,"/",mois,"/",annee," ",heure,":",minute," - ",tache,sep="")
        i+=1

def ajout_calendrier(calendrier,tachePlus):
    calendrier2=[]
    n=len(calendrier)
    i=0
    jourAnnee=[0,0,31,60,91,121,152,182,213,244,274,305,335,366]
    temps1 = tachePlus[0]*525600+(jourAnnee[tachePlus[1]]+tachePlus[2])*1440+tachePlus[3]*60+tachePlus[4]
    while i < len(calendrier):
        temps2 = calendrier[i][0]*525600+(jourAnnee[calendrier[i][1]]+calendrier[i][2])*1440+calendrier[i][3]*60+calendrier[i][4]
        if temps1<=temps2:
            calendrier2.append(tachePlus)
            for j in range(i+1,n):
                calendrier2.append(calendrier[j])
        else:
            calendrier2.append(calendrier[i])
            i+=1
    if n==len(calendrier2):
        calendrier2.append(tachePlus)
            
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
            voir_calendrier_jour(calendrier)
        if action==2:
            voir_calendrier_semaine(calendrier)
        if action==3:
            voir_calendrier_mois(calendrier)
        if action==4:
            voir_calendrier
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
            ajout_calendrier(calendrier,[annee,mois,jour,heure,minute,tache])
            
interface_initiale()