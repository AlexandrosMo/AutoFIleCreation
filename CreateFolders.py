import os
 

def CreateFolders():
        create_folder =('January,February,March,April,May,June,July,August,September,October,November,December')
        
        for month in create_folder.split(','):
            if not os.path.exists(f"CreateFiles/{month}"):
                os.makedirs(f"CreateFiles/{month}")

            letter =('A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z')
            for letter in letter.split(','):
                os.makedirs(f"CreateFiles/{month}/{letter}")
CreateFolders()
