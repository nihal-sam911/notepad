# connector 

import mysql.connector as m


class database :
    
    def connection(self):
        
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



             


   def create(self):
       
       con = self.connection()
       if con is None:
           return false
           
           cur = con.cusor()
           query = "CREATE IF NOT EXISTS notepad( 
                    id int auto_increment primary key,
                    Title varchar(300) not null,
                    content text,
                    UPDATED_AT timestamp default current_timestamp on update current_timestamp);"

           cur.execute(query)
           con.commit()
           cur.close()
           con.close()






#---------





    

