import psycopg2
import csv

def createTableManually(conn,cur):
    cur.execute('''CREATE TABLE COMPANY
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL);''')
    print("Table created successfully")
     
    #insert into table
    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )");
     
    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
     
    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
     
    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
     
    conn.commit()
    print("Records created successfully")
    
    
def createTableFromCSV(conn,cur):    
    cur.execute(''' CREATE TABLE ENDTOENDWORKSHOP
           (ID INT PRIMARY KEY         NOT NULL,
           first_name           TEXT   NOT NULL,
           last_name            TEXT   NOT NULL,
           email                TEXT   NOT NULL,
           country              TEXT   NOT NULL,
           gender               TEXT   NOT NULL); ''')
                   
    f = open(r'EndToEndWorkshop1.csv', 'r')
    cur.copy_from(f, 'ENDTOENDWORKSHOP', sep=',')
    conn.commit()
    f.close()
     
    print("Created table successfully")
    

def createTableFromCSVAutomatically(conn,cur):    
    fieldnames = []
    with open('Biosciences.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        #get fieldnames from DictReader object and store in list
        fieldnames = reader.fieldnames
    
    sql_table = 'CREATE TABLE research_bio (%s)' % ','.join('%s VARCHAR(150)' % name for name in fieldnames)
    cur.execute(sql_table)
   
    each_row_dict = []
    with open('Biosciences.csv') as csvfile:
        reader = csv.DictReader(csvfile)
           
        sql_insert = ('INSERT INTO research_bio (%s) VALUES (%s)' %
              (','.join('%s' % name for name in fieldnames),
               ','.join('%%(%s)s' % name for name in fieldnames)))
           
        for row in reader:
            each_row_dict.append(row) 
               
        cur.executemany(sql_insert, each_row_dict)
          
        conn.commit()
     
    print("Created table successfully")


if __name__ == "__main__":
    
    #Connect To Database
    conn = psycopg2.connect(database="Synapse", user="postgres", password="FeedTheApples", host="127.0.0.1", port="5432")
    print("Opened database successfully")
    
    #define a cursor to work with by getting a cursor from the connection
    cur = conn.cursor()
    
    
    #Create table from csv
    createTableFromCSVAutomatically(conn,cur)
    
    #release the resources 
    conn.close()
