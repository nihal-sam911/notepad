# connector 

import mysql.connector as m


class database :
    
    def connection():
        
        try:
            
            con = m.connect (
                  host="localhost",
                  user="root",
                  password="password",
                  database="notepad")

            
            if con.is_connected() : 
                print("successfully conencted")
                return con

            except m.Error as e:
                print(f"connection failed: {e}")
                return None



             


   def create():
       h
       con = connection()
       if con is None:
           
           return false
           cur = con.cusor()
           query = "CREATE IF NOT EXISTS notepad;" #NOT COMPLETED

           cur.execute(query)
           cur.close()
           con.close()





    

